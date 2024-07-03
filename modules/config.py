from openai import OpenAI
import os

# Ensure the API key is set
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(
    api_key='sk-llm-assignment-LawnoYcOdErwiPCn5vTzT3BlbkFJQ40jiNAQT8CrSabMdBjs',
)

def get_gpt_response(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful assistant for an e-commerce platform. Recognize requests for order status, return policies, and human representative requests."},
        {"role": "user", "content": "What is the return policy for items purchased at your store?"},
        {"role": "assistant", "content": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items."},
        {"role": "user", "content": "Are there any items that cannot be returned under this policy?"},
        {"role": "assistant", "content": "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details."},
        {"role": "user", "content": "How will I receive my refund?"},
        {"role": "assistant", "content": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund."},
        {"role": "user", "content": "Can you check the status of my recent order?"},
        {"role": "assistant", "content": "Sure, could you please provide me with your order ID?"},
        {"role": "system", "content": "Recognize user requests for human representative assistance, such as 'talk to a human', 'customer service', 'real person', etc."},
        {"role": "user", "content": "I need to speak to a customer service representative."},
        {"role": "assistant", "content": "Sure, I can connect you with a human representative. Please provide your full name, email, and phone number."},
        {"role": "user", "content": "My order ID is 12345."},
        {"role": "assistant", "content": "Let me check that for you..."},
        {"role": "system", "content": "System is processing order status request..."},
        {"role": "assistant", "content": "Your order with ID 12345 is currently out for delivery and expected to arrive by [date/time]."},
        {"role": "user", "content": "Thank you!"},
        {"role": "assistant", "content": "You're welcome! Is there anything else I can assist you with?"},
    ]

    response = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo-0125"
    )
    return response.choices[0].message.content


