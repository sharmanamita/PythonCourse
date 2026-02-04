from flask.cli import load_dotenv
from openai import OpenAI
import os

load_dotenv()
Test_Key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=Test_Key)

def llm_model(prompt, model="gpt-4.1"):
    response = client.responses.create(
        model=model,
        input=prompt
    )
    return response.output_text