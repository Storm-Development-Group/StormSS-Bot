# StormSS-Bot

StormSS-Bot is a Discord bot that provides quick access to Storm Scanner's API within Discord servers. It allows users to fetch information from Storm Scanner's API directly through Discord commands.

## Installation

To use StormSS-Bot, follow these steps:

1. Clone this repository to your local machine:
```bash
git clone https://github.com/Storm-Development-Group/StormSS-Bot.git
```
2. Navigate to the project directory:
```bash
cd StormSS-Bot
```
3. Install the required dependencies. Make sure you have Python and pip installed:

```bash
pip install -r requirements.txt
```
4. Set up your configuration by editing the config.json file in the src directory. Add your bot token and specify your desired command prefix.

## Usage

Once you have set up your configuration, you can run the bot by executing the `main.py` file:

The bot will now be online and ready to respond to commands in your Discord server.

## Commands

The following commands are available:

- `<prefix>history <user>`: Fetches the history for a specified user.
- `<prefix>results <pin>`: Fetches results for a specified PIN.

Replace `<prefix>` with your bot prefix defined in `config.json`, `<user>` with a mention or Discord ID, and `<pin>` with the PIN you want to fetch results for.

## Files

- `src/main.py`: Contains the source code for the Discord bot.
- `src/config.json`: Configuration file where you can specify your bot token and command prefix.

## Contributing

Contributions are welcome! If you have suggestions or encounter any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [GPL-3.0 license](LICENSE).