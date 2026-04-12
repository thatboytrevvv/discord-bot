# Discord Bots (Monorepo)

Discord webhook bots deployed on Railway.

## Structure

```
bots/
├── funfacts/         # Random fun fact of the day (daily)
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

## Railway Configuration

For each bot service in Railway:

1. **Root Directory**: Set to `bots/<botname>`
2. **Config File**: `/bots/<botname>/railway.json` (absolute path)
3. **Cron Schedule**: Configure as needed
4. **Environment Variables**:
   - `DISCORD_WEBHOOK_URL` (required)
   - `GOOD_MORNING_MESSAGE` (optional, goodmorning bot only)

## Adding a New Bot

1. Create directory: `bots/mybot/`
2. Add files:
   - `app.py` - Main script (should exit after running)
   - `requirements.txt` - Python dependencies
   - `railway.json` - Railway config with watch patterns
3. Configure Railway service with root directory `bots/mybot`

All bots are webhook-based (no persistent processes).
