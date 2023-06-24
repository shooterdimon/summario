from config import API_TOKEN
from summary_tools import get_summary

import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


logger = logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dispatcher=Dispatcher(bot)


@dispatcher.message_handler(content_types=["text"])
async def suer_input_handler(message: Message):
    text = message.text

    await bot.send_chat_action(message.chat.id, 'typing')
    print(get_summary(text))
    await message.reply(get_summary(text)[:4096])


if __name__ == '__main__':
	executor.start_polling(dispatcher, skip_updates=True)