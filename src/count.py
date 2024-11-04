import tiktoken

class TokenCounter:
    def num_tokens_from_string(self, *args: str) -> int:
        """Returns the total number of tokens in the provided text strings."""
        encoding = tiktoken.get_encoding("o200k_base")
        total_tokens = 0

        for string in args:
            total_tokens += len(encoding.encode(string))

        return total_tokens

    def cost_of_input_tokens(self, total_tokens: int, price_per_token: float) -> float:
        """Calculates the cost of input tokens based on the number of tokens and the price per token."""
        input_cost = total_tokens * price_per_token
        return input_cost

    def cost_of_output_tokens(self, total_tokens: int, price_per_token: float) -> float:
        """Calculates the cost of output tokens based on the number of tokens and the price per token."""
        output_cost = total_tokens * price_per_token
        return output_cost
