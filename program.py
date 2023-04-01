import openai
import gradio

openai.api_key = "###"

messages = []

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    print(f'you: {user_input}\n')
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    print(f'assistant: {ChatGPT_reply}\n')
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "textbox", outputs = "textbox", title = "Vithu's GPT")

demo.launch(share=False)