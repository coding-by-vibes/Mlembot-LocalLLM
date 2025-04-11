"""
response_engine.py – Builds prompts and queries the LLM backend.
- Fetches active persona for the guild
- Constructs the full prompt from persona + user input
- Calls KoboldCpp API and returns the generated result
"""

"""
response_engine.py

Handles prompt construction and response generation for the local LLM bot.
Includes dynamic debug logging controlled by the `.env` variable: RESPONSE_DEBUG=true
"""

import os
from personas.loader import load_persona
from personas.prompt_builder import build_prompt
from utils.bot_data import bot_data_manager 
from utils.api import query_koboldcpp

DEBUG = os.getenv("RESPONSE_DEBUG", "false").lower() == "true"

# inside your message handler:
async def generate_response(guild_id, user_input, history):
    channel_data = bot_data_manager.get_channel(str(guild_id))
    persona_name = channel_data.bot_persona if channel_data else "default"
    persona = load_persona(persona_name)
    prompt = build_prompt(persona, history, user_input)

    if DEBUG:
        print(f"--- Generating for persona: {persona.name}")
        print("--- Prompt ---")
        print(prompt)
        print("--- End Prompt ---\n")

    response = await query_koboldcpp(
        prompt=prompt,
        settings=persona.kobold_settings,
        memory=persona.memory
    )

    return response


"""
Response Control Settings (from constants.API_DEFAULTS):

- temperature: Controls randomness. Lower = more deterministic. Default: 0.8
- top_p: Controls diversity via nucleus sampling. Default: 0.9
- top_k: Token cutoff rank. Default: 100
- rep_pen: Repetition penalty. Higher = less repetition. Default: 1.07
- max_length: Maximum tokens to generate. Dynamically set.
- stop_sequence: Token(s) that cause generation to halt.
- typical, tfs, top_a: Advanced sampling fine-tuning (see Kobold docs).
- quiet, trim_stop, use_default_badwordsids: Format and filter flags.

To override any setting per-request, update the payload inside generate_response().
"""

