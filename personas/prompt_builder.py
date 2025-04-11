def build_prompt(persona, history: str, user_input: str) -> str:
    parts = []

    parts.append("[RULES]:\n"
                 "- You are only allowed to generate ONE message.\n"
                 "- Do NOT continue the conversation after your turn.\n"
                 "- Do NOT simulate scenes, narration, or actions. No RP.\n"
                 "- Do NOT describe what other characters say or do.\n"
                 "- Never write for the user.\n"
                 "- You must speak as yourself and stop.\n"
                 "- End your response without follow-up or prompting.\n")

    if persona.scenario:
        parts.append(f"[Scenario]: {persona.scenario}")

    if persona.persona:
        parts.append(f"[Personality]: {persona.persona}")

    if persona.example_dialogues:
        examples = "\n".join(persona.example_dialogues)
        parts.append(f"[Example Dialogues]:\n{examples}")

    if history:
        parts.append(f"[Conversation]:\n{history}")

    parts.append(f"User: {user_input}\n{persona.name}:")
    return "\n\n".join(parts)
