# GenAI ChatBot

## Overview
GenAI ChatBot is an AI-powered chatbot designed to interact with users by leveraging natural language processing and vector-based retrieval. This project utilizes **ChromaDB** for vector storage and retrieval, making it efficient for answering questions based on the provided dataset.

## Features
- **Vector-Based Search**: Uses **ChromaDB** for efficient data retrieval.
- **Document Processing**: Reads and processes PDF documents for knowledge extraction.
- **Interactive Chat Interface**: Provides a user-friendly web-based UI for chatbot interactions.
- **LLM Integration**: Uses a generative AI model to enhance responses.
- **Flask-Based Backend**: The server is powered by Flask, making it easy to deploy and extend.

## Evaluation Metrics

Evaluated the chatbot’s performance using two key metrics on several queries. For one representative query, the results were as follows:

**Rouge-L F-measure:**
- **Standard LLM:** 0.17
- **BM25_llm_answer:** 0.25 (+47% improvement over Standard LLM)
- **LLM with RAG Chain:** 0.318 (+87% improvement over Standard LLM)

**Sentence Transformer Cosine Similarity:**
- **Standard LLM:** 0.78
- **BM25_llm_answer:** 0.55 (29% lower than Standard LLM)
- **LLM with RAG Chain:** 0.9 (+15% improvement over Standard LLM)

> *These enhancements were achieved by integrating **LLaMA** for language generation, **LangChain** for orchestration, and **Chroma** as the vector store to index a 4,000-page medical PDF knowledge base for retrieval-augmented generation.

## Project Structure
```
GenAI_ChatBot/
│── chroma_db/             # Vector database storage
│   ├── chroma.sqlite3     # ChromaDB database file
│── data/                  # Source documents
│   ├── medical_book.pdf   # Knowledge source for chatbot
│── src/                   # Source code
│   ├── __init__.py
│   ├── helper.py          # Utility functions
│   ├── prompt.py          # Handles chatbot prompts
│── static/                # Static files (CSS, JS, etc.)
│   ├── style.css          # Stylesheet for UI
│── templates/             # HTML templates
│   ├── index.html         # Web interface for chatbot
│── testing/               # Testing scripts and notebooks
│   ├── trials.ipynb       # Jupyter notebook for testing
│── app.py                 # Main application entry point
│── store_vector.py        # Stores processed data as vectors
│── requirements.txt       # Python dependencies
│── setup.py               # Project setup script
│── LICENSE                # Project licensing information
│── .gitignore             # Git ignored files
```

## Installation
### Prerequisites
- Python 3.x
- pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/SudhanshuGulhane/GenAI_ChatBot.git
   cd GenAI_ChatBot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the browser and visit:
   ```
   http://localhost:5000
   ```

## Usage
- Start the Flask server and interact with the chatbot via the web interface.
- The chatbot fetches responses using vector search and LLM-based processing.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

