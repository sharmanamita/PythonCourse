# from langchain_community.chains import LLMChain - its deprecated and removed from packages
# use LCEL pattern

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnablePassthrough

location_prompt = """
    Your job is to come up with a classic dish from the area that the users suggests. {location}
    YOUR RESPONSE:
"""

receipe_prompt = """
    Your job is to find receipe of the dish that the user suggests. {dish}
    YOUR RESPONSE:
"""

estimated_time_prompt = """
    Your job is to find the estimated time to cook the dish that the user suggests. {receipe}
    YOUR RESPONSE:
"""

llm = init_chat_model(model="gpt-4o-mini", model_provider="openai", temperature=0.5)

location_chain_LCEL = (
    PromptTemplate.from_template(location_prompt)
    | llm
    | StrOutputParser()
)

receipe_chainLCEL = (
    PromptTemplate.from_template(receipe_prompt)
    | llm
    | StrOutputParser()
)

estimated_time_chainLCEL = (
    PromptTemplate.from_template(estimated_time_prompt)
    | llm
    | StrOutputParser()
)

overall_chain_lcel = (
    RunnablePassthrough.assign(dish=lambda x: location_chain_LCEL.invoke({"location": x["location"]}))
    | RunnablePassthrough.assign(receipe=lambda x: receipe_chainLCEL.invoke({"dish": x["dish"]}))
    | RunnablePassthrough.assign(time=lambda x: estimated_time_chainLCEL.invoke({"receipe": x["receipe"]}))
)

# Run the chain
result = overall_chain_lcel.invoke({"location": "India"})
print(result['location'])
print(result['dish'])
print(result['receipe'])
print(result['time'])