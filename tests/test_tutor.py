
from app.services.memory import ConversationMemory
from app.services.tutor import TeluguTutor


def test_memory_stores_messages():
    memory = ConversationMemory()

    memory.add_message(
        "test-session",
        "user",
        "Namaskaram"
    )

    history = memory.get_history("test-session")

    assert len(history) == 1
    assert history[0]["content"] == "Namaskaram"


def test_memory_preserves_order():
    memory = ConversationMemory()

    memory.add_message("abc", "user", "Hello")
    memory.add_message(
        "abc", "assistant", "Namaskaram"
    )

    history = memory.get_history("abc")

    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"


def test_memory_limit():
    memory = ConversationMemory(max_messages=3)

    for i in range(5):
        memory.add_message(
            "abc", "user", f"Message {i}"
        )

    history = memory.get_history("abc")

    assert len(history) == 3
    assert history[0]["content"] == "Message 2"


def test_clear_session():
    memory = ConversationMemory()

    memory.add_message("abc", "user", "Hello")
    memory.clear("abc")

    assert memory.get_history("abc") == []


def test_prompt_requires_romanized_telugu():
    tutor = TeluguTutor()

    prompt = tutor.build_system_prompt("beginner")

    assert "English letters only" in prompt
    assert "Never use Telugu script" in prompt
    assert "beginner" in prompt

