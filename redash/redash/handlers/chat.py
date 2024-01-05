from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
import requests
# from redash.handlers.langchain.exectuors import get_agent_executor

import os

from openai import OpenAI
VARIABLE_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
  api_key=VARIABLE_KEY
)

api_url = os.environ.get("API_URL")

class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            question = value.get('question')

            question_answer = requests.post("https://8365-197-156-71-84.ngrok-free.app/api/chat", json={"message": question})
            # https://8365-197-156-71-84.ngrok-free.app
            # response_data = {"answer": question_answer.text}
            # return jsonify(response_data), 200

            

            if question_answer.status_code == 200:
                api_response = question_answer.json()
                answer = api_response.get("data")

                response_data = {"answer": answer}
                return jsonify(response_data), 200

            else:
                return jsonify({"error": f"An error occurred"}), 500

            # completion = client.chat.completions.create(
            #     model="gpt-4-1106-preview",
            #     messages=[
            #         {"role": "system", "content": "You are a redash visualization assistant, skilled in SQL queries and data visualization. You are only required to give answers for query and data visualization questions. If asked about a topic outside these two, make sure to respond that you have no information regarding that question. I am only here to help you with your query and data visualization questions. When asked to write queries, only provide the code without descriptions."},
            #         {"role": "user", "content": question}
            #     ]
            # )
            # answer = completion.choices[0].message.content

            
        except Exception as error:
            return jsonify({"error": f"An error occurred {error}"}), 500