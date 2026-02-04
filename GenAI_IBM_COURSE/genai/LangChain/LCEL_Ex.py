# Steps tp define LCEL (LangChain External Language Model) example
# 1. Define content with template variable with curly braces {}
# 2. create instance of PromptTemplate
# 3. 

# IBM Watsonx model configuration (commented out)
# model_id = "meta-llama/llama-3-405b-instruct"

# parameters = {
#     GenParams.MAX_NEW_TOKENS: 256,  # this controls the maximum number of tokens in the generated output
#     GenParams.TEMPERATURE: 0.5, # this randomness or creativity of the model's responses
# }

# url = "https://us-south.ml.cloud.ibm.com"
# project_id = "skills-network"

# llm = WatsonxLLM(
#         model_id=model_id,
#         url=url,
#         project_id=project_id,
#         params=parameters
#     )

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain.chat_models import init_chat_model
from langchain_core.language_models import ModelProfileRegistry
import os


content = "Tell me a {adjective} joke about {subject}"
prompt = PromptTemplate.from_template(content)

def format_prompt(inputs: dict) -> str:
    return prompt.format(**inputs)

# Initialize an OpenAI-backed chat model via LangChain.
# Replace "openai:gpt-4.1" with a model you have access to.
# Run this cmd before running the code -> $env:OPENAI_API_KEY="your_openai_api_key"
# llm = init_chat_model(model="gpt-5", model_provider="openai", temperature=0.5)
llm = init_chat_model("openai:gpt-5", temperature=0.5)

joke_chain = (
    RunnableLambda(format_prompt)
    | llm
    | StrOutputParser()
)

result = joke_chain.invoke({"adjective": "funny", "subject": "chickens"})
print(result)