from config import ai_client
from config import model

def send_message(message: str):
    if message == '' or message is None:
        return "Message cannot be empty"
    try:
        response = ai_client.chat.send(
            model = model,
            messages = [
                {"role": "user", "content": message}
            ],
        )
        return response.choices.pop().message.content
    except Exception as e:
        return f"Error sending message: {e}"