from data_access.chromadb_repo import ChromaDBRepository
from services.llm_service import call_llm


def rag(chroma_repo: ChromaDBRepository, user_input: str) -> str:
    relative_documents = chroma_repo.retrieve_relevant_documents(user_input, n_results=1)
    context = ""
    for doc in relative_documents:
        context += f"{doc["content"]}\n"
    system_prompt = f"Answer the following question based on the provided context:"
    user_prompt = f"Context: {context}\n\nQuestion: {user_input}"

    llm_response = call_llm(system_prompt, user_prompt)

    return llm_response


def main():
    chroma_repo = ChromaDBRepository("air_data_files_collection")
    chroma_repo.store_text_file('./data/txts/airdatafiles2.txt')

    user_input = input("Enter a question: ")
    answer = rag(chroma_repo, user_input)
    print(f"RAG Answer: {answer}")


if __name__ == '__main__':
    main()
