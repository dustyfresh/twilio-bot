# Twilio Bot

## About
This repository is for a flask based twilio bot that I've been working. The bot simply will prank call phone numbers that you specify in your SMS command.

## Setup
Edit the *docker-compose.yml* file with your twilio API keys

```
$ git clone git@github.com:dustyfresh/twilio-bot.git
$ cd twilio-bot
$ docker-compose build
$ docker-compose up -d
```

## Available Commands
Each command has an associated MP3 to play when it calls someone. MP3 files can be found in the static assets directory  [here](https://github.com/dustyfresh/twilio-bot/tree/master/app/code/static/mp3), and the twilio XML config for each command can be found [here](https://github.com/dustyfresh/twilio-bot/tree/master/app/code/static/xml).

| command  | description  |
|---|---|
| !rickroll <number> | What monster would I be if I didn't bake this in right from the start? |
| !hack <number> | THEY'RE TRASHING OUR RIGHTS! |
| !taken <number> |  I have a very specific set of skills |
| !aha <number> | Play AHA - Take on me |
| !africa <number> | Play Toto - Africa |
| !sendbobs <number> | Play send bobs meme |
| !fedoras <number> | Swag is for boys, fedoras are for men |
| !rightround <number> | DoA - You spin me round |
| !iran <number> | flock of seagulls - i ran |
| !maxheadroom <number> | Let max headroom confuse them |
| !happybirthday <number> | Send happy birthday wishes from Mr. Rogers |
| !tookourjobs <number> | DEY TOOK ARE JERBS |
| !blicky <number> | Play Comethazine - Blicky |


## Support
Send me a DM on [twitter](https://twitter.com/dustyfresh) if you need help getting setup or adding commands.
