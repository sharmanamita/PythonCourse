from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

CREDENTIALS = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "project_id": "skills-network",
}

params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100,
}

model = ModelInference(
    model_id="ibm/granite-3-3-8b-instruct",
    params=params,
    credentials=CREDENTIALS,
    project_id="skills-network",
)

text = """
Only reply with the answer. What is the capital of Canada?
"""

print(model.generate(text)["results"][0]["generated_text"])
