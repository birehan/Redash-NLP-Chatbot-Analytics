import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from logger import logger

# Load environment variables from .env file
load_dotenv()

# Access the values using os.environ.get()
connection_params = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT")
}

# Use the connection_params as needed in your script

def create_table_query(df: pd.DataFrame, table_name: str) -> str:
    """
    Generate a CREATE TABLE query for a PostgreSQL database table based on a Pandas DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame used for generating the query.
        table_name (str): Name of the database table.

    Returns:
        str: The CREATE TABLE query as a string.
    """
    try:
        # Convert column names to lowercase, replace spaces with underscores,
        # and replace parentheses with empty strings
        df.columns = [column.lower().replace(' ', '_').replace('(', '').replace(')', '') for column in df.columns]

        data_type_mapping = {
            'int64': 'INTEGER',
            'float64': 'DOUBLE PRECISION',
            'object': 'TEXT',
            'datetime64[ns]': 'DATE'
        }

        column_definitions = ', '.join([f'"{column}" {data_type_mapping.get(str(df[column].dtype), "TEXT")}' for column in df.columns])

        primary_key_columns = ['"' + df.columns[0] + '"']

        if table_name in ['viewership_by_date_table_data', "totals_table_data"]:
            primary_key_columns = ['"' + df.columns[0] + '"']

        elif df.columns[0] == "Date":
            primary_key_columns.append('"' + df.columns[1] + '"')

        primary_key_constraint = f'PRIMARY KEY ({", ".join(primary_key_columns)})'

        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {column_definitions},
                {primary_key_constraint}
            );
        '''
        return create_table_query

    except Exception as e:
        logger.error(f"Error creating table query: {e}")
        return ''



def run_sql_query(query: str) -> None:
    """
    Execute a SQL query on a PostgreSQL database.

    Parameters:
        query (str): SQL query to be executed.

    Returns:
        None: This function does not return any value.
    """
    try:
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logger.info("Log success")

    except Exception as e:
        logger.error(f"Log the error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return None

def populate_dataframe_to_database(df: pd.DataFrame, table_name: str) -> None:
    """
    Insert a Pandas DataFrame into a PostgreSQL database table.

    Parameters:
        df (pd.DataFrame): The DataFrame to be inserted.
        table_name (str): Name of the database table.

    Returns:
        None: This function does not return any value.
    """
    try:
        db_url = f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}"
        engine = create_engine(db_url, echo=False)

        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        logger.info(f"Inserted {len(df)} rows into the database table {table_name}.")

    except Exception as e:
        logger.error(f"Error inserting data into the database: {e}")

    finally:
        if engine:
            engine.dispose()

    return None




def get_postgres_data(query: str) -> tuple:
    """
    Execute a SQL query on a PostgreSQL database and return the results and cursor description.

    Parameters:
        query (str): SQL query to be executed.

    Returns:
        tuple: A tuple containing the results and cursor description.

    Raises:
        Exception: If there is an error during the execution or fetching of data.
    """
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        description = cursor.description
        logger.info("Successfully executed query and fetched data from the database.")
        return results, description

    except Exception as e:
        error_message = f"Error executing query or fetching data from the database: {e}"
        logger.error(error_message)
        raise Exception(error_message)

    finally:
        cursor.close()
        conn.close()
        logger.info("Database connection closed.")


def get_postgres_df(query: str) -> pd.DataFrame:
    """
    Execute a SQL query on a PostgreSQL database and return the results as a Pandas DataFrame.

    Parameters:
        query (str): SQL query to be executed.

    Returns:
        pd.DataFrame: The results of the query as a Pandas DataFrame.

    Raises:
        Exception: If there is an error during the execution or conversion of query results.
    """
    try:
        results, description = get_postgres_data(query)
        columns = [desc[0] for desc in description]
        df = pd.DataFrame(results, columns=columns)
        logger.info("Successfully converted query results to a Pandas DataFrame.")
        return df

    except Exception as e:
        error_message = f"Error converting query results to Pandas DataFrame: {e}"
        logger.error(error_message)
        raise Exception(error_message)
