
from langchain_openai import ChatOpenAI
from langchain_core.messages import ChatMessage

chat = ChatOpenAI(model_name="gpt-4o", temperature=0)

history = ChatMessage()
history.add_ai_message("Hello! How can I assist you today?")
history.add_human_message("Can you tell me a joke?")

