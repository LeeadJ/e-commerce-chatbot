import os
from modules.order_status import isOrderStatusRequest, get_order_status
from modules.config import get_gpt_response
from modules.human_rep import isHumanRepresentativeRequest, request_human_representative_info, save_contact_info
from modules.return_policy import isReturnPolicyRequest, get_return_policy_info
from textblob import TextBlob

def correct_spelling(user_input):
    corrected_input = str(TextBlob(user_input).correct())
    return corrected_input

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
            print("Chatbot:", get_order_status(order_id))

        # Request Human rep:
        elif isHumanRepresentativeRequest(user_input):
            name, email, phone = request_human_representative_info()
            if name is None and email is None and phone is None:
                print("Chatbot: Exit successful. No contact information was saved.")
            else:
                print("Chatbot:", save_contact_info(name, email, phone))

        # Return Policy:
        elif isReturnPolicyRequest(user_input):
            user_input = input("You: ")
            print("Chatbot:", get_return_policy_info(user_input))

        # Auto chat response:
        else:
            print(f"Chatbot: {get_gpt_response(user_input)}")

if __name__ == "__main__":
    main()
