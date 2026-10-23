# Python AI Agent Demo

This repository contains a simple Python-based AI agent demo for Chapter 01 of the "Python AI Agent Made Easy" series. It demonstrates how a local Python program can:

- answer product questions using a built-in catalog
- fall back to a local Ollama language model for general questions
- communicate with an AI model over the Ollama API

## Project Overview

The sample program in `intro_agent.py` combines a lightweight rule-based tool with a local LLM:

- If the user asks about a product's price or stock, the app checks a built-in product dictionary.
- If the question is not covered by the local product catalog, it sends the prompt to a model running via Ollama.
- The app continues to run in a loop until the user exits.

## Included Files

- `intro_agent.py` — main demo application
- `Chapter01_IntroAiAgent.py` — project entry file
- `Chapter01_IntroAiAgent.pyproj` — Python project configuration
- `Chapter01_IntroAiAgent.slnx` — solution configuration

## Requirements

Before running the project, make sure you have:

- Python 3.x installed
- Ollama installed and running locally
- A model available locally, such as:
  - `qwen3.5:9b`

## Setup

1. Install Ollama from https://ollama.com/
2. Start the Ollama service locally.
3. Pull the model used by the app:

```bash
ollama pull qwen3.5:9b
```

4. Run the Python script:

```bash
python intro_agent.py
```

## Example Usage

```text
You: What is the price of the laptop?

[Local Python Tool]
Assistant: Laptop price: RM3500.00

You: Tell me about Python decorators.

Asking Qwen 3.5...

Assistant: Python decorators are functions that modify or wrap other functions...
```

## Notes

- The local product catalog is intentionally simple and acts as a demonstration tool.
- Model access depends on a running Ollama service at `http://localhost:11434/api/chat`.
- The application is designed for learning and experimentation rather than production use.

## License

This project is provided as a learning example and may be used for educational purposes.
