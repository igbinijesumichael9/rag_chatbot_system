from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_PATH = "artifacts/chroma_db"


class Retriever:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_db = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=self.embeddings
        )

    def retrieve(self, query, k=3):

        results = self.vector_db.similarity_search(
            query,
            k=k
        )

        return results