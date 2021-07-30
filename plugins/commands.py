from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


REPO = "**Zer0Byte 2.0 :** [Updates](https://t.me/Zer0ByteOfficial)\n\n🌟 **Owner :** [Afgan Jalebi](https://t.me/deeprajk) \n\n**📍  [Group](https://t.me/Zer0ByteSupport)  &  [Off-Topic](https://t.me/deeprajk)   📍**"
HOME_TEXT = "👋 **Hi [{}](tg://user?id={})**,\n\nI'm **Zer0Byte 2.0** \nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop!\n\n**Thanks For Using**"
HELP = """**Join @Zer0ByteOfficial and @Zer0ByteSupport to get more help!!

🏷️ **Users Commands**:
\u2022 `/play`  -  Reply to an audio to play or add to queue.
\u2022 `/help`  -  Shows help for commands.
\u2022 `/playlist`  -  Shows the playlist.
\u2022 `/current`  -  Shows playing time of current track.
\u2022 `/song song name`  -  Download the song.

🏷️ **Admin Commands**:
\u2022 `/skip x`  -  Skip current or x song. [ x >= 2 ]
\u2022 `/join`  -  Join voice chat of current group.
\u2022 `/leave`  -  Leave current voice chat.
\u2022 `/vc`  -  Check which VC is joined.
\u2022 `/stop`  -  Stop playing music.
\u2022 `/radio`  -  Start radio stream.
\u2022 `/stopradio`  -  Stop radio stream.
\u2022 `/replay`  -  Play from the beginning.
\u2022 `/clean`  -  Remove unused RAW PCM files.
\u2022 `/pause`  -  Pause playing music.
\u2022 `/resume`  -  Resume playing music.
\u2022 `/mute`  -  Mute the VC Bot.
\u2022 `/unmute`  -  Unmute the VC Bot.
\u2022 `/restart`  -  Restart the bot.
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('🔔 Updates', url='https://t.me/The_HellBot'),
        InlineKeyboardButton('👥 Support', url='https://t.me/Its_Fuckin_Hell'),
    ],
    [
        InlineKeyboardButton('🌟 Owner', url='https://github.com/The-HellBot'),
        InlineKeyboardButton('✨ Off-Topic', url='https://github.com/The-HellBot/VcBot'),
    ],
    [
        InlineKeyboardButton('⚙️ HELP', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(REPO, disable_web_page_preview=True)


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
