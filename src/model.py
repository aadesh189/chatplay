class ModelsChoice:
    def selected_model(self, model: str) -> tuple:
        # Dictionary mapping models to their prices
        model_price = {
            "gpt-4o": 0.0000025,
            "gpt-4o-completion": 0.000010,
            "gpt-4o-mini": 0.00000015,
            "gpt-4o-mini-completion": 0.0000006,
            "gpt-4": 0.00003,
            "gpt-4-completion": 0.00006,
            "gpt-4-turbo": 0.00001,
            "gpt-4-turbo-completion": 0.00003,
            "gpt-3.5-turbo": 0.000003,
            "gpt-3.5-turbo-completion": 0.000008,
            "claude-3-5-sonnet-20240620": 0.000003,
            "claude-3-5-sonnet-20240620-completion": 0.000015,
            "claude-3-opus-20240229": 0.000015,
            "claude-3-opus-20240229-completion": 0.000075,
            "claude-3-sonnet-20240229": 0.000003,
            "claude-3-sonnet-20240229-completion": 0.000015,
            "claude-3-haiku-20240307": 0.00000025,
            "claude-3-haiku-20240307-completion": 0.00000125,
            "o1-preview":0.000015,
            "o1-preview-completion":0.00006,
            "o1-mini":0.000003,
            "o1-mini-completion":0.000012
        }

        # Check if the model exists in the price dictionary
        if model in model_price:
            price = model_price[model]
            completion_key = f"{model}-completion"
            
            # Get the completion price
            price_completion = model_price.get(completion_key, 0.0)

            # Format prices
            formatted_price = format(price, '.10f')
            formatted_price_completion = format(price_completion, '.10f')

            # Print formatted prices for debugging
            print(formatted_price)
            print(formatted_price_completion)

            return float(formatted_price), float(formatted_price_completion)

        # Return None if the model is not found
        print("Model not found.")
        return None, None
