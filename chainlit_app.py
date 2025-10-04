# chainlit_app.py
import chainlit as cl
from langchain.llms import Ollama

# Simple Chainlit handler that proxies user input to Ollama via LangChain
@cl.on_message
async def main(message: cl.Message):
    # instantiate LLM (lightweight, local model name)
    llm = Ollama(model="llama3")

    # call LLM synchronously via LangChain LLM wrapper
    resp = llm(message.content)

    await cl.Message(content=str(resp)).send()