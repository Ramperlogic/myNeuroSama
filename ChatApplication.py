import ollama


class ChatApplication:
    def __init__(self, debug_mod, model):
        self.DEBUG_MOD = debug_mod
        self.MODEL = model
        pass

    def run(self):
        print("-------------------- started --------------------")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("-------------------- ending --------------------")
                break
            resp = ollama.chat(
                model=self.MODEL,
                messages=[
                    {'role': 'user', 'context': user_input}
                ],
                keep_alive="-1h"
            )
            if resp:
                try:
                    content = resp.get("message").get('content')
                    output_str = content.split('</think>')[1]
                    output_str = output_str.strip()
                except:
                    output_str = "error"
                print(f"Ai: {output_str}")
                if self.DEBUG_MOD:
                    print(f"Ai: {resp}")
            else:
                print("error no resp")
