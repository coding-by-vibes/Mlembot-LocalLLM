# personas/schema.py

from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class KoboldSettings(BaseModel):
    temperature: float = 0.7
    rep_pen: float = 1.1
    rep_pen_range: int = 256
    stop_sequence: List[str] = Field(default_factory=lambda: ["User:", "Bot:"])
    trim_stop: bool = True
    mirostat: int = 2
    mirostat_tau: float = 5.0
    mirostat_eta: float = 0.1
    top_p: float = 0.9
    top_k: int = 100
    typical: float = 1.0
    tfs: float = 1.0
    top_a: float = 0.0
    logit_bias: Optional[Dict[int, float]] = None
    banned_tokens: Optional[List[str]] = None
    max_length: int = 300  # ✅ default token limit

class Persona(BaseModel):
    name: str
    display_name: Optional[str]
    persona: str
    scenario: Optional[str] = ""
    greeting: Optional[str] = ""
    example_dialogues: List[str] = Field(default_factory=list)
    memory: str
    kobold_settings: KoboldSettings