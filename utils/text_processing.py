"""Text processing utilities for the Discord bot.

This module contains functions for processing and validating text input,
including text formatting.
"""

import re
from typing import List

def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to a specified maximum length.
    
    Args:
        text: The text to truncate
        max_length: Maximum length of the text
        
    Returns:
        str: Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def format_chat_history(messages: List[str], bot_name: str) -> str:
    """Format chat history for the bot's context.
    
    Args:
        messages: List of chat messages
        bot_name: Name of the bot
        
    Returns:
        str: Formatted chat history
    """
    formatted = "\n".join(f"### {msg}" for msg in messages)
    return f"{formatted}\n### {bot_name}:"

def clean_bot_mention(text: str, bot_name: str) -> str:
    """Remove mentions of the bot from text.
    
    Args:
        text: Text to clean
        bot_name: Name of the bot
        
    Returns:
        str: Cleaned text without bot mentions
    """
    # Create regex pattern to match @bot_name or @bot_name with any case
    pattern = re.compile(rf'@\s*{re.escape(bot_name)}', re.IGNORECASE)
    # Replace all matches with empty string and strip whitespace
    return pattern.sub('', text).strip() 