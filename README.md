# K.S.O.N.

**K.S.O.N.** - **Knurski System Omijania Niebezpieczeństw**

A small Discord bot that draws random excuses/reasons from a text database.  
The bot was made as a simple fun project for Discord servers.

## Features

- draws a random reason/excuse from a text file,
- can mention another user in the generated response,
- allows adding new reasons directly from Discord,
- checks whether a similar reason already exists in the database.

## Commands

### `!bo`

Draws a random reason from the database.

```text
!bo
```

Example response:

```text
reason: #12: example reason
```

### `!bo @user`

Draws a random reason and mentions the selected user.

```text
!bo @username
```

Example response:

```text
@username Im very sorry, but my client is unable to take part in this activity because: #12: example reason
```

### `!add`

Adds a new reason to the database.

```text
!add your new reason here
```

Example:

```text
!add I have to water my cactus
```

## Configuration

Before running the bot, update these values in `Discord_bot.py`.

Set the path or name of your text database file:

```python
File_name = "Your_database"
```

Replace `"Your_database"` with the name or path of your text file containing excuses/reasons.

Then set your Discord bot token at the bottom of the file:

```python
BOT_TOKEN = "Your bot token"
```

## Database file

The database is a normal text file.  
Each reason should be placed in a separate line, for example:

```text
I have to feed my goldfish
My internet is emotionally unavailable
I am busy avoiding responsibility
```
