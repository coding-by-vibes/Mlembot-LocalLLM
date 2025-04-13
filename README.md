# MlemBot - Discord Bot with Local LLM Integration

A Discord bot that integrates with local language models (LLMs) for natural conversation, using KoboldAI/KoboldCpp as the backend.

This project was made through Cursor as I learn my way through python. If you encounter bugs, please let me know!

[Like this project? Buy me a coffee!](https://buymeacoffee.com/codingbyvibes)

## Features

- Local LLM integration via KoboldAI/KoboldCpp
- Channel-specific conversation settings
- Customizable bot personalities
- Conversation history management
- Admin commands for configuration
- Automatic model loading and management
- Windows batch scripts for easy startup

## Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- KoboldAI or KoboldCpp installed and running
- Windows OS (for batch scripts)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/coding-by-vibes/Mlembot-LocalLLM.git
cd Mlembot-LocalLLM
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and configure:
```bash
copy .env.example .env
```

4. Edit `.env` with your settings:
```
DISCORD_BOT_TOKEN=your_discord_bot_token
KAI_ENDPOINT=http://localhost:5001
ADMIN_NAME=your_discord_username
```

5. Configure KoboldCpp:
   - Copy `run_kobold.bat.example` to `run_kobold.bat`
   - Edit `run_kobold.bat` with your model path and settings

## Usage

1. Start KoboldCpp:
```bash
run_kobold.bat
```

2. Start the bot:
```bash
run_bot.bat
```

3. Use the following slash commands in Discord:
- `/botmaxlen` - Set maximum response length
- `/botsleep` - Put the bot to sleep
- `/botreset` - Reset conversation history
- `/botpersona` - Change bot's personality

## Project Structure

```
Mlembot-LocalLLM/
├── cogs/                 # Discord bot command modules
├── data/                 # Data storage and history
├── models/              # Model management and utilities
├── personas/            # Bot personality definitions
├── reference_docs/      # Documentation and API references
├── utils/               # Utility functions and helpers
├── .env                 # Environment variables
├── .env.example         # Example environment configuration
├── bot.py               # Main bot implementation
├── main.py              # Entry point
├── requirements.txt     # Project dependencies
├── run_bot.bat          # Bot startup script
├── run_kobold.bat       # KoboldCpp startup script
└── README.md           # Project documentation
```

## Reference Documentation

The `reference_docs/` directory contains important documentation:
- `discord_dev_setup.md` - Discord bot setup guide
- `kobold_api_usage.py` - Kobold API usage examples
- `koboldai_docs.json` - KoboldAI API documentation
- `koboldcpp_readme.md` - KoboldCpp documentation
- `kobold_api_schema.json` - Kobold API schema

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Development Guidelines

This project uses Cursor rules for consistent development practices. The `.cursorrules` file in the project root contains comprehensive guidelines for:
- Code quality and style
- Project architecture and patterns
- Testing and validation
- Security practices
- Version control
- Documentation maintenance
- AI collaboration

All contributors should review and follow these guidelines when working on the project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.