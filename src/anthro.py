import os
import anthropic
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Anthropic client with the API key
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class AnthroAssistant:
    def anthro_ass(self, model: str, sys_data: str, user_data: str) -> str:
        # Set token limits based on the model
        if model == "claude-3-5-sonnet-20240620":
            tokens = 8192
        else:
            tokens = 4096
        
        # Create a message request
        try:
            message = client.messages.create(
                model=model,
                max_tokens=tokens,
                system=sys_data,
                messages=[{"role": "user", "content": user_data}]
            )
            
            # Extract and return the response content
            anthro_response = message.content[0].text
            return anthro_response
        except anthropic.APIError as e:
            return("The API key which your provided is not correct one. Please check and update new and valid API key.")
        except Exception as e:
            return f"An error occurred: {str(e)}"
