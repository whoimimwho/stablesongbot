from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am π¦πΎππΎ VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @iamchildofcosmos β€

Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/-04-25-480",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π₯ Group", url="https://t.me/wearestrangethings"
                    ),
                    InlineKeyboardButton(
                        "πΎ Source code", url="https://github.com"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/wearestrangethings"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
