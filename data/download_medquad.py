import kagglehub
import os
import shutil


def download_medquad():

    print("Downloading MedQuAD dataset...")

    path = kagglehub.dataset_download(
        "pythonafroz/medquad-medical-question-answer-for-ai-research"
    )

    print(f"Dataset downloaded at: {path}")

    os.makedirs("data/raw", exist_ok=True)

    for file in os.listdir(path):
        source = os.path.join(path, file)
        destination = os.path.join("data/raw", file)

        if os.path.isfile(source):
            shutil.copy(source, destination)

    print("Dataset copied to data/raw")


if __name__ == "__main__":
    download_medquad()