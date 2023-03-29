class Agent:
    def __init__(self, chatbot, tools):
        self.chatbot = chatbot
        self.tools = tools

    def do(self, task):
        tool_detail = "\n".join([f"{tool.name} - {tool.description}" for tool in self.tools])

        self.chatbot.speak(task)
        self.chatbot.speak(f"You have a suite of tools to help you. They are:\n{tool_detail}")
        self.chatbot.speak("What tool do you want to use, if any? If you want to use a tool, respond only with the tool name or None. Do not respond with any other text.")
        chosen_tool_name = self.chatbot.respond()
        chosen_tool_name = chosen_tool_name[:-1] if chosen_tool_name[-1] == "." else chosen_tool_name 
        print(chosen_tool_name)
        chosen_tool = [tool for tool in self.tools if tool.name == chosen_tool_name][0]

        if chosen_tool:
            self.chatbot.speak(f"What input do you want to give {chosen_tool.name}? Give only the input.")
            inp = self.chatbot.respond()
            print(inp)
            output = chosen_tool.use(inp)
