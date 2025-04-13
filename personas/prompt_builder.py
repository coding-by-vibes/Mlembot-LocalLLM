def build_prompt(persona, history: str, user_input: str) -> str:
    parts = []

    # Static rules header
    parts.append("[RULES]:\n"
                 "- You are only allowed to generate ONE message.\n"
                 "- Do NOT continue the conversation after your turn.\n"
                 "- Do NOT simulate scenes, narration, or actions. No RP.\n"
                 "- Do NOT describe what other characters say or do.\n"
                 "- Never write for the user.\n"
                 "- You must speak as yourself and stop.\n"
                 "- End your response without follow-up or prompting.\n")

    # Dynamically include persona fields that are strings
    label_map = {
        "scenario": "Scenario",
        "persona": "Personality",
        "authors_note": "Note",
        "appearance": "Appearance",
        "setting": "Setting"
    }

    for key, label in label_map.items():
        value = getattr(persona, key, None)
        if value and isinstance(value, str):
            parts.append(f"[{label}]: {value}")

    # Handle example_dialogues (must be list of strings)
    if hasattr(persona, "example_dialogues") and isinstance(persona.example_dialogues, list):
        examples = "\n".join(persona.example_dialogues)
        parts.append(f"[Example Dialogues]:\n{examples}")

    # Conversation history
    if history:
        parts.append(f"[Conversation]:\n{history}")

    # Final prompt input
    parts.append(f"User: {user_input}\n{persona.name}:")
    return "\n\n".join(parts)



# def build_prompt(persona, history: str, user_input: str) -> str:
#     parts = []

#     parts.append("[RULES]:\n"
#                  "- You are only allowed to generate ONE message.\n"
#                  "- Do NOT continue the conversation after your turn.\n"
#                  "- Do NOT simulate scenes, narration, or actions. No RP.\n"
#                  "- Do NOT describe what other characters say or do.\n"
#                  "- Never write for the user.\n"
#                  "- You must speak as yourself and stop.\n"
#                  "- End your response without follow-up or prompting.\n")

#     if persona.scenario:
#         parts.append(f"[Scenario]: {persona.scenario}")

#     if persona.persona:
#         parts.append(f"[Personality]: {persona.persona}")

#     if persona.example_dialogues:
#         examples = "\n".join(persona.example_dialogues)
#         parts.append(f"[Example Dialogues]:\n{examples}")

#     if history:
#         parts.append(f"[Conversation]:\n{history}")

#     parts.append(f"User: {user_input}\n{persona.name}:")
#     return "\n\n".join(parts)
