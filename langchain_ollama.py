# langchain_ollama.py
from langchain.llms import Ollama

def make_llm(model_name: str = "llama3", temperature: float = 0.2):
    """Create a LangChain Ollama LLM instance."""
    return Ollama(model=model_name, temperature=temperature)

# Example usage
if __name__ == "__main__":
    llm = make_llm()
    print(llm("Say hello in one sentence."))