# Test version to verify all dependencies work
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv(r'C:\Users\Namita.Saltoo\Workspace\PythonCourse\.env')

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnablePassthrough

print("✓ All imports successful!")
print(f"✓ OpenAI API Key detected: {bool(os.getenv('OPENAI_API_KEY'))}")

location_prompt = """
Your job is to come up with a classic dish from the area that the users suggests. {location}
YOUR RESPONSE:
"""

receipe_prompt = """
Your job is to find receipe of the dish that the user suggests. {dish}
YOUR RESPONSE:
"""

estimated_time_prompt = """
Your job is to find the estimated time to cook the dish that the user suggests. {receipe}
YOUR RESPONSE:
"""

print("\n✓ Creating LLM instance with gpt-4o-mini...")
llm = init_chat_model(model="gpt-4o-mini", model_provider="openai", temperature=0.5)
print("✓ LLM initialized successfully!")

print("\n✓ Building LCEL chains...")
location_chain_LCEL = (
    PromptTemplate.from_template(location_prompt)
    | llm
    | StrOutputParser()
)

receipe_chainLCEL = (
    PromptTemplate.from_template(receipe_prompt)
    | llm
    | StrOutputParser()
)

estimated_time_chainLCEL = (
    PromptTemplate.from_template(estimated_time_prompt)
    | llm
    | StrOutputParser()
)

overall_chain_lcel = (
    RunnablePassthrough.assign(dish=lambda x: location_chain_LCEL.invoke({"location": x["location"]}))
    | RunnablePassthrough.assign(recipe=lambda x: receipe_chainLCEL.invoke({"dish": x["dish"]}))
    | RunnablePassthrough.assign(time=lambda x: estimated_time_chainLCEL.invoke({"receipe": x["recipe"]}))
)

print("✓ All LCEL chains built successfully!")

print("\n" + "="*60)
print("Running chain with location='China'...")
print("This will call OpenAI API (may take 10-30 seconds)")
print("="*60 + "\n")

try:
    result = overall_chain_lcel.invoke({"location": "China"})
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
except KeyboardInterrupt:
    print("\n⚠️ Operation cancelled by user")
except Exception as e:
    print(f"\n❌ Error: {type(e).__name__}: {e}")
