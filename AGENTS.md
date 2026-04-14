# AGENTS.md - Development Guidelines

This document provides guidelines for working with the Discord Bots monorepo.

## Project Structure

```
discord-bot/
bots/
├── funfacts/         # Random fun fact (daily)
│   ├── app.py
│   ├── railway.json
│   └── requirements.txt
├── goodmorning/      # Daily good morning message (Mondays)
│   ├── app.py
│   ├── railway.json
│   └── requirements.txt
└── wordbot/          # Word of the day (daily)
    ├── app.py
    ├── railway.json
    └── requirements.txt
```

Each bot is a standalone Python script that exits after execution. They are triggered by Railway cron jobs.

## Commands

### Running a Bot Locally

```bash
# Good morning bot
cd bots/goodmorning
python app.py

# Word of the day bot
cd bots/wordbot
python app.py
```

### Linting

Use Ruff for linting and formatting:

```bash
# Lint all Python files
ruff check bots/

# Lint specific bot
ruff check bots/goodmorning/

# Auto-fix issues
ruff check --fix bots/

# Format code
ruff format bots/
```

### Testing

Currently no test suite exists. When adding tests:

```bash
# Run all tests (when added)
pytest

# Run tests for specific bot
pytest bots/goodmorning/

# Run single test file
pytest bots/goodmorning/test_app.py

# Run single test
pytest bots/goodmorning/test_app.py::test_send_morning_message
```

## Code Style

### Formatting
- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use double quotes for strings
- Trailing commas in multi-line collections

### Naming Conventions
- `snake_case` for functions and variables
- `UPPER_CASE` for module-level constants
- `PascalCase` for classes (if any)
- Descriptive names, avoid abbreviations

### Imports
```python
# Standard library imports first
import os
import json
import random

# Third-party imports second
import requests

# No relative imports in this project
```

### Function Structure
```python
def function_name():
    """Docstring describing what the function does."""
    # Implementation
    pass


def main_function():
    """Main entry point for the bot."""
    try:
        result = do_something()
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
```

### Error Handling
- Use `exit(1)` for fatal errors
- Always set timeouts on HTTP requests (10 seconds)
- Check HTTP response status codes explicitly
- Print error messages to stdout before exiting

### Environment Variables
- Use `os.environ["VAR_NAME"]` for required variables
- Use `os.environ.get("VAR_NAME", default)` for optional variables
- Define constants at module level after imports

### Constants
```python
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
DEFAULT_MESSAGE = "Default text"
TIMEOUT_SECONDS = 10
```

## Adding a New Bot

1. Create directory: `bots/<botname>/`
2. Create files:
   - `app.py` - Main entry point
   - `requirements.txt` - Dependencies
   - `railway.json` - Railway configuration with watch patterns
3. Follow existing patterns from `goodmorning` or `wordbot`
4. Template for `railway.json`:
   ```json
   {
     "$schema": "https://railway.com/railway.schema.json",
     "deploy": {
       "startCommand": "python app.py",
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10,
       "watchPatterns": ["/bots/<botname>/**"]
     }
   }
   ```

## Railway Deployment

- Each bot is a separate Railway service
- Root Directory: `bots/<botname>`
- Config File: `/bots/<botname>/railway.json`
- Cron schedules trigger execution
- Scripts must exit after completion (not persistent)

## Dependencies

- `requests` - HTTP client for Discord webhooks
- No async/await patterns (synchronous scripts)
- Keep dependencies minimal

## Commit Messages

Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code restructuring
- `chore:` - Maintenance tasks
- `docs:` - Documentation updates
