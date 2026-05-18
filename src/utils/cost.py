def calculate_cost(model_name: str, input_tokens: int, output_tokens: int) -> float:
    """
    Calculates the estimated cost based on Google AI Studio pricing (May 2026).
    """
    # Approximate pricing per 1M tokens
    pricing = {
        "gemini-3.1-flash-lite": {"input": 0.075 / 1_000_000, "output": 0.30 / 1_000_000},
        "gemini-2.5-pro": {"input": 1.25 / 1_000_000, "output": 5.00 / 1_000_000},
        "gemini-2.5-flash": {"input": 0.10 / 1_000_000, "output": 0.40 / 1_000_000},
    }
    
    # Fallback logic
    if model_name in pricing:
        costs = pricing[model_name]
    elif "pro" in model_name.lower():
        costs = pricing["gemini-2.5-pro"]
    else:
        costs = pricing["gemini-3.1-flash-lite"]
        
    return (input_tokens * costs["input"]) + (output_tokens * costs["output"])
