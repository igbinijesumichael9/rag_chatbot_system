from src.retrieval.retriever import VectorRetriever


def main():
    retriever = VectorRetriever()

    query = "What is FastAPI?"

    results = retriever.retrieve(query=query)

    print("\n========== RETRIEVAL RESULTS ==========\n")

    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}:\n")
        print(result.page_content[:1000])


if __name__ == "__main__":
    main()