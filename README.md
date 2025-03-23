# Discord OwO Ticket Notify & OwO Ticket Notify Bot

## Author

**Creator:** lethinh26

## Introduction

Discord OwO Ticket Notify is a self-bot that monitors the `#seller-ads` channel in the Support OwO server for stock-related messages. If someone posts a message indicating they are selling a ticket, the bot extracts relevant stock information and stores it in a MongoDB database. This allows for real-time tracking of ticket availability.

Discord OwO Ticket Notify Bot is a separate bot designed to legally operate under Discord’s Terms of Service. It works alongside the self-bot, providing a visible stock list in a designated channel, updating every 30 seconds, and notifying roles when updates occur. **Both codes are interdependent and cannot function separately.**

## Features

### Discord OwO Ticket Notify (Self-Bot)
- Monitors messages in a specified channel for stock updates.
- Extracts and stores stock information from messages.
- Updates stock details if messages are edited.
- Removes stock records if messages are deleted.

### Discord OwO Ticket Notify Bot
- Displays the stock list in a specified channel.
- Updates the stock list every **30 seconds**.
- Pings a specified role when stock is updated.

## Installation

### Requirements

Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies

#### For Self-Bot
- `pymongo==4.10.1`
- `git+https://github.com/dolfies/discord.py-self.git`

#### For Bot Version
- `py-cord==2.5.0`
- `pymongo==4.10.1`

## Configuration

### Self-Bot Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lethinh26/Discord_OwO_Ticket_Notify.git
   cd Discord_OwO_Ticket_Notify
   ```
2. Configure the bot by modifying the following variables in the script:
   ```python
   mongo = MongoClient("mongodb+srv://...") # Replace your mongoDB srv
   OWO_TICKET_CHANNEL = 123  # Replace with the actual channel ID
   NOTI_CHANNEL = 123  # Replace with the actual notification channel ID
   TOKEN = ""  # Your Discord self-bot token
   ```
3. Start the bot:
   ```bash
   python bot.py
   ```

### Bot Version Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Bot.git
   cd Discord_OwO_Ticket_Notify_Bot
   ```
2. Configure the bot with the following variables:
   ```python
   NOTI_CHANNEL_ID = 123  # Replace with the actual notification channel ID
   TOKEN = ""  # Your bot token
   ROLE_ID = 123  # Replace with the actual role ID for pings
   ```
3. Start the bot:
   ```bash
   python bot.py
   ```

## Usage

- **Self-Bot** automatically syncs messages containing "stock" or "stocks" when it starts.
- **Self-Bot** extracts stock information from messages and stores it.
- **Self-Bot** updates stock data if messages are edited.
- **Self-Bot** removes stock records if messages are deleted.
- **Bot Version** fetches stock data every 30 seconds and updates the embed.
- **Bot Version** pings a specified role when stock data changes.

## Important Note

This code has been intentionally restricted to minimize the risk of being detected by Discord. Since it is a self-bot, it only runs and logs notifications in the console. However, self-bots violate Discord’s Terms of Service, which can lead to account termination. If you want to unlock the full potential of this bot, consider using the dedicated bot version that I have prepared: [Discord_OwO_Ticket_Notify_Bot](https://github.com/lethinh26/Discord_OwO_Ticket_Notify_Bot).

## Disclaimer

- **Self-bots are against Discord's Terms of Service. Use at your own risk.**
- **For a fully compliant version, use Discord OwO Ticket Notify Bot.**

