import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3.5:9b"

# Sample product catalog
PRODUCTS = {
    "laptop": {
        "price": 3500.00,
        "stock": 15
    },
    "monitor": {
        "price": 850.00,
        "stock": 30
    },
    "keyboard": {
        "price": 120.00,
        "stock": 8
    }
}


def get_product_information(question):
    """Retrieve information from the sample catalog."""

    question = question.lower()

    if "price" not in question and "stock" not in question:
        return None

    for name, product in PRODUCTS.items():

        if name in question:

            if "stock" in question:
                return (
                    f"{name.title()} stock: "
                    f"{product['stock']} units"
                )

            return (
                f"{name.title()} price: "
                f"RM{product['price']:.2f}"
            )

    if "price of" in question or "stock of" in question:
        return "Product not found in the sample catalog."

    return None


def ask_ollama(question):
    """Send a question to the local Ollama model."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful Python learning assistant. "
                "Give clear, concise answers. "
                "Do not invent business product information."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 200
        }
    }

    request_data = json.dumps(payload).encode("utf-8")

    request = Request(
        OLLAMA_URL,
        data=request_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urlopen(request, timeout=600) as response:
        result = json.load(response)

    return result["message"]["content"].strip()


def main():

    print("======================================")
    print("       PYTHON AI AGENT DEMO")
    print("       Visual Studio 2026")
    print("       Ollama + Qwen 3.5")
    print("======================================")

    print("Ask a general question or product question.")
    print("Type 'exit' to close the program.")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        # First check whether a local tool can answer.
        product_answer = get_product_information(
            question
        )

        if product_answer is not None:

            print("\n[Local Python Tool]")
            print("Assistant:", product_answer)
            continue

        # Otherwise ask the language model.
        print("\nAsking Qwen 3.5...")

        try:
            answer = ask_ollama(question)

            if answer:
                print("\nAssistant:", answer)
            else:
                print("The model returned an empty response.")

        except HTTPError as ex:
            print(
                f"Ollama returned HTTP error {ex.code}. "
                "Check the model name and server."
            )

        except (URLError, TimeoutError) as ex:
            print("Cannot reach Ollama:", ex)

        except (KeyError, ValueError) as ex:
            print("Unexpected AI response:", ex)


if __name__ == "__main__":
    main()
