from transformers import pipeline

from src.retrieval.retriever import Retriever


class RAGChatbot:

    def __init__(self):

        self.retriever = Retriever()

        self.generator = pipeline(
            task="text2text-generation",
            model="google/flan-t5-large",
            max_new_tokens=256
        )

        self.chat_history = []

    def build_prompt(self, query, context):

        history = "\n".join(self.chat_history[-4:])

        prompt = f"""
You are an AI assistant that answers questions
based only on the provided context.

Conversation History:
{history}

Context:
{context}

Question:
{query}

Instructions:
- Give a clear and accurate answer
- Use the provided context only
- If the answer is not in the context, say:
  "I could not find the answer in the documents."

Answer:
"""

        return prompt

    def generate_response(self, query):

        documents = self.retriever.retrieve(query)

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = self.build_prompt(
            query=query,
            context=context
        )

        response = self.generator(prompt)

        answer = response[0]["generated_text"]

        sources = []

        for doc in documents:

            source = doc.metadata.get(
                "source",
                "Unknown Source"
            )

            if source not in sources:
                sources.append(source)

        self.chat_history.append(
            f"User: {query}"
        )

        self.chat_history.append(
            f"Assistant: {answer}"
        )

        return {
            "answer": answer,
            "sources": sources
        }