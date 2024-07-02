import os
from modules.functions import get_order_status, save_contact_info, get_return_policy_info
from modules.config import get_gpt_response

def main():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        if 'order status' in user_input.lower():
            order_id = input("Please provide your order ID: ")
            print("Bot:", get_order_status(order_id))
        elif 'human representative' in user_input.lower():
            name = input("Please provide your full name: ")
            email = input("Please provide your email: ")
            phone = input("Please provide your phone number: ")
            print("Bot:", save_contact_info(name, email, phone))
        elif 'return policy' in user_input.lower():
            print("Bot:", get_return_policy_info(user_input))
        else:
            response = get_gpt_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
