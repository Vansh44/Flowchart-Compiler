# Flowchart Compiler

A flowchart generation project with a FastAPI backend and a Streamlit frontend. The app uses OpenAI to generate MermaidJS and D2 flowchart code based on a natural language prompt, then renders and exports the result.

## Features

- FastAPI API for generating flowcharts
- Streamlit UI for prompt entry, Mermaid preview, and SVG export
- MermaidJS flowchart generation from natural language descriptions
- D2 flowchart generation endpoint for comparison
- Example Mermaid editor with live preview and download support

## Project Structure

- `api.py` — FastAPI application entry point
- `app.py` — Streamlit user interface
- `main.py` — helper scripts for launching API or UI
- `routes/flowchart.py` — flowchart generation endpoints
- `dto/flowchart.py` — request schema for flowchart generation
- `utils/openai.py` — OpenAI client helper
- `requirements.txt` — Python dependencies

## Requirements

- Python 3.10+
- `OPENAI_API_KEY` environment variable set

## Setup

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the API

Start the FastAPI backend:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

Then verify the endpoint:

```bash
curl http://localhost:8000/
```

## Running the Streamlit UI

Start the frontend app:

```bash
streamlit run app.py
```

Open the displayed URL in your browser. The UI includes:

- AI Generator tab for prompt-based Mermaid flowchart creation
- Manual MermaidJS editor tab
- Symbol Legend tab with syntax examples
- Compare Mermaid & D2 tab for additional flowchart views

## API Endpoints

### `POST /flowchart/mermaid`

Generates MermaidJS code from a prompt.

Request JSON:

```json
{
  "prompt": "Example prompt",
  "direction": "Top-to-Bottom",
  "complexity": "Medium"
}
```

Response JSON:

```json
{
  "mermaid_code": "flowchart TB\n..."
}
```

### `POST /flowchart/d2`

Generates D2 code from a prompt using the same request schema.

Response JSON:

```json
{
  "d2_code": "direction: down\n..."
}
```

## Notes

- The backend uses OpenAI via `openai.OpenAI` to generate flowchart code.
- The Streamlit UI converts Mermaid code to SVG using `https://mermaid.ink/svg`.
- If the app cannot connect to the API, check `API_URL` in `.env` and ensure the backend is running.

## License

This repository does not include a license file. Add one if you want to specify reuse terms.
