import os
from modules.functions import correct_spelling, isOrderStatusRequest, get_order_status, save_contact_info
from modules.config import get_gpt_response
from modules.human_rep import isHumanRepresentativeRequest, request_human_representative_info
from modules.return_policy import isReturnPolicyRequest, get_return_policy_info

def main():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break

        user_input = correct_spelling(user_input).lower()

        # Order status:
        if isOrderStatusRequest(user_input):
            order_id = input("Please provide your order ID: ")
            print("Bot:", get_order_status(order_id))

        # Request Human rep:
        elif isHumanRepresentativeRequest(user_input):
            name, email, phone = request_human_representative_info()
            if name is None and email is None and phone is None:
                print("Bot: Exit successful. No contact information was saved.")
            else:
                print("Bot:", save_contact_info(name, email, phone))

        # Return Policy:
        elif isReturnPolicyRequest(user_input):
            print("Bot:", get_return_policy_info(user_input))

        # Auto chat response:
        else:
            print(f"Chatbot: {get_gpt_response(user_input)}")

if __name__ == "__main__":
    main()
