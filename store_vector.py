from src.helper import load_pdf_file, split_text_data, download_hugging_face_embeddings
import chromadb
from langchain_chroma import Chroma

extracted_data = load_pdf_file(data='data/')
text_chunks = split_text_data(extracted_data)
embeddings = download_hugging_face_embeddings()

chroma_client = chromadb.PersistentClient(path="./chroma_db")
vector_store = Chroma.from_documents(text_chunks, embeddings, persist_directory="./chroma_db")
vector_store.persist()
