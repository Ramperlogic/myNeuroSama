import ollama
import requests

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
            client = ollama.Client(
                host='http://host.docker.internal:11434',
                headers={'Content-Type': 'application/json'}
            )
            resp = client.chat(
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
    def call_ollama(self):
        user_input = input("You: ")
        host = "host.docker.internal"
        port = "11434"
        url = f"http://{host}:{port}/api/chat"
        model = self.MODEL
        headers = {"Content-Type": "application/json"}
        data = {
            "model": model,  # 模型选择
            "options": {
                "temperature": 0.  # 为0表示不让模型自由发挥，输出结果相对较固定，>0的话，输出的结果会比较放飞自我
            },
            "stream": False,  # 流式输出
            "messages": [{
                "role": "system",
                "content": user_input
            }]  # 对话列表
        }
        response = requests.post(url, json=data, headers=headers, timeout=60)
        res = response.json()
        print(res)