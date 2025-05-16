import requests


def call_llm(system_prompt: str, user_message: str, model: str = "llama-3.2-1b-instruct", temperature: float = 0.1):
    """
    Call the local LLM server with the given prompts.
    
    Args:
        system_prompt: The system prompt to set context for the LLM
        user_message: The user's message/query
        model: The model to use for generation
        temperature: Controls randomness (higher = more random)
        
    Returns:
        The LLM's response text
    """
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": temperature,
        "max_tokens": -1,
        "stream": False
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    
    result = response.json()
    return result["choices"][0]["message"]["content"]


if __name__ == '__main__':
    print(call_llm("you are helpful", "What color is the sky?"))
