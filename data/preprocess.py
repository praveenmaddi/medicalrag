
import pandas as pd
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

# RAW_DATA_DIR = 'C:/Users/rsvps/OneDrive/Desktop/Experiments/llm_engineering_class1/Capstone_RAG_MedicalData/medicalrag/data/raw'
# PROCESSED_DATA_DIR = 'C:/Users/rsvps/OneDrive/Desktop/Experiments/llm_engineering_class1/Capstone_RAG_MedicalData/medicalrag/data/processed'

def preprocess_medquad():

    print("Exploring/Pre-procesing MedQuAD dataset...")

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    input_path = RAW_DATA_DIR/"medquad.csv"
    output_path = PROCESSED_DATA_DIR/"medquad_clean.csv"

    df = pd.read_csv(input_path)
    start_rows = df.shape[0]
    print('rows before processing:', start_rows)

    # Missing Values/ Null Values - Drop or Impute
    df.isna().sum()
    # Drop rows with null answers. focus_area can be imputed from Question, but later
    df = df.dropna(subset=["answer", "focus_area"]).reset_index(drop=True)
    print('rows after removing missing values:', df.shape[0])

    # Duplicates
    print(df.nunique())

    # Pure duplicates - full row - remove them
    df_full_dup_removed = df.drop_duplicates(
        subset=["question", "answer", "source", "focus_area"],
        keep="first"
    ).reset_index(drop=True)

    # Partial duplicates - same question, source and focus_area but different answer - Merge the answers to the same question, source and focus_area
    merged_df = (
        df_full_dup_removed
        .groupby(["question", "source", "focus_area"], as_index=False)
        .agg({
            "answer": lambda x: "\n".join(x.drop_duplicates())
        })
    )
    end_rows = merged_df.shape[0]
    print('rows after processing missing values and duplicates:', end_rows)
    print('total rows removed:', start_rows - end_rows)
    merged_df.to_csv(output_path, index=False)
    print("Pre-processed Dataset copied to data/processed")

    """
    # Find full duplicates
    duplicates = (
        df1.groupby(["question", "answer", "source", "focus_area"])
          .size()
          .reset_index(name="count")
          .query("count > 1")
          .sort_values(by="count", ascending=False)
    )
    print(duplicates.shape)
    duplicates['count'].max()

    #Find partial duplicates 
    duplicates2 = (
        df_full_dup_removed.groupby(["question","source","focus_area"])
          .size()
          .reset_index(name="count")
          .query("count > 1")
          .sort_values(by="count", ascending=False)
    )
    """

if __name__ == "__main__":
    preprocess_medquad()