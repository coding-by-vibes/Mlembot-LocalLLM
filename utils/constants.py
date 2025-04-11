"""Bot constants and configuration values."""

# API Configuration
API_DEFAULTS = {
    "max_context_length": 4096,
    "rep_pen": 1.07,
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 100,
    "top_a": 0,
    "typical": 1,
    "tfs": 1,
    "rep_pen_range": 320,
    "rep_pen_slope": 0.7,
    "sampler_order": [6,0,1,3,4,2,5],
    "min_p": 0,
    "genkey": "KCPP8888",
    "quiet": True,
    "trim_stop": True,
    "stop_sequence": ["\n###", "### "],
    "use_default_badwordsids": False
}

# Bot Configuration
BOT_DEFAULTS = {
    "max_message_length": 1000,
    "max_history_length": 20,
    "default_idle_timeout": 120,
    "default_max_response_length": 250,
    "default_persona": "clippy",
    "temperature": 0.8,
}

# Message Processing
MESSAGE_PATTERNS = {
    "name_intro": "my name is",
    "characteristics": "i am",
    "interests": "i like"
}

# Error Messages
ERROR_MESSAGES = {
    "not_whitelisted": "This channel is not whitelisted. Use /botwhitelist first.",
    "admin_only": "You don't have permission to use this command.",
    "command_failed": "Sorry, the command failed.",
    "bot_loop": "It appears that I am stuck in a conversation loop with another bot or AI. I will refrain from replying further until this situation resolves."
} 