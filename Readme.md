# VideoMind 🎥🧠

An AI-powered teaching assistant that lets you ask questions about your own video content. VideoMind converts video lectures into transcripts, embeds them for semantic search, and uses an LLM (Llama 3.2) with a Retrieval-Augmented Generation (RAG) pipeline to answer questions grounded in your video material.

## Features

- 🎞️ Converts video lectures into audio and text transcripts automatically
- 🔍 Generates vector embeddings from transcripts for semantic search
- 🤖 Uses RAG to retrieve relevant context and feed it to an LLM (Llama 3.2 via Ollama)
- 💬 Answers user queries grounded in the actual video content, not just general knowledge

## Tech Stack

- **Language:** Python
- **Speech-to-Text:** OpenAI Whisper
- **Embeddings & Vector Search:** joblib-based vector store
- **LLM:** Llama 3.2 (via Ollama)
- **Core Libraries:** NumPy, Pandas, Scikit-learn

## Project Structure

```
VideoMind/
├── jsons/                  # Transcript JSON files generated from audio
├── mp3_to_jsons.py         # Converts MP3 audio to JSON transcripts
├── output.json             # Sample/aggregated output data
├── preprocess_json.py      # Converts JSON transcripts to a dataframe with embeddings, saved as a joblib pickle
├── process_incoming.py     # Handles incoming query processing pipeline
├── prompt.txt               # LLM prompt template
├── response.txt            # Sample/logged model response
├── speech_to_text.py       # Speech-to-text conversion script
├── video_to_mp3.py         # Extracts audio (MP3) from video files
└── README.md
```

> **Note:** Virtual environments, raw audio/video files, and generated embedding files are excluded via `.gitignore` and not tracked in version control.

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com) installed locally, with the Llama 3.2 model pulled:
  ```bash
  ollama pull llama3.2
  ```
- `pip install -r requirements.txt` (Whisper, pandas, numpy, scikit-learn, joblib, etc.)

## How to Use This Teaching Assistant on Your Own Data

### Step 1 — Collect your videos
Move all your video files into the `video/` folder.

### Step 2 — Convert video to MP3
Extract audio from your videos by running:
```bash
python video_to_mp3.py
```

### Step 3 — Convert MP3 to JSON transcripts
Transcribe the audio files into text using Whisper:
```bash
python mp3_to_jsons.py
```

### Step 4 — Convert the JSON transcripts to vector embeddings
Build a searchable knowledge base from your transcripts:
```bash
python preprocess_json.py
```
This converts the JSON files into a dataframe with embeddings and saves it as a `.joblib` pickle file.

### Step 5 — Prompt generation and feeding to the LLM
Load the embeddings, retrieve relevant context for a user's query, build a prompt, and feed it to the LLM:
```bash
python process_incoming.py
```
The joblib file is loaded into memory, a relevant prompt is generated based on the user's query, and the response is returned by the LLM.

## Example Workflow

```
video/ → video_to_mp3.py → mp3 files
mp3 files → mp3_to_jsons.py → jsons/ (transcripts)
jsons/ → preprocess_json.py → embeddings.joblib
User query + embeddings.joblib → process_incoming.py → LLM response
```

## Future Improvements

- [ ] Add a simple web UI for querying videos
- [ ] Support batch processing of multiple courses/playlists
- [ ] Add caching for repeated queries
- [ ] Support additional LLM backends beyond Ollama

## License

Add your preferred license here (e.g., MIT).