# backend/nlp/pipeline.py

from .loaders import load_text, load_pdf, load_youtube
from .preprocessing import preprocess_text, tokenize_text
from .chunking import chunk_sen
from .generator import generate_notes

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


# Import inside function to avoid circular issues
def run_pipeline(source: str, input_data: str):
    from backend.api.llm_api import summarize_text

    if source == "text":
        raw_text = load_text(input_data)
    elif source == "pdf":
        raw_text = load_pdf(input_data)
    elif source == "youtube":
        raw_text = load_youtube(input_data)
    else:
        raise ValueError("Unsupported input type!")

    cleaned_text = preprocess_text(raw_text)
    sentences = tokenize_text(cleaned_text)
    chunks = chunk_sen(sentences, chunk_size=5)

    summaries = [summarize_text(chunk) for chunk in chunks]

    return {
        "notes": generate_notes(summaries)
    }

if __name__ == "__main__":
    youtube_url = "https://youtu.be/ukzFI9rgwfU?si=Ua0J-fIdyDaRdQnK"
    try:
        result = run_pipeline("youtube", youtube_url)
        print(result["notes"])
        
    except Exception as e:
        print("Error during pipeline execution:", str(e))