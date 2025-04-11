"""
message.py – Represents a user or bot message in the chat log.
Includes:
- Message class with author/content/metadata
- to_dict/from_dict helpers for serialization
"""

# utils/message.py
from dataclasses import dataclass, field
import time
from typing import Dict

@dataclass
class Message:
    author: str
    content: str
    timestamp: float = field(default_factory=lambda: time.time())
    metadata: Dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "content": self.content,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Message':
        return cls(
            author=data["author"],
            content=data["content"],
            timestamp=data["timestamp"],
            metadata=data.get("metadata", {})
        )
