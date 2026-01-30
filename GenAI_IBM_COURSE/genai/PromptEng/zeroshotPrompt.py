from llmservice import llm_model

prompt = """Classify the following statement as true or false: 
            'The Eiffel Tower is located in Berlin.'

            Answer:
"""
llm_model(prompt)

#Ecercise additional prompts
# 1. Prompt for Movie Review Classification
# "Write a prompt that asks the model to classify a movie review as positive or negative."
movie_review_prompt = "Give me review of movie Dhurandhar, and classify it as positive or negative."

# 2. Prompt for Climate Change Paragraph Summarization
# "Create a prompt that instructs the model to summarize a paragraph about climate change."
climate_change_prompt = "Write a paragraph about climate change and summarize it in one sentence."

# 3. Prompt for English to Spanish Translation
# "Design a prompt that asks the model to translate an English phrase to Spanish without showing any examples."
translation_prompt = "Translate the following English phrase to Spanish: 'Good morning, how are you?'"

response = {}
response['movie_review'] = llm_model(movie_review_prompt)
response['climate_change'] = llm_model(climate_change_prompt)
response['translation'] = llm_model(translation_prompt)

for item in response:
    print(response[item], "\n")
