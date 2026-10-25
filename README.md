# EmbedAI

A universal SaaS platform for building AI assistants grounded in the user's own
materials (text files, PDFs, web page content) and embedding them on websites via
`iframe`.

The project doubles as a learning ground for Python Core, backend engineering
(FastAPI, PostgreSQL) and AI Engineering (RAG, embeddings, evaluation, LLM security).

> Status: early MVP. See this README for scope and setup.

## Problem

Website owners, small businesses and freelancers want to expose an assistant on
their site that answers questions **from their own materials** — not from the
model's general knowledge. Existing options are often:

- expensive or closed-source,
- hard to deploy without a frontend team,
- not showing sources (hard to trust the answer),
- mixing data between customers.

## Target users

- **Small site and shop owners** — want to handle repetitive questions without
  hiring a support team.
- **Agencies and freelancers** — want to offer clients an assistant grounded in
  their content without building their own platform.
- **Small companies with a knowledge base** (FAQ, docs, offers) — want customers
  to find answers themselves.

## MVP scope (what we build first)

- user registration and login,
- assistant management (create, rename, delete),
- import of **TXT / Markdown** and **PDF** files (text extraction),
- text normalization and chunking with metadata (source, page, chunk index),
- embeddings and semantic search (pgvector),
- LLM answers grounded in the user's own sources, **with citations**,
- honest "I don't know" when the materials do not support an answer,
- data isolation between users and assistants,
- basic analytics (model usage, errors, failed imports, unanswered questions),
- `iframe` widget to embed an assistant on an external site,
- request limits and input size limits,
- local run and deployment instructions.

## Out of scope for the MVP (deliberately postponed)

Not built at this stage:

- payments and subscriptions,
- complex agents or tool calling,
- fine-tuning,
- an extensive analytics dashboard,
- microservices, Kubernetes,
- a separate React frontend (UI: FastAPI + Jinja2 + HTMX + CSS),
- a custom JavaScript widget (`iframe` is enough to start),
- OCR for scanned PDFs,
- importing from arbitrary URLs — only after SSRF protections.

## Main use cases

1. **A user signs up** and creates an assistant with a chosen name.
2. **Uploads materials** (TXT/Markdown/PDF) and sees their processing status.
3. **Asks a question** in the EmbedAI panel and receives an answer with sources
   (document, page number).
4. **Gets an honest "I don't know"** when the documents do not contain the answer.
5. **Embeds the assistant** on their own site via `iframe`, restricting allowed
   domains.
6. **The account owner** sees basic statistics and failures (imports, unanswered
   questions) and **cannot see** other accounts' data.

## Tech stack (summary)

- Python 3.12, `uv` (or `venv` + `pip` — one approach chosen for the whole project),
- FastAPI + Pydantic, Jinja2 + HTMX + CSS,
- PostgreSQL + SQLAlchemy 2.x + Alembic + pgvector,
- Ollama or an external model API through a custom adapter,
- pytest + Ruff, Docker Compose, GitHub Actions.

## Getting started

See [Development setup](#development-setup) below for local installation
instructions.

## Development setup

### Requirements

- [uv](https://docs.astral.sh/uv/) — Python package and project manager
- Git

### First-time setup

```bash
# Clone the repository (skip if you are already inside it)
git clone <repo-url> embedai
cd embedai

# Install Python 3.12 (uv downloads it if missing)
uv python install 3.12

# Create the virtual environment and install dependencies
uv sync

# Create the local environment file and fill in values
cp .env.example .env
# then edit .env (e.g. APP_SECRET_KEY)
```

### Daily commands

```bash
# Reproduce the environment from the lockfile
uv sync

# Run the test suite (configured in task 0.3)
uv run pytest

# Lint and format (configured in task 0.3)
uv run ruff check .
uv run ruff format .
```

### Reproducibility

The environment is pinned via `pyproject.toml`, `.python-version` and `uv.lock`.
On a fresh clone, `uv sync` recreates the same virtual environment.

## License

To be decided.