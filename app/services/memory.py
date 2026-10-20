
from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, List


class ConversationMemory:
    def __init__(self, max_messages: int = 30):
        self.sessions = defaultdict(list)
        self.max_messages = max_messages

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str
    ) -> None:

        if role not in {"user", "assistant"}:
            raise ValueError("Invalid message role")

        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.sessions[session_id].append(message)

        self.sessions[session_id] = (
            self.sessions[session_id][
                -self.max_messages:
            ]
        )

    def get_history(
        self,
        session_id: str
    ) -> List[Dict]:

        return list(
            self.sessions.get(session_id, [])
        )

    def clear(self, session_id: str) -> None:
        self.sessions.pop(session_id, None)

    def session_count(self) -> int:
        return len(self.sessions)

