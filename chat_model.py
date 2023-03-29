import openai

class ChatGPT:
    def __init__(self, openai_api_key, model):
        self.open_api_key = openai_api_key
        self.model = model

    def chat(self, messages):
        openai.api_key = self.open_api_key
        response = openai.ChatCompletion.create(
            model = self.model,
            messages = messages
        )
        return response.choices[0].message