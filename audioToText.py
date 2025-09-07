import sys
import os
import whisper
from docx import Document

def transcribe_audio(audio_path, output_folder="docx"):
    # Load model (base for speed, large for accuracy)
    model = whisper.load_model("base")

    print(f"🔄 Transcribing {audio_path} ... this may take a while.")
    result = model.transcribe(audio_path)

    # Extract text
    transcript = result["text"]

    # Save as .txt
    txt_file = os.path.splitext(os.path.basename(audio_path))[0] + ".txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"✅ Transcript saved as {txt_file}")

    # Save as .docx
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    docx_file = os.path.join(output_folder, os.path.splitext(os.path.basename(audio_path))[0] + ".docx")

    doc = Document()
    doc.add_heading("Audio Transcription", level=1)
    doc.add_paragraph(transcript)
    doc.save(docx_file)

    print(f"✅ Transcript saved as Word file: {docx_file}")

    return transcript

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python audioToText.py <audiofile>")
    else:
        audio_file = sys.argv[1]
        transcribe_audio(audio_file)
