from llm import *

def run():
    print("Chat with AI model started")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Bye!")
            break

        response = send_message(user_input)
        print(f"\nBot: {response}\n")