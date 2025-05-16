import chromadb
import os
import uuid
from typing import List, Dict, Any


class ChromaDBRepository:
    def __init__(self, collection_name: str = "documents"):
        """Initialize ChromaDB repository with a collection name."""
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def store_text_file(self, file_path: str, window_size: int = 100, overlap: float = 0.1) -> None:
        """
        Store text from a file using sliding window approach.
        
        Args:
            file_path: Path to the text file
            window_size: Size of each text chunk
            overlap: Percentage of overlap between chunks (0.0 to 1.0)
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        step_size = int(window_size * (1 - overlap))
        
        chunks = []
        ids = []
        metadatas = []
        
        for i in range(0, len(text), step_size):
            if i + window_size <= len(text):
                chunk = text[i:i+window_size]
            else:
                chunk = text[i:]
                if len(chunk) < window_size * 0.5:
                    break
            
            chunk_id = str(uuid.uuid4())
            chunks.append(chunk)
            ids.append(chunk_id)
            metadatas.append({
                "source": os.path.basename(file_path),
                "start_char": i,
                "end_char": i + len(chunk)
            })
        
        if chunks:
            self.collection.add(
                documents=chunks,
                ids=ids,
                metadatas=metadatas
            )
            print(f"Added {len(chunks)} chunks from {file_path} to ChromaDB")
    
    def retrieve_relevant_documents(self, query: str, n_results: int = 1) -> List[Dict[str, Any]]:
        """
        Retrieve the most relevant documents for a given query.
        
        Args:
            query: User input query
            n_results: Number of results to return
            
        Returns:
            List of relevant documents with their metadata
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        documents = []
        if results and 'documents' in results and results['documents']:
            for i, doc in enumerate(results['documents'][0]):
                document = {
                    "content": doc,
                    "metadata": results['metadatas'][0][i] if 'metadatas' in results and results['metadatas'] else {},
                    "distance": results['distances'][0][i] if 'distances' in results and results['distances'] else None,
                    "id": results['ids'][0][i] if 'ids' in results and results['ids'] else None
                }
                documents.append(document)

        return documents


if __name__ == '__main__':
    chroma_repo = ChromaDBRepository("air_data_files_collection")
    print(chroma_repo.retrieve_relevant_documents("What GreenAirBot is?"))
