from src.ingestion.pdf_loader import ingest_documents


def main():
    """
    Entry point for PDF ingestion pipeline.
    """
    ingest_documents()


if __name__ == "__main__":
    main()