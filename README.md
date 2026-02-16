# CoachBot AI — Smart Fitness Assistance

CoachBot AI is a Streamlit demo that builds structured prompts from athlete inputs and requests coaching guidance from a generative model (Gemini or OpenAI). This repository is a scaffold you can extend for research or small demo deployments.

**Repository name:** workspace

**Main files**
- `app.py` — Streamlit application and prompt builder (main entry).
- `requirements.txt` — Python dependencies.

**Quick Start (local)**

Prerequisites: Python 3.10+, virtualenv (recommended).

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Set an API key (OpenAI recommended for testing):

```powershell
setx OPENAI_API_KEY "sk-..."
# For the current session only (PowerShell):
$env:OPENAI_API_KEY = "sk-..."
```

4. Run the app:

```powershell
python -m streamlit run /workspace/app.py --server.port 8501
```

Open the UI at http://localhost:8501.

**Configuration / Environment variables**
- `OPENAI_API_KEY` — OpenAI API key (the app prefers this variable).
- `GEMINI_API_KEY` — Gemini API key (used if provider set to Gemini).
- `GOOGLE_API_KEY` — legacy/alternate key names; the app may fall back to other vars.

Do not commit keys to source control. Add `.env` and any local key files to `.gitignore`.

**Using the app**
- Choose `Provider` in the app header: `Auto` (detects by key prefix), `Gemini`, or `OpenAI`.
- Paste an API key into the UI or set the corresponding environment variable.
- Toggle `mock_mode` to test the UI without network calls.

**Troubleshooting**
- `streamlit` command not found: run with `python -m streamlit` or ensure packages installed into the active Python environment.
- HTTP 401: invalid or unauthorized key. Confirm the key and billing in the provider dashboard.
- HTTP 429: rate-limited. Wait a minute, reduce `max_tokens`, enable `mock_mode`, or check account quotas. The app includes retry/backoff and mock fallback for OpenAI.

**Developer notes**
- The app prefers `OPENAI_API_KEY` if present. If you use a different env var name (e.g., `OPEN_AI_KEY`), either set `OPENAI_API_KEY` or update `app.py` to read your variable.
- Tests (if added) should live under `tests/` and run with `pytest`.

**Security**
- Rotate keys immediately if they appear in public history. Never commit `.env` or API keys.

**Contributing / Next steps**
- Improve and version prompt templates, add logging (scrub secrets), and add CI (lint/tests).
- Add deployment instructions (Streamlit Cloud, Docker, or a small VM).

**License**
MIT or your preferred license.

---

Files:
- [app.py](app.py)
- [requirements.txt](requirements.txt)
# CoachBot AI — Smart Fitness Assistance (Scaffold)

This repository contains a Streamlit scaffold for `CoachBot AI`, a generative-AI powered virtual coach demonstration using Gemini 1.5 (Gemini 1.5 Pro). The app collects athlete inputs and constructs prompts to request personalized training, recovery, tactical, and nutrition guidance from the Gemini model.

## Files
- `app.py` — Streamlit application scaffold with sample prompts and Gemini integration fallback.
- `requirements.txt` — Minimal dependency list.

## Setup
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Provide your Gemini API key either by setting an environment variable `GEMINI_API_KEY` or pasting it into the app's API key field.

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
# On Windows (PowerShell):
$env:GEMINI_API_KEY = "YOUR_API_KEY"
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

## Notes
- The code attempts to use the `google.generativeai` client if installed; if that fails it will fall back to a simple REST POST. Adjust the endpoint, request shape, and response parsing to match the exact Gemini client or REST API contract you are using for your project.
- The scaffold includes 10 example prompts/features required by the assignment. You should expand and refine these prompts and the prompt engineering logic to suit your final submission.

## Next steps you may want me to do
- Add prompt templates for specific sports/positions
- Implement prompt versioning, logging, and hyperparameter tuning UI
- Create a README section with rubric mapping and screenshots
- Package the app for deployment to Streamlit Cloud
# ShopImpact — Streamlit demo

This is a small demo app built with Streamlit that helps users log planned purchases and estimates CO₂ emissions, provides greener alternatives, and displays playful eco badges.

Files added:

- `app.py` — Streamlit app (main entry)
- `shopimpact/core.py` — core multipliers and calculation logic
- `tests/test_core.py` — small pytest tests
- `requirements.txt` — Python dependencies

Quick start (Windows PowerShell):

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

Notes:
- This demo persists purchases to `data.json` in the project folder.
- Multipliers are illustrative. For production, use curated LCA databases and unit-based multipliers.
