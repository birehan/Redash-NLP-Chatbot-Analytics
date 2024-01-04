import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

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
        return results, description

    except Exception as e:
        error_message = f"Error executing query or fetching data from the database: {e}"
        raise Exception(error_message)

    finally:
        cursor.close()
        conn.close()


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
        return df

    except Exception as e:
        error_message = f"Error converting query results to Pandas DataFrame: {e}"
        raise Exception(error_message)
