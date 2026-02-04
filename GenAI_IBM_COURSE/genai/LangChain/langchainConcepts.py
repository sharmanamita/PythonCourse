
from langchain.chat_models import init_chat_model
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
import os

llm = init_chat_model("openai:gpt-5", temperature=0.5)
model = ModelInference(
    model_id="gpt-5",
    params={
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5,},
    credentials={
        "apikey": os.getenv("OPENAI_API_KEY"),
    }
)


# response = llm.invoke("In today's sales meeting, we")
response = llm.invoke("Who is man's best friend?")
print(response.content)

# IBM's Watsonx LLM via LangChain
# watsonllm = WatsonxLLM(model=model)
# rsp = watsonllm.invoke("Tell me a funny joke about programmers.")
# print(rsp.content)