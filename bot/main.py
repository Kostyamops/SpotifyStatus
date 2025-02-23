import asyncio
import config
import telebot
import time
import typing
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


bot = telebot.TeleBot(config.bot_token, parse_mode='HTML')
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-read-currently-playing",
        client_id=config.client_id,
        client_secret=config.client_secret,
        redirect_uri=config.redirect_uri,
        username=config.spotiusername,
    )
)

current_playing = typing.List[typing.Union[str, str, str]]

async def update_status(_current_playing):
    while True:
        current = spotify.current_user_playing_track()
        time_now = datetime.now().strftime("%H:%M:%S")

        if current == None:
            music = "Сейчас ничего не играет" + "\n" + "<a href='https://open.spotify.com/user/31k7a3hib7meibguomhesoo3cxii'><i>Профиль Спотифай</i></a>" + " (" + str(time_now) + ")"

        else:
            track = current["item"]["name"]
            album = current["item"]["album"]["name"]
            artist = current["item"]["artists"][0]["name"]
            link = "https://open.spotify.com/track/" + str(list((current["item"]["uri"]).split(":"))[-1])

            if _current_playing != [track, album, artist]:
                music = "Сейчас играет: <b>" + artist + " - " + track + "</b>\n" + "<a href='" + link + "'><i>Спотифай</i></a>" + " (" + str(time_now) + ")"
        chat_id = '-1001893715085'
        bot.edit_message_text(chat_id=chat_id, message_id=421, text=music)

        time.sleep(15)


async def main():
    while True:
        try:
            await asyncio.gather(
                update_status(current_playing)
            )
        except Exception as e:
            telebot.logger.error(f"БОТ УПАЛ | БОТ УПАЛ | БОТ УПАЛ | БОТ УПАЛ")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())