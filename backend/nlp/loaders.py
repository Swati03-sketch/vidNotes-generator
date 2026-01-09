import re
import PyPDF2
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound


def load_text(text: str) -> str:
    if not text.strip():
        raise ValueError("Empty text input!")
    return text


def load_pdf(file_path: str) -> str:
    if not file_path.lower().endswith(".pdf"):
        raise ValueError("Please attach a PDF file!")
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def extract_yt_id(url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None


def load_youtube(url: str) -> str:
    video_id = extract_yt_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL!")

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
    except TranscriptsDisabled:
        raise ValueError("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise ValueError("No transcript found for this video.")

    return " ".join(item.text for item in transcript)
