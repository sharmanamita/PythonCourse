from llmservice import llm_model

prompt = """Consider the problem: 'A store had 22 apples. 
            They sold 15 apples today and got a new delivery of 8 apples. 
            How many apples are there now?’

            Break down each step of your calculation

"""
response = llm_model(prompt)

print(response)

# Excercise additional prompts
# 1. Write a prompt that asks the model to think through whether a student should study tonight or go to a movie with friends, considering their upcoming test in two days.
# 2. Write a prompt that instructs the model to explain the step-by-step process of making a peanut butter and jelly sandwich.

decisionPrompt = """Consider the situation: A student has a test in two days. 
They can either study tonight or go to a movie with friends.
Break down the factors they should consider in making this decision."""

sandwichPrompt = """Explain the step-by-step process of making a peanut butter and jelly sandwich."""

response = {
    'decision': llm_model(decisionPrompt),
    'sandwich': llm_model(sandwichPrompt)
}

print("Decision Making Process:\n", response['decision'], "\n")
print("Peanut Butter and Jelly Sandwich Process:\n", response['sandwich'], "\n")
