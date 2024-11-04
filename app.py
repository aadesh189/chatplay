from flask import Flask, jsonify, request
from flask_cors import CORS
from src.count import TokenCounter
from src.model import ModelsChoice
from src.open import OpenAIAssistant
from src.anthro import AnthroAssistant

app = Flask(__name__)
CORS(app)

@app.route('/prmpt', methods=['POST'])
def display_sys_prompt():
    data = request.json
    sys_data = data.get('system', '')
    user_data = data.get('user', '')
    model = data.get('choicemodel', '')

    # Log the received data for debugging
    print(sys_data)
    print(user_data)
    print(model)

    model_choice = ModelsChoice()
    price_tuple = model_choice.selected_model(model)
    print(f"Model Price: {price_tuple[0]:.8f}, Completion Price: {price_tuple[1]:.8f}")

    number_token = TokenCounter()
    input_token = number_token.num_tokens_from_string(sys_data, user_data)
    input_cost = number_token.cost_of_input_tokens(input_token, price_tuple[0])

    if model in ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo","o1-mini","o1-preview"]:
        openai_assistant_instance = OpenAIAssistant()
        openai_response = openai_assistant_instance.openai_ass(model, sys_data=sys_data, user_data=user_data)
        print(openai_response)
        
        output_token = number_token.num_tokens_from_string(openai_response)
        output_cost = number_token.cost_of_output_tokens(output_token, price_tuple[1])
        total_tokens = input_token + output_token
        total_cost = input_cost + output_cost
        
        print("Number of tokens: ", total_tokens)
        print("Cost of tokens: ", total_cost)
        
        return jsonify({"sysdata": openai_response, "token": total_tokens, "cost": total_cost})
    
    else:
        anthro_assistant_instance = AnthroAssistant()
        anthro_response = anthro_assistant_instance.anthro_ass(model, sys_data=sys_data, user_data=user_data)
        print(anthro_response)
        
        output_token = number_token.num_tokens_from_string(anthro_response)
        output_cost = number_token.cost_of_output_tokens(output_token, price_tuple[1])
        total_tokens = input_token + output_token
        total_cost = input_cost + output_cost
        
        print("Number of tokens: ", total_tokens)
        print("Cost of tokens: ", total_cost)
        
        return jsonify({"sysdata": anthro_response, "token": total_tokens, "cost": total_cost})

if __name__ == '__main__':
    app.run(debug=True)
