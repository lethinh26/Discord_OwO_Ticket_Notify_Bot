# Discord OwO Ticket Notify Bot

## Author

**Creator:** lethinh26

## Introduction

Discord OwO Ticket Notify Bot is a fully compliant Discord bot that works alongside [Discord OwO Ticket Notify Self](https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Self). This bot provides real-time stock updates in a designated channel and notifies a specific role whenever an update occurs.

**Important Note:** This bot will not function properly without [Discord OwO Ticket Notify Self](https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Self). Ensure that both are running for full functionality.

## Features

- Fetches stock data from MongoDB every 30 seconds.
- Displays an updated stock list in a specified notification channel.
- Pings a designated role when new stock information is available.
- Fully adheres to Discord’s Terms of Service.

## Installation

### Requirements

Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies
- `py-cord==2.5.0`
- `pymongo==4.10.1`

## Configuration

1. Clone the repository:
   ```bash
   git clone https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Bot.git
   cd Discord_OwO_Ticket_Notify_Bot
   ```
2. Configure the bot by modifying the following variables in the script:
   ```python
   mongo = MongoClient("mongodb+srv://...") # Replace your mongoDB srv
   NOTI_CHANNEL_ID = 123  # Replace with the actual channel ID
   TOKEN = ""  # Your bot token
   ROLE_ID = 123  # Replace with the role ID to be pinged
   ```
3. Start the bot:
   ```bash
   python main.py
   ```

## Usage

- The bot retrieves stock data from MongoDB every 30 seconds.
- It updates the stock information in the designated notification channel.
- When new stock is available, it pings the specified role.

## Disclaimer

- This bot fully complies with Discord’s Terms of Service.
- It requires the [self-bot version](https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Self) to function properly.

