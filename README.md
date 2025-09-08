# 🎙️ Audio Transcriber (Whisper AI + Python)

Convert your long audio recordings into **Text, Word (.docx), and PDF** using **OpenAI Whisper**.  
This tool is **free, offline, and unlimited** – perfect for podcasts, lectures, sermons, interviews, or any long audio.

---

## ✨ Features
- ✅ Transcribe audio (MP3, WAV, M4A, etc.) into **plain text**
- ✅ Save transcripts as `.txt`, `.docx`, and `.pdf`
- ✅ Works fully offline (no API key required)
- ✅ Free & unlimited usage with **Whisper AI**
- ✅ Cross-platform: Windows, macOS, Linux

---

## 📂 Project Structure
```bash
audio-transcriber/
│
├── audioToText.py         # Main Python script
├── commands.txt           # Ready-to-use CLI commands
├── note.txt               # Step-by-step installation & usage guide
├── README.md              # Project documentation
├── requirements.txt       # Dependencies list
├── docx/                  # Transcribed TXT/DOCX/PDF files
└── sample\_audio/          # Example audio files
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/King-Greatman-Spirit/audio-transcriber-whisper.git
cd audio-transcriber-whisper
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Transcription

```bash
python audioToText.py sample_audio/audio.mp3
```

---

## 📦 Output

After running the script, all transcripts will be stored in the **`docx/` folder**:

* `audio.txt` → Plain text transcript
* `audio.docx` → Word document with formatting
* `audio.pdf` → PDF document

Example:

```
docx/
 ├── sermon.txt
 ├── sermon.docx
 └── sermon.pdf
```

---

## 🛠 Installing FFmpeg (Windows Guide)

Whisper requires **FFmpeg** for audio decoding.
Follow these steps to install:

### Step 1: Download FFmpeg

👉 [Download from gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
Choose **ffmpeg-release-essentials.zip**.

### Step 2: Extract FFmpeg

Extract into:

```
C:\ffmpeg
```

You should now have:

```
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffplay.exe
C:\ffmpeg\bin\ffprobe.exe
```

### Step 3: Add FFmpeg to PATH

1. Press **Win + R** → type `sysdm.cpl` → Enter
2. Go to **Advanced tab** → **Environment Variables**
3. Select `Path` (under *System variables*) → **Edit** → **New** → Add:

   ```
   C:\ffmpeg\bin
   ```
4. Save & close

### Step 4: Verify Installation

Run in terminal:

```bash
ffmpeg -version
```

✅ If installed correctly, you’ll see version info (e.g., `ffmpeg version n6.1`).

---

## 🔧 Configuration

By default, the script uses the **`base` Whisper model** (balanced speed & accuracy).
You can modify `audioToText.py` to switch between models:

* `tiny` → Fastest, least accurate
* `base` → Balanced (default)
* `small` → Good quality
* `medium` → High accuracy
* `large` → Best accuracy (slowest)

---

## 📌 SEO Keywords

* Free offline audio transcription
* Convert MP3 to text with Python
* Whisper AI speech-to-text
* Transcribe audio to DOCX & PDF
* Best free transcription tool for long recordings

---

## 🤝 Contribution

Pull requests are welcome!
For major changes, open an issue first to discuss your ideas.

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 👤 Author

Created with ❤️ by [King-Greatman-Spirit](https://github.com/King-Greatman-Spirit)


