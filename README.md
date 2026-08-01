# K.S.O.N.

**K.S.O.N.** – **Knurski System Omijania Niebezpieczeństw**

K.S.O.N. is a lightweight Discord bot that selects random excuses from a text-file database. It can include a mentioned user in the generated response and allows new entries to be added directly from Discord. Before saving an excuse, the bot checks whether a similar entry already exists. The project was created as a small and humorous utility for Discord servers.

## Technologies

`Python` `discord.py` `Discord API` `Text-file database` `String comparison`

## Commands

* `!bo` – draws a random excuse from the database.
* `!bo @user` – draws an excuse and mentions the selected user.
* `!add <reason>` – adds a new excuse to the database.

## Configuration and development status

Create a text database with one excuse per line, then configure `File_name` and `BOT_TOKEN` in `Discord_bot.py`. Never commit the bot token to the repository; a future version should load it from an environment variable. The current implementation is functional, with possible improvements including command permissions and more robust database management.
