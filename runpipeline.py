#from data.download_medquad import download_medquad
from data.preprocess import preprocess_medquad
#from ingestion.loader import load_medquad_documents
#from ingestion.embeddings import get_embedding_model
#from ingestion.chunker import chunk_documents
#from ingestion.build_index import build_index

def main():
    #download_medquad()
    preprocess_medquad()
    #load_medquad_documents()
    #get_embedding_model()
    #chunk_documents()
    #build_index()


if __name__ == "__main__":
    main()