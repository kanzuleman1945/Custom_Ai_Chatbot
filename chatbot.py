import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Conversation memory
conversation_history = []

print("=================================")
print("      CUSTOM AI CHATBOT")
print("=================================")
print("Type 'exit' to quit.")
print()

while True:

    # Get user input
    user_input = input("You: ")

    # Exit command
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    # Add user's message to memory
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation history to the AI
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation_history
    )

    # Get AI response
    ai_response = response.choices[0].message.content

    # Add AI response to memory
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display AI response
    print("AI:", ai_response)
    print()