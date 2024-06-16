import requests

API_KEY = '3d9c1375ba0643a79399c16c8a09aa'
API_ENDPOINT = 'https://api.llama3.com/v1/chat'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def chat_with_llama3(user_input):
    data = {
        'input': user_input,
        'model': 'llama-3'
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get('response', 'No response from Llama-3.')
    else:
        return f'Error: {response.status_code}, {response.text}'

def main():
    print("Start chatting with Llama-3 (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        llama_response = chat_with_llama3(user_input)
        print(f"Llama-3: {llama_response}")

if __name__ == "__main__":
    main()
