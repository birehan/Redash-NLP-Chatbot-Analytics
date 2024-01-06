import unittest
from unittest.mock import MagicMock
import os
import sys
import psycopg2



sys.path.append(os.path.abspath(os.path.join('../scripts')))
from scripts import run_sql_query

class TestRunSQLQuery(unittest.TestCase):

    def setUp(self):
        # Define your connection parameters for testing
        self.test_connection_params = {
            'dbname': 'your_test_db',
            'user': 'your_test_user',
            'password': 'your_test_password',
            'host': 'your_test_host',
            'port': 'your_test_port'
        }

    def test_run_sql_query_success(self):
        # Define a test SQL query
        test_query = "INSERT INTO your_table (column1, column2) VALUES (value1, value2);"

        # Mock the psycopg2.connect method
        psycopg2.connect = MagicMock()

        # Call the function with the test parameters
        run_sql_query(self.test_connection_params, test_query)

        # Assert that psycopg2.connect was called with the correct parameters
        psycopg2.connect.assert_called_once_with(**self.test_connection_params)

    def test_run_sql_query_error(self):
        # Define a test SQL query that will cause an error
        test_query = "INVALID SQL QUERY;"

        # Mock the psycopg2.connect method
        psycopg2.connect = MagicMock()

        # Call the function with the test parameters
        run_sql_query(self.test_connection_params, test_query)

        # Assert that psycopg2.connect was called with the correct parameters
        psycopg2.connect.assert_called_once_with(**self.test_connection_params)

        # Assert that the error message is logged
        # This depends on how you handle errors in your actual code
        # You may need to modify this part based on your logging approach
        self.assertIn("Log the error:", self.capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
