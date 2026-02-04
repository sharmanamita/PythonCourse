from model import llama3_response, granite_response, mixtral_response


def test_all_models(system, user):
    llama_rsp = llama3_response(system_prompt=system, user_prompt=user)
    granite_rsp = granite_response(system_prompt=system, user_prompt=user)
    mixtral_rsp = mixtral_response(system_prompt=system, user_prompt=user)

    print("Llama3 Response:\n", llama_rsp.content)
    print("\nGranite Response:\n", granite_rsp.content)
    print("\nMixtral Response:\n", mixtral_rsp.content)


# Example call to test all models

test_all_models(
    "You are a helpful assistant who provides concise and accurate answers",
    "What is the capital of Canada? Tell me a cool fact about it as well",
)
