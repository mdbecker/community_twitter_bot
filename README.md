community_twitter_bot
=====================

Twitter bot that allows approved users to tweet from a shared account using direct messages.

## Config
Example ``config.json``
```json
{
    "access_token": "694865265-OWQ3ZTk4YzE2NzE4NGU5OWJiMGFjZjBkN2E1NWM0",
    "access_token_secret": "NTYwMWJkYjIzZmZhNDNhZWI4OTZhNWU5OGU4ZDMxNDgYj",
    "api_key": "MzhhYmVkZjA3MjA1NGUyYWJmM",
    "api_secret": "OTRmZWI2NTY4ZjlhNDVkODhjYmI1ODlkOWU2ZGM1ZjMODIxMDd",
    "users": {"beckerfuffle": "MB"}
}
```

``access_token``, ``access_token_secret``, ``api_key``, and ``api_secret`` can be created by [setting up a twitter app](https://apps.twitter.com/). ``users`` is a dictionary containing a mapping of twitter handle to signature. Only users defined in the users dictionary will be allowed to relay tweets through the bot.

## Usage
This bot should be run as a deamon. It will listen for direct messages from authorized users that contain the hashtag #rt. It will retweet these messages and sign them with the authorized users signature.

## Contributing
Pull requests are welcome! I'm certain there are lots of other features that would be useful to other organizations.
