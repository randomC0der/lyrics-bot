# lyrics-bot

[![license](https://img.shields.io/github/license/randomC0der/lyrics-bot.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Install

### General

Create a file `lyrics.txt` containing all the lyrics.
Empty lines are ignored so you can put them as you like.

### Twitter

If you haven't already, [apply for a developer account](https://developer.twitter.com/en/apply-for-access), so that you get access to the API.
You have to set the following environment variables with their respective values.

- TwitterConsumerKey
- TwitterConsumerSecret
- TwitterAccessToken
- TwitterAccessSecret

In order to run the script, you have to install the dependency: `pip3 install tweepy`

### Discord

Dependency [discord.py](https://github.com/Rapptz/discord.py): `pip3 install discord.py`

## Usage

(todo)

## Contributing

The following stuff should be done:

- Genius Integration to pull lyrics automatically (<https://www.storybench.org/download-song-lyrics-genius-using-python/>, <https://genius.com/developers>, <https://github.com/johnwmillr/LyricsGenius>)
- unify logging

## License

[This code is licensed under the MIT license.](../LICENSE)
However, the lyrics are not covered by this license as they belong to their respective owners.
