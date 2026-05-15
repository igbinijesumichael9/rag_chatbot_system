from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings


DATA_PATH = "data/raw"

VECTOR_DB_PATH = "artifacts/chroma_db"


def load_pdf_documents():

    documents = []

    pdf_files = Path(DATA_PATH).glob("*.pdf")

    for pdf_file in pdf_files:

        print(f"Loading: {pdf_file}")

        loader = PyPDFLoader(str(pdf_file))

        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    return documents


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for document in documents:

        chunks = text_splitter.split_documents([document])

        for chunk in chunks:

            chunk.metadata["source"] = (
                document.metadata.get(
                    "source",
                    str(document.metadata)
                )
            )

            all_chunks.append(chunk)

    return all_chunks


def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vector_db.persist()

    print("\nVector database created successfully.")

    return vector_db


def ingest_documents():

    print("\n========== PDF INGESTION STARTED ==========\n")

    documents = load_pdf_documents()

    if not documents:

        print(f"No PDF files found in {DATA_PATH}")
        return

    print(f"\nLoaded {len(documents)} pages.")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    create_vector_store(chunks)

    print("\n========== INGESTION COMPLETED ==========\n")