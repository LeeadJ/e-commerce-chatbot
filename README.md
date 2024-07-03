# E-commerce Chatbot

## Project Overview

This project implements a conversational agent (chatbot) using the OpenAI API to handle customer support queries for an e-commerce platform. 
The chatbot can respond to inquiries about order status, return policies, and also connect users with human representatives.

### Project Structure
e-commerce-chatbot/<br>
├── main.py<br>
├── data/<br>
│ ├── contact_info.csv<br>
│ └── order_info.csv<br>
└── modules/<br>
├── config.py<br>
├── human_rep.py<br>
├── order_status.py<br>
└── return_policy.py<br>


- **main.py:** Main script to run the chatbot and handle user interactions.
- **data/:** Directory for storing CSV files (`contact_info.csv`, `order_info.csv`) used for storing contact and order information.
- **modules/:** Directory containing various Python modules for different aspects of the chatbot.

### Functionalities

1. **Order Status:** Provides information about the status of an order based on the provided order ID.
2. **Human Representative Request:** Allows users to request to speak to a human representative and collects their contact information (name, email, phone).
3. **Return Policies:** Provides information about return policies including what items can be returned, what items cannot be returned, and how refunds are processed.
4. **OpenAI Integration:** Uses the OpenAI API to handle general conversation responses when specific functionalities are not triggered.

## Setup and Dependencies

### Environment Setup

1. **Python Installation:**
   - Ensure Python 3.x is installed on your system.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/LeeadJ/e-commerce-chatbot
   cd e-commerce-chatbot
   ```
3. **Install Dependencies:**
   ```bash
   pip install openai
   pip install textblob
   ```
   
## Running the Chatbot
Run the main.py script in the terminal to start the chatbot:
   ```bash
   python main.py
   ```
## Testing the Agent

1. Order Status:
   - Type "What is the status of my order?" or "Check order status".
   - Provide a valid order ID when prompted. (check ID example in order_status.csv)


2. Human Representative Request:
   - Type phrases like "I want to talk to a human" or "Speak to customer service".
   - Enter valid contact information when prompted.
   

3. Return Policies:
   - Type "What is your return policy?" or "Can I return items?".


4. General Conversation:
   - The user can have typical conversation to see how the chatbot responds when not triggered by specific functionalities.

5. Example Dialogue:
![Screenshot 2024-07-03 at 16 04 57](https://github.com/LeeadJ/e-commerce-chatbot/assets/77110578/2f5aca8a-f1fc-42e4-8676-babfa07c3d16)
