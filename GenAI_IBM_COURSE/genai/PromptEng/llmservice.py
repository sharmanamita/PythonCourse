from openai import OpenAI

Test_Key = "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"
client = OpenAI(api_key=Test_Key)

def llm_model(prompt, model="gpt-4.1"):
    response = client.responses.create(
        model=model,
        input=prompt
    )
    return response.output_text