def isReturnPolicyRequest(user_input):
    phrases = [
        'return policy', 'what is the return policy', 'items return policy',
        'returning items', 'refund policy', 'exchange policy', 'policy on returns'
    ]
    for phrase in phrases:
        words = phrase.split()
        if all(word in user_input for word in words):
            print("Chatbot: What would you like to know about the return policy?")
            return True
    return False

def get_return_policy_info(user_input):
    return_policy_trigger = [
        "what is the return policy",
        "what is the return policy on items",
        "what is your return policy for items purchased?",
        "return policy for items bought from your store?",
        "can I return items I purchased?",
        "what's your policy on returns?",
    ]
    non_returnable_trigger = [
        "what items cannot be returned?",
        "non-returnable items policy?",
        "items that can't be returned?",
        "exceptions to your return policy?",
    ]
    refund_process_trigger = [
        "what is the refund policy",
        "how do I get my refund?",
        "refund process details?",
        "receiving my refund?",
        "how are refunds processed?",
    ]
    if any(word in user_input for word in return_policy_trigger):
        return "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items."

    elif any(word in user_input for word in non_returnable_trigger):
        return "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.",

    elif any(word in user_input for word in refund_process_trigger):
        return "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card."
    # user_input = user_input.strip().lower()
    # keywords = ['']
    # for query, response in responses.items():
    #     if all(word in question for word in query.split()):
    #         return response
    return "Sorry, I don't have information on that."