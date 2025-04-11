# MlemBot - Discord Bot with Local LLM Integration

A Discord bot that integrates with local language models for natural conversation.

## Features

- Local LLM integration
- Channel-specific settings
- Customizable personalities
- Conversation history management
- Admin commands for configuration

## Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- Local Language Model API endpoint

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mlembot.git
cd mlembot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:
```
DISCORD_BOT_TOKEN=your_discord_bot_token
KAI_ENDPOINT=your_local_llm_endpoint
ADMIN_NAME=your_discord_username
```

## Usage

1. Start the bot:
```bash
python src/main.py
```

2. Use the following slash commands in Discord:
- `/botmaxlen` - Set maximum response length
- `/botsleep` - Put the bot to sleep
- `/botreset` - Reset conversation history
- `/botpersona` - Change bot's personality

## Project Structure

```
mlembot/
├── src/
│   ├── bot/
│   │   ├── commands/       # Bot command implementations
│   │   ├── events/         # Bot event handlers
│   │   └── bot.py          # Main bot implementation
│   ├── config/
│   │   └── settings.py     # Configuration management
│   ├── models/
│   │   └── bot_data.py     # Data structures and state management
│   ├── utils/
│   │   ├── api.py         # API interaction utilities
│   │   └── text_processing.py # Text processing utilities
│   └── main.py            # Entry point
├── personas/              # Bot personality definitions
├── requirements.txt       # Project dependencies
├── .env                  # Environment variables
└── README.md            # Project documentation
```

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

This project is licensed under the MIT License - see the LICENSE file for details.