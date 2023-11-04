import ast
import json

import openai
from sqlalchemy import text
from describe_database import get_db_schema

with open('db_config.json', 'r') as f:
    db_config = json.load(f)

# Load the API key from api_key.txt
with open('api_key.txt', 'r') as f:
    openai_api_key = f.read().strip()

# variable to access GPT-3


# Function to initialize session with GPT-3, make it aware of the database schema, and it's purpose as a Chef Companion
def initialize_session():
    db_schema = get_db_schema(
        db_config["host"],
        db_config["user"],
        db_config["password"],
        db_config["database"],
    )
    from app import messages

    prompt = (
        "You are a Chef Companion. You are a chatbot that helps chefs with their daily tasks. "
        "You will interface with a mysql database and help a chef track their ingredients and recipes."
        "If the user reveals that they possess an ingredient, you will add it to the database. "
        "If a user asks to save a recipe, you should add it to the database along with the required ingredients and steps."
        "Your goal is to make the user's interface between the database and the Chef Companion as seamless as possible."
        f"The database you will be interfacing with is described as such: {db_schema}"
        f"The first question you ask will be What would you like to cook today? You should ask probing questions"
        f"to help the chef decide what they can cook."
    )
    messages.append({"role": "system", "content": f"{prompt}"})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613", messages=messages,
        )
        response_message = response["choices"][0]["message"]
        print(response_message)
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    return response["choices"][0]["message"]



# Function to execute SQL query generated from AI response
def execute_sql(sql_query: str):
    from app import app, db

    results = "Query executed successfully."
    with app.app_context():
        try:
            result = db.session.execute(text(sql_query))
            if result.returns_rows:
                results = str(result.fetchall())
            db.session.commit()
        except Exception as e:
            print(str(e))
            return f"Error executing query: {str(e)}"
    return results

# Function to send message back to human
def reply(message: str):
    return message


# Function to send input to GPT-3 and parse output
def send_message(messages: list):
    functions = [
        {
            "name": "execute_sql",
            "description": "Execute a SQL query using the app's database context",
            "parameters": {
                "type": "object",
                "properties": {
                    "sql_query": {
                        "type": "string",
                        "description": "The SQL query to execute",
                    },
                },
                "required": ["sql_query"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", messages=messages,
        functions = functions,
        function_call="auto"
    )
    response_message = response["choices"][0]["message"]
    while response_message.get("function_call"):
        print(response_message)
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle error
        function_name = response_message["function_call"]["name"]
        function_to_call = FUNCTION_MAP[function_name]
        function_args = [val for key, val in json.loads(response_message["function_call"]["arguments"]).items()]
        function_response = function_to_call(*function_args)
        if function_response is None:
            function_response = ""
        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
            function_call="auto",
        )  # get a new response from GPT where it can see the function response
        response_message = second_response["choices"][0]["message"]

    return response_message["content"]




def parse_output(gpt_output: str):
    instructions = ast.literal_eval(gpt_output)
    for i, fn in enumerate(instructions["functions"]):
        if fn == "reply":
            return FUNCTION_MAP[fn](instructions["args"][i])
        else:
            FUNCTION_MAP[fn](instructions["args"][i])


FUNCTION_MAP = {"execute_sql": execute_sql, "reply": reply}


def test():
    execute_sql("SELECT * FROM ingredients")
