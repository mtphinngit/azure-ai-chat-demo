import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Load environment variables
        load_dotenv()

        # Initialize Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01"
        )

        # Start loop for user input
        while True:
            # Get input prompt
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                print("Exiting the chat. Goodbye!")
                break
            if len(input_text.strip()) == 0:
                print("Please enter a valid prompt.")
                continue

            # Get response from Azure OpenAI
            response = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": input_text}
                ]
            )

            # Display the assistant’s reply
            print("\nResponse:\n" + response.choices[0].message.content + "\n")

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    main()
