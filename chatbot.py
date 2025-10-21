import openai
import os

# Quick chatbot demo with OpenAI API
# Install: pip install openai

class SimpleChatbot:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('OPENAI_API_KEY')
        if self.api_key:
            openai.api_key = self.api_key
    
    def chat(self, message, system_prompt="You are a helpful assistant."):
        """Send a message to the chatbot and get a response"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}. Please set your OPENAI_API_KEY."
    
    def run_demo(self):
        print("Simple Chatbot Demo - Ready in under 2 mins!")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            
            response = self.chat(user_input)
            print(f"Bot: {response}\n")

if __name__ == '__main__':
    bot = SimpleChatbot()
    bot.run_demo()
