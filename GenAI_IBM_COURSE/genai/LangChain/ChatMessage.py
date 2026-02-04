from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


llm = init_chat_model("openai:gpt-5", temperature=0.5)
msg = llm.invoke([
    SystemMessage(content="You are a helpful AI bot that assists a user in choosing the perfect book to read in one short sentence"),
    HumanMessage(content="I enjoy mystery novels, what should I read?"),
    AIMessage(content="You should try a CrossFit class"),
    HumanMessage(content="How often should I attend?"),
])
print(msg.content)