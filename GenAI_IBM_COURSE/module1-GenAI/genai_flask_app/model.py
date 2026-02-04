from langchain_ibm import ChatWatsonx
from langchain.prompts import PromptTemplate
from config import PARAMETERS, LLAMA3_MODEL_ID, GRANITE_MODEL_ID, MIXTRAL_MODEL_ID


# Function to initialize a model
def initialize_model(model_id):
    return ChatWatsonx(
        model_id=model_id,
        url="https://us-south.ml.cloud.ibm.com",
        project_id="skills-network",
        params=PARAMETERS,
    )


# Initialize models
llama3_llm = initialize_model(LLAMA3_MODEL_ID)
granite_llm = initialize_model(GRANITE_MODEL_ID)
mixtral_llm = initialize_model(MIXTRAL_MODEL_ID)

llama3_template = PromptTemplate(
    template="""
    <|begin_of_text|>
    <|start_header_id|>system<|end_header_id|>{system_prompt}<end_of_id>
    <|start_header_id|>user<|end_header_id|>{user_prompt}<end_of_id>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=["system_prompt", "user_prompt"],
)

granite_template = PromptTemplate(
    template="""
        <|system|>{system_prompt}\n\<|user|>{user_prompt}\n<|assistant|>
    """,
    input_variables=["system_prompt", "user_prompt"],
)

mixtral_template = PromptTemplate(
    template="""
        <s>[INST]{system_prompt}\n{user_prompt}[/INST]
    """,
    input_variables=["system_prompt", "user_prompt"],
)


def get_ai_response(model, template, system_prompt, user_prompt):
    chain = template | model
    return chain.invoke({"system_prompt": system_prompt, "user_prompt": user_prompt})


# Model-specific response functions
def llama3_response(system_prompt, user_prompt):
    return get_ai_response(llama3_llm, llama3_template, system_prompt, user_prompt)


def granite_response(system_prompt, user_prompt):
    return get_ai_response(granite_llm, granite_template, system_prompt, user_prompt)


def mixtral_response(system_prompt, user_prompt):
    return get_ai_response(mixtral_llm, mixtral_template, system_prompt, user_prompt)
