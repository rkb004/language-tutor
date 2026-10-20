# Telugu Tutor — Local AI Language Learning Prototype

A proposed privacy-first conversational tutor for practicing **spoken Telugu using Romanized Telugu** (Telugu written with English letters). The project is designed around locally hosted language models and a lightweight Python API.

> **Status: Architecture and starter scaffold.** This repository documents the design and provides non-functional starter interfaces. It is **not** a complete application and has not been validated end-to-end.

## Why build it?

Language learners often need low-pressure conversational practice, immediate corrections, and examples they can actually use with family and friends. Telugu Tutor is designed to make short, contextual speaking exercises possible without requiring cloud-hosted conversations.

## Proposed experience

1. Choose a scenario, such as greeting a relative or ordering food.
2. Practice with a conversational tutor in **Romanized Telugu**.
3. Receive short corrections, translations, and alternative phrasing.
4. Continue the dialogue with a small session memory of vocabulary and mistakes.
5. Optionally add speech input and audio playback in a later iteration.

## Planned stack

| Component | Proposed technology | Role |
| --- | --- | --- |
| API | Python, FastAPI | Session and chat endpoints |
| Local inference | Ollama (e.g. Phi-3, Llama 3.1, Qwen 2.5) | Conversational generation |
| Speech-to-text | Whisper | Optional transcription |
| Memory | Local JSON/SQLite | Session history and vocabulary |
| UI | Future web or CLI client | Practice interface |

## Architecture

```text
Learner (future UI)
       |
       v
FastAPI routes (planned)
       |
       +-- Conversation service --> Ollama (local model)
       |
       +-- Session memory -------> Local storage
       |
       +-- Speech service -------> Whisper (optional)
```

## Repository structure

```text
app/
  api/            # Proposed HTTP route contracts
  models/         # Request and response schemas
  services/       # Planned tutor, memory and speech integrations
docs/
  architecture.md # Design decisions and roadmap
  example-dialogue.md
tests/            # Test cases to implement later
requirements.txt  # Intended dependencies (not validated)
```

## Example interaction (illustrative)

**Learner:** `Nenu Telugu nerchukuntunnanu.`

**Tutor:** `Chaala baagundi!` — That's great! You said, “I am learning Telugu.”

**Tutor:** `Meeru roju Telugu maatladutara?` — Do you speak Telugu every day?

The examples illustrate the desired interaction; they are not output from a running application.

## Proposed API

- `POST /chat` — Submit a learner message and receive a tutor reply.
- `POST /sessions` — Start a practice session.
- `GET /sessions/{session_id}` — Retrieve session context.
- `POST /transcribe` — Optional audio-to-text.

These endpoints are **design targets, not implemented endpoints**.

## Roadmap

- [x] Define concept and architecture
- [x] Document proposed API and example interaction
- [x] Add repository scaffolding
- [ ] Implement FastAPI routes
- [ ] Integrate Ollama and prompt templates
- [ ] Add session memory and vocabulary review
- [ ] Add Whisper speech input
- [ ] Build a learner-facing interface
- [ ] Add automated tests and end-to-end validation

## Design priorities

- **Romanized Telugu first:** accessible to learners who speak some Telugu but do not read the script fluently.
- **Local by default:** minimize sharing conversation data with third-party services.
- **Useful feedback:** explain corrections briefly, with natural alternatives.
- **Incremental architecture:** keep inference, memory, and speech services replaceable.

## Author

**Rachit Bandaram** · [GitHub](https://github.com/rkb004)

## License

MIT — see [LICENSE](LICENSE).
