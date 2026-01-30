from llmservice import llm_model

prompt = """When I was 6, my sister was half of my age. Now I am 70, what age is my sister?

            Provide three independent calculations and explanations, then determine the most consistent result.

"""
response = llm_model(prompt)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")