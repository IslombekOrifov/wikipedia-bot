"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from decouple import config
import wikipedia

from aiogram import Bot, Dispatcher, executor, types


wikipedia.set_lang('uz')


API_TOKEN = config("TOKEN", default="Your Token")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi its a echo bot")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        result = wikipedia.summary(message.text)
        await message.answer(result)
    except:
        await message.answer('Bunday maqola topilmadi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)