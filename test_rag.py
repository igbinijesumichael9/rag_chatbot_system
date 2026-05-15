from src.llm.rag_chain import RAGChatbot


def main():

    chatbot = RAGChatbot()

    while True:

        query = input(
            "\nAsk a question (or type 'exit'): "
        )

        if query.lower() == "exit":
            break

        result = chatbot.generate_response(query)

        print("\n========== RESPONSE ==========\n")

        print(result["answer"])

        print("\n========== SOURCES ==========\n")

        for source in result["sources"]:

            print(source)


if __name__ == "__main__":

    main()