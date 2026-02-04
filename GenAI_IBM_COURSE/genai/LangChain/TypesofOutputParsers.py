from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, CommaSeparatedListOutputParser
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

# StrOutputParsers - used to format the output frpom LLms in string structured way.
llm = init_chat_model(model="gpt-5", model_provider="openai", temperature=0.5)

prompt = PromptTemplate.from_template("Tell me a joke about {subject}")

response = prompt | llm | StrOutputParser()

result = response.invoke({"subject": "cats"})
print(result)


# JsonOutputParser - used to format the output from LLMs in JSON structured way.
class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")

json_parser = JsonOutputParser(pydantic_object=Joke)
json_instructions = json_parser.get_format_instructions()

# Solution 1: Using from_template method
prompt = PromptTemplate.from_template(
    "Generate a joke about {subject} in the following JSON format:\n{format_instructions}\n"
)

# Solution 2: Using PromptTemplate constructor
# prompt = PromptTemplate(
#     template="Generate a joke about {subject} in the following JSON format:\n{format_instructions}\n",
#     input_variables=["subject"],
#     partial_variables={"format_instructions": json_instructions},
# )

response = prompt | llm | json_parser

print(response.invoke({"subject": "dogs", "format_instructions": json_instructions}))
# print(response.invoke({"subject": "dogs"}))

# CommaSeparatedListOutputParser - used to format the output from LLMs in comma separated list structured way.
comma_parser = CommaSeparatedListOutputParser()
comma_instructions = comma_parser.get_format_instructions()

comma_prompt = PromptTemplate.from_template(
    "List five : {subject} \n{format_instructions}\n"
)

comma_response = comma_prompt | llm | comma_parser
print(comma_response.invoke({"subject": "programming languages", "format_instructions": comma_instructions}))


