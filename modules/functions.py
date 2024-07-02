import csv
from textblob import TextBlob

def correct_spelling(user_input):
    corrected_input = str(TextBlob(user_input).correct())
    return corrected_input

def isOrderStatus(user_input):
    if any(all(word in user_input.lower() for word in phrase.split()) for phrase in [
        'order status', 'status of my order', 'where is my order',
        'status of my delivery', 'status of my shipment', 'status of my package',
        'order update', 'order tracking', 'delivery status', 'shipment status', 'package status',
        'happening shipment', 'package on way', 'order dispatch'
    ]):
        return True
    return False


def get_order_status(order_id):
    while order_id != "exit":
        with open('data/order_info.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['order_id'] == order_id:
                    return f"Order status for {order_id}: {row['status']}"
        order_id = input("Order ID not found. Please enter new order ID or type exit and click enter: ")
    return "Exited order status."

def save_contact_info(name, email, phone):
    with open('data/contact_info.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])
    return "Your contact information has been saved. A representative will contact you shortly."

def get_return_policy_info(question):
    responses = {
        "What is the return policy for items purchased at our store?": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.",
        "Are there any items that cannot be returned under this policy?": "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.",
        "How will I receive my refund?": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card."
    }
    normalized_question = question.strip().lower()
    return responses.get(normalized_question, "Sorry, I don't have information on that.")