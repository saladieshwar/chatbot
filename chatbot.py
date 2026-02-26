import requests
import json

# =========================
# CONFIG
# =========================
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"   # change if you use mistral, phi, etc.


# =========================
# CHAT FUNCTION
# =========================
def chat_with_ollama(messages):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": True
        },
        stream=True
    )

    full_reply = ""

    for line in response.iter_lines():
        if line:
            decoded_line = json.loads(line.decode("utf-8"))
            content = decoded_line.get("message", {}).get("content", "")
            print(content, end="", flush=True)
            full_reply += content

    print()
    return full_reply


# =========================
# MAIN LOOP
# =========================
def main():
    print("🤖 Ollama Chatbot (type 'exit' to quit)\n")

    messages = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        print("Bot: ", end="")
        reply = chat_with_ollama(messages)

        messages.append({
            "role": "assistant",
            "content": reply
        })


if __name__ == "__main__":
    main()