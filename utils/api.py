"""
api.py – Sends prompts to KoboldCpp API and handles the response.
- Uses aiohttp to send async POST requests
- Accepts prompt, persona settings, and memory block
"""

# utils/api.py

"""API interaction utilities for the Discord bot.

This module contains functions for interacting with the KoboldCpp API,
including text generation.
"""

import aiohttp

async def query_koboldcpp(prompt: str, settings, memory: str):
    payload = {
        "prompt": prompt,
        "memory": memory,
        "temperature": settings.temperature,
        "rep_pen": settings.rep_pen,
        "rep_pen_range": settings.rep_pen_range,
        "stop_sequence": settings.stop_sequence,
        "trim_stop": settings.trim_stop,
        "mirostat": settings.mirostat,
        "mirostat_tau": settings.mirostat_tau,
        "mirostat_eta": settings.mirostat_eta,
        "top_p": settings.top_p,
        "top_k": settings.top_k,
        "typical": settings.typical,
        "tfs": settings.tfs,
        "top_a": settings.top_a,
        "max_length": settings.max_length,
        "quiet": True,
        "use_default_badwordsids": False,
        "sampler_order": [6, 0, 1, 3, 4, 2, 5],  # Matches KoboldAI default
        "stop_token_ids": [15]  # EOS stop
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5001/api/v1/generate", json=payload) as resp:
            data = await resp.json()
            return data["results"][0]["text"]
