

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# PromptTemplate - Module that helps to format prompts with variables.
prompt = PromptTemplate.from_template("Tell me a summary on topic {subject}")

rsp = prompt.invoke({"subject": "UI Developer future"})
print(rsp)

# ChatPromptTemplate - Module that formats list of chat messages with variables.
chatPrompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant." ),
    ("user", "Explain the concept of {topic} in simple terms."),
    ("user", "What are the key skills required for a {position}?")
])

formattedMessages = chatPrompt.invoke({"topic": "langchain", "position": "data scientist"})
print(formattedMessages)

# Placeholder - used to push list of messages into ChatPromptTemplate
placeHolderTemplate = ChatPromptTemplate([
    ("system", "You are a helpful assistant." ),
    ("user", "{msgs}")
])

formattedMsgs = placeHolderTemplate.invoke({
    "msgs": [
        "Explain the concept of transformers in simple terms.",
        "What are the key skills required for a machine learning engineer?"
    ]
})

print(formattedMsgs.to_messages())
