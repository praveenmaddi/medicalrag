from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(
    documents,
    chunk_size=500,
    chunk_overlap=100
):
    """
    Split documents into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []

    for doc in documents:

        text = doc["text"]

        metadata = doc["metadata"]

        split_texts = splitter.split_text(text)

        for chunk in split_texts:

            chunks.append(
                {
                    "text": chunk,
                    "metadata": metadata
                }
            )

    return chunks