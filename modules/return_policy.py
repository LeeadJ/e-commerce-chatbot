def isReturnPolicyRequest(user_input):
    phrases = [
        'return policy', 'what is the return policy', 'items return policy',
        'returning items', 'refund policy', 'exchange policy', 'policy on returns'
    ]
    for phrase in phrases:
        words = phrase.split()
        if all(word in user_input for word in words):
            return True
    return False

def get_return_policy_info(question):
    responses = {
        "What is the return policy for items purchased at our store?": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.",
        "Are there any items that cannot be returned under this policy?": "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.",
        "How will I receive my refund?": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card."
    }
    question = question.strip().lower()
    for query, response in responses.items():
        if all(word in question for word in query.split()):
            return response
    return "Sorry, I don't have information on that."