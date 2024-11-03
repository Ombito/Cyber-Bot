# Cyber-bot


Welcome to the **Cyber-Bot**. This bot is designed to enhance your Discord server experience by providing a variety of fun and useful commands. From greeting users to performing simple calculations, this bot aims to be a helpful companion in your community.

## Features

- Greet users with a friendly message.
- Perform basic arithmetic operations.
- Respond to ping checks.
- Provide information about the bot and its commands.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository** (or download the ZIP file):
   ```bash
   git clone https://github.com/Ombito/Cyber-bot.git
   cd Cyber-bot
   ```

2. **Install the required packages**:
   ```bash
   pip install discord.py
   ```

3. **Set up your Discord bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy the bot token.

4. **Create a `.env` file** in the root of your project directory and add your token:
   ```plaintext
   TOKEN=your_bot_token_here
   ```

## Usage

To run the bot, execute the following command in your terminal:

```bash
python3 main.py
```


Once the bot is running, invite it to your Discord server using the OAuth2 URL generated in the Discord Developer Portal. Make sure to give it appropriate permissions.

## Commands

Here are some commands you can use with the bot:

| Command              | Description                                           |
|---------------------|-------------------------------------------------------|
| `$hello`            | Greet the bot!                                       |
| `$ping`             | Check if the bot is responsive (responds with Pong!).|
| `$info`            | Get information about available commands.            |

## Contribution

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

---


Thank you for using our Cyber Bot. We hope it brings joy and utility to your server!
