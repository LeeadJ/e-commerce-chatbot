import csv

def isOrderStatusRequest(user_input):
    phrases = [
        'order status', 'status of my order', 'where is my order',
        'status of my delivery', 'status of my shipment', 'status of my package',
        'order update', 'order tracking', 'delivery status', 'shipment status', 'package status',
        'happening shipment', 'package on way', 'order dispatch'
    ]
    for phrase in phrases:
        words = phrase.split()
        if all(word in user_input for word in words):
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

