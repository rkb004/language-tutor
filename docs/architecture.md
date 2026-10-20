# Architecture notes

## Scope

This repository is an **unimplemented prototype scaffold**. Files under `app/` describe intended responsibilities rather than a working service.

## Components

- **API:** Accept text input, scenario, and optional session identifier.
- **Tutor engine:** Compose an instruction prompt for conversational practice and pass it to a local model via Ollama.
- **Memory:** Persist session context, repeated errors, and practiced vocabulary locally.
- **Speech (optional):** Transcribe learner audio with Whisper and pass the text to the tutor.

## Design choices

1. Use Romanized Telugu as the default output format, with concise English explanations.
2. Separate language model adapters from the conversation orchestration layer.
3. Make speech optional so text-only tutoring works without audio dependencies.
4. Avoid claiming fluency scoring without a validated evaluation method.

## Suggested implementation order

1. Basic `/chat` endpoint and input validation.
2. Ollama integration with timeout/error handling.
3. Local session storage.
4. Scenario prompts and correction formatting.
5. Speech support and tests.
