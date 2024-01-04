from langchain.agents import AgentExecutor
from agents import get_agent_analyst

from tools import execute_sql,get_table_columns,get_table_column_distr


def get_agent_executor():
    analyst_agent_executor = AgentExecutor(
        agent=get_agent_analyst(),
        tools=[execute_sql, get_table_columns, get_table_column_distr],
        verbose=True,
        max_iterations=10, # early stopping criteria
        early_stopping_method='generate',
        # to ask model to generate the final answer after stopping
    )

    return analyst_agent_executor






# analyst_agent_executor.invoke(
#   {"question": "what is the Device type having the highest Average view duration?"}
# )
