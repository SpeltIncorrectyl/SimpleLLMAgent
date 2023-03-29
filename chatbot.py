class Chatbot:
    def __init__(self, chat, primer):
        self.chat = chat
        self.primer = primer
        self.messages = []
        self.wipe()

    def wipe(self):
        self.messages = [{"role" : "system", "content" : self.primer}]

    def speak(self, message):
        self.messages.append({"role" : "user", "content" : message})

    def mimic(self, message):
        self.messages.append({"role" : "assistant", "content" : message})

    def respond(self):
        response = self.chat.chat(self.messages)
        self.messages.append(response)
        return response.content