from src.helper import download_hugging_face_embeddings
import chromadb
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import system_prompt
from langchain_chroma import Chroma
from langchain_ollama.llms import OllamaLLM

def process_query(input):
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
    return rag_chain.invoke({"input": input})