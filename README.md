# discord_bot

# Follow this guide to set up the discord end -> https://discordpy.readthedocs.io/en/latest/discord.html

# You will need python3, pip and pipenv

`sudo apt-get install python3`

`sudo apt-get install python-pip`

`sudo apt-get install pipenv`

# Clone the repo

`git clone https://github.com/insomniac807/discord_bot.git`

`cd discord_bot`

# Navigate to Master Branch

`git checkout master`

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

# Finally run bootstrap.sh to launch the backend API and have your bot go live

`./bootstrap.sh`

# If successful the server will output


 `* Serving Flask app "./server/server.py"`

 `* Environment: production`
  
  `* Debug mode: off`

`We have logged in as {YourBotName#YourBotId}`





