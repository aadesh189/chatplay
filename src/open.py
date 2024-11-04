import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIAssistant:
    def openai_ass(self, model: str, sys_data: str, user_data: str) -> str:
        # Set token limits based on the model
        if model in ['gpt-4o', 'gpt-4o-mini']:
            tokens = 16384
        elif model == 'o1-preview':
            tokens = 32768
        elif model == 'o1-mini':
            tokens = 65536
        elif model == 'gpt-4':
            tokens = 8192
        else:
            tokens = 4096

        # Create a chat completion request
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=tokens,
                messages=[
                    {"role": "system", "content": sys_data},
                    {"role": "user", "content": user_data}
                ]
            )
            
            # Extract and return the response content
            openai_response = response.choices[0].message.content
            return openai_response
        except openai.APIError as e:
            return("The API key which your provided is not correct one. Please check and update new and valid API key.")
        except openai.error.InvalidRequestError as e:
            return "Invalid request: " + str(e)
        except openai.error.AuthenticationError as e:
            return "Authentication error: " + str(e)

