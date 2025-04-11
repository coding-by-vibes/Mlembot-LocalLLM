"""
bot_data.py – Guild-level memory, persona, and generation settings manager.
Includes:
- BotChannelData: Stores per-guild context, persona, and config
- BotDataManager: Singleton for managing all runtime and persistent state
"""

from threading import Lock
"""Data models and state management for the Discord bot.

This module contains the data structures and state management logic for the bot,
including channel data, chat history, and bot settings.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
import time
import json
import os
from personas.loader import load_persona
from utils.history import save_channel_history, load_channel_history
from utils.constants import BOT_DEFAULTS
from utils.message import Message

@dataclass
class BotChannelData:
    busy: Lock = field(default_factory=Lock)
    """Represents the state and settings for a single Discord server."""
    temperature: float = BOT_DEFAULTS.get("temperature", 0.8)
    chat_history: List[Message] = field(default_factory=list)
    bot_reply_timestamp: float = field(default_factory=lambda: time.time() - 9999)
    bot_loop_timeout: int = BOT_DEFAULTS["default_idle_timeout"]
    bot_botloopcount: int = 0
    bot_override_memory: str = ""
    bot_persona: str = BOT_DEFAULTS["default_persona"]
    bot_maxlen: int = BOT_DEFAULTS["default_max_response_length"]
    guild_id: str = field(default="") 
    user_contexts: Dict[str, Dict] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "bot_reply_timestamp": self.bot_reply_timestamp,
            "bot_loop_timeout": self.bot_loop_timeout,
            "bot_botloopcount": self.bot_botloopcount,
            "bot_override_memory": self.bot_override_memory,
            "bot_persona": self.bot_persona,
            "bot_maxlen": self.bot_maxlen,
            "temperature": self.temperature,
        }

    def add_message(self, author: str, content: str, metadata: Optional[Dict] = None) -> None:
        if len(self.chat_history) >= BOT_DEFAULTS["max_history_length"]:
            self.chat_history.pop(0)

        user_context = self._extract_user_context(author, content)
        if user_context:
            self.user_contexts[author] = {**self.user_contexts.get(author, {}), **user_context}

        self.chat_history.append(Message(author=author, content=content, metadata=metadata or {}))
        save_channel_history(self.guild_id, self.chat_history)  # ⬅️ uses guild ID now

    def _extract_user_context(self, author: str, content: str) -> Dict:
        """Extract potential user context from message content."""
        context = {}
        
        # Look for self-introductions
        if "my name is" in content.lower():
            name = content.lower().split("my name is")[-1].strip()
            context["name"] = name
            
        # Look for preferences or characteristics
        if "i am" in content.lower():
            characteristics = content.lower().split("i am")[-1].strip()
            context["characteristics"] = characteristics
            
        # Look for interests
        if "i like" in content.lower():
            interests = content.lower().split("i like")[-1].strip()
            context["interests"] = interests
            
        return context

    def get_user_context(self, author: str) -> str:
        """Get formatted context for a specific user."""
        context = self.user_contexts.get(author, {})
        if not context:
            return ""
            
        context_parts = []
        if "name" in context:
            context_parts.append(f"Name: {context['name']}")
        if "characteristics" in context:
            context_parts.append(f"Characteristics: {context['characteristics']}")
        if "interests" in context:
            context_parts.append(f"Interests: {context['interests']}")
            
        return "\n".join(context_parts)

    def get_recent_messages(self, author: Optional[str] = None, limit: int = 5) -> List[Message]:
        """Get recent messages, optionally filtered by author."""
        messages = self.chat_history[-limit:] if limit > 0 else self.chat_history
        if author:
            messages = [msg for msg in messages if msg.author == author]
        return messages

class BotDataManager:
    """Manages bot data across all channels."""
    
    def __init__(self):
        self.channels: dict = {}
        self.personas: dict = {}
        self.load_personas()
        self.import_config()

    @staticmethod
    def get_guild_key(guild_id: str) -> str:
        return str(guild_id)
    
    def load_personas(self) -> None:
        """Load persona configurations from JSON files."""
        personas_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "personas"))
        for filename in os.listdir(personas_dir):
            if filename.endswith('.json'):
                persona_name = filename[:-5]
                with open(os.path.join(personas_dir, filename), 'r') as f:
                    self.personas[persona_name] = json.load(f)
    
    def import_config(self) -> None:
        try:
            config_path = os.path.abspath("botsettings.json")

            if os.path.exists(config_path):
                with open(config_path, 'r') as file:
                    raw = file.read().strip()
                    if not raw:
                        print("[CONFIG] Skipping empty botsettings.json")
                        return

                    data = json.loads(raw)
                    for d in data:
                        key = d['key']
                        if key not in self.channels:
                            self.channels[key] = BotChannelData(guild_id=key)

                        channel = self.channels[key]
                        channel.bot_loop_timeout = int(d.get('bot_loop_timeout', 8))
                        channel.bot_override_memory = d.get('bot_override_memory')
                        channel.bot_maxlen = int(d.get('bot_maxlen', 300))
                        channel.bot_persona = d.get('bot_persona', 'clippy')
                        channel.temperature = float(d.get('temperature', 0.8))

                print("[CONFIG] Imported botsettings.json")

        except Exception as e:
            print(f"[CONFIG] Failed to read settings: {e}")
    
    def export_config(self) -> None:
        try:
            data = []
            for guild_id, channel_data in self.channels.items():
                if ":" in guild_id:
                    print(f"[SKIP] Ignoring legacy key: {guild_id}")
                    continue
                data.append({
                    "key": guild_id,  # Now clearly a guild ID
                    "bot_loop_timeout": channel_data.bot_loop_timeout,
                    "bot_override_memory": channel_data.bot_override_memory,
                    "bot_maxlen": channel_data.bot_maxlen,
                    "bot_persona": channel_data.bot_persona,
                    "temperature": channel_data.temperature
                })

            config_path = os.path.abspath("botsettings.json")
            with open(config_path, 'w') as file:
                json.dump(data, file, indent=2)

            print("[CONFIG] Exported botsettings.json")

        except Exception as e:
            print(f"[CONFIG] Failed to export settings: {e}")
    
    def get_channel(self, guild_id: str) -> Optional[BotChannelData]:
        return self.channels.get(guild_id)
    
    def add_channel(self, guild_id: str, _=None):  # second arg ignored now
        key = str(guild_id)
        self.channels[key] = BotChannelData(guild_id=key)
        self.channels[key].bot_persona = "clippy"
    
    def remove_channel(self, guild_id: str) -> None:
        if guild_id in self.channels:
            del self.channels[guild_id]
    
    def get_persona(self, persona_name: str):
        """Return a schema-validated Persona object."""
        try:
            return load_persona(persona_name)
        except Exception:
            return load_persona("clippy")  # fallback

    def set_channel_persona(self, guild_id: str, persona_name: str, clear_history: bool = False) -> None:
        if guild_id in self.channels:
            channel = self.channels[guild_id]
            if clear_history:
                channel.chat_history = []
            channel.bot_persona = persona_name
            channel.bot_override_memory = ""
            self.export_config()


    def set_temporary_persona(self, guild_id: str, memory_override: str) -> None:
        if guild_id in self.channels:
            channel = self.channels[guild_id]
            channel.chat_history = []
            channel.bot_override_memory = memory_override
            self.export_config()


bot_data_manager = BotDataManager()