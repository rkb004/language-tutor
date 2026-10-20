"""Future local session-memory service."""


class SessionMemory:
    def load(self, session_id: str):
        raise NotImplementedError("Session storage is not implemented")

    def save(self, session_id: str, turns):
        raise NotImplementedError("Session storage is not implemented")
