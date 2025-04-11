import json
import os
from .schema import Persona, KoboldSettings

# personas/loader.py

def load_persona(persona_name: str, base_path="personas") -> Persona:
    path = os.path.join(base_path, f"{persona_name}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Persona '{persona_name}' not found at {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
  
    try:
        persona = Persona(**data)
        print(f"[LOADER] Loaded persona '{persona.name}' from file: {path}")
        print(f"[LOADER] Persona memory preview: {persona.memory[:60]}...")
    except Exception:
        fallback_path = os.path.join(base_path, "clippy.json")
        if os.path.exists(fallback_path):
            with open(fallback_path, "r", encoding="utf-8") as fallback_file:
                fallback_data = json.load(fallback_file)
                persona = Persona(**fallback_data)
                print(f"[LOADER] Fallback loaded: '{persona.name}' from {fallback_path}")
        else:
            raise

    # ✅ Inject or adjust stop_sequence
    stop_sequence = persona.kobold_settings.stop_sequence or []
    resolved_stops = []
    for token in stop_sequence:
        resolved_stops.append(token.replace("{{char}}", persona.name))

    # Always include standard speaker stop lines
    if f"\nUser:" not in resolved_stops:
        resolved_stops.append("\nUser:")
    if f"\n{persona.name}:" not in resolved_stops:
        resolved_stops.append(f"\n{persona.name}:")

    persona.kobold_settings.stop_sequence = resolved_stops

    return persona
