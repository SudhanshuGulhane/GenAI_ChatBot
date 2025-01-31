from flask import Flask, render_template, jsonify, request

from src.helper import download_hugging_face_embeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import system_prompt
import chromadb
from langchain_chroma import Chroma
from langchain_ollama.llms import OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

embeddings = download_hugging_face_embeddings()
chroma_client = chromadb.PersistentClient(path="./chroma_db")
retriever = Chroma(persist_directory="./chroma_db", embedding_function=embeddings).as_retriever()
llm = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)
qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chatbot():
    input = request.form["msg"]
    response = rag_chain.invoke({"input": input})
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)