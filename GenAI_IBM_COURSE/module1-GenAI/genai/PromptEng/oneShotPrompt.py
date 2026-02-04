from llmservice import llm_model

prompt = """Here is an example of translating a sentence from English to French:

            English: “How is the weather today?”
            French: “Comment est le temps aujourd'hui?”
            
            Now, translate the following sentence from English to French:
            
            English: “Where is the nearest supermarket?”
            
"""
response = llm_model(prompt)
print(response)

# Excercise additional prompts
# 1. Create a prompt with one example of a formal email, then ask the model to write another formal email on a different topic.
# 2. Provide one example of converting a technical concept into a simple explanation, then ask the model to explain a different concept.
# 3. Give one example of extracting keywords from a sentence, then ask the model to extract keywords from a new sentence.

emailPrompt = """" Here is an example of formal email:
    subject: request for meeting

    Dear Me.Smith,
    I hope this email finds you well. I am writing to request a meeting to discuss our upcoming project. Please let me know your availability next week.
    Best regards,
    John Doe

    Now, write a formal email on the topic of requesting feedback on a report.
  """""

techPrompt = """
    Here is an example of converting a technical concept into a simple explanation:
    Technical Concept: Blockchain
    Simple Explanation: A blockchain is like a digital ledger that records transactions across many computers so that the record cannot be changed retroactively. It’s like a shared notebook that everyone can see and verify, making it very secure.
    Now, explain the concept of "Quantum Computing" in simple terms.
"""

keywordPrompt = """
    Here is an example of extracting keywords from a sentence:
    Sentence: "Artificial intelligence is transforming the way we live and work."
    Keywords: artificial intelligence, transforming, live, work
    Now, extract keywords from the following sentence:
    Sentence: "Renewable energy sources are essential for a sustainable future."
 """

response = {
    'email': llm_model(emailPrompt),
    'techQ': llm_model(techPrompt),
    'keyword': llm_model(keywordPrompt)
}

for item in response:
    print(response[item], "\n")