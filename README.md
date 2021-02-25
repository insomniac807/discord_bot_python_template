# discord_bot

# Follow this guide to set up the discord end -> https://discordpy.readthedocs.io/en/latest/discord.html

# You will need python3, pip and pipenv

`sudo apt-get install python3`

`sudo apt-get install python-pip`

`sudo apt-get install pipenv`

# Clone the repo

`git clone https://github.com/insomniac807/discord_bot_python_template.git`

`cd discord_bot`

# Make sure you are in the root directory and give bootstrap.sh executable permission

`chmod +x ./bootstrap.sh`

# Create a python3 virtual environment

`pipenv --three`

# Launch it

`pipenv shell`

# Install Dependencies

`pipenv install`

# Go to env and replace BOT_TOKEN_GOES_HERE with your bot token

# rename env to .env

# Finally run bootstrap.sh to have your bot go live

`./bootstrap.sh`

# Console Should Log

`{YourBotName#YourBotId} is online`





