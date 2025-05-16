# Simple RAG Example

This project demonstrates a basic Retrieval-Augmented Generation (RAG) implementation using local LLMs through LM Studio. It's designed for educational purposes to help understand how RAG systems work.

## Overview

RAG (Retrieval-Augmented Generation) combines the power of large language models with the ability to retrieve relevant information from a knowledge base. This approach allows the model to generate responses based on specific information rather than relying solely on its pre-trained knowledge.

## Features

- Document storage and retrieval using ChromaDB vector database
- Local LLM integration through LM Studio
- Simple question-answering interface
- Context-aware responses based on retrieved documents

## Prerequisites

- Python 3.8+
- LM Studio running locally on port 1234
- ChromaDB

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make sure LM Studio is running with the API server enabled on port 1234

## Project Structure

- `main.py` - Main application entry point
- `data_access/chromadb_repo.py` - ChromaDB repository for document storage and retrieval
- `services/llm_service.py` - Service for interacting with the local LLM
- `data/txts/` - Directory containing text files for the knowledge base

## Usage

1. Start LM Studio and run a model with the API server enabled
2. Run the main script:
```bash
python main.py
```
3. Enter your question when prompted
4. The system will retrieve relevant information and generate a response

## How It Works

1. Text documents are stored in ChromaDB as vector embeddings
2. When a question is asked, the system retrieves the most relevant document(s)
3. The retrieved context and the question are sent to the LLM
4. The LLM generates a response based on the provided context

## Example
```text
Enter a question: What is GreenAirBot?
RAG Answer: GreenAirBot is an AI-powered assistant designed to provide information about air quality data and help users understand air pollution metrics.
```

## Customization

- Change the LLM model by modifying the `model` parameter in `call_llm()`
- Adjust the number of retrieved documents by changing the `n_results` parameter in `retrieve_relevant_documents()`
- Add more documents to the knowledge base by placing text files in the data directory

## License

This project is available for educational purposes.