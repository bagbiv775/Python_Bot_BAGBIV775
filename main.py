from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message):
    print(message)
    print(message.text)


@dp.message()
async def all_messages(message: Message, bot: Bot):
    if message.from_user.full_name == 'Max':
        msg_text = f'Хватит баловаться, {message.from_user.full_name}!!!\nИди учи уроки!!!'
    else:
        msg_text = f'Пользователь {message.from_user.full_name} написал:\n{message.text}'

    await bot.send_message(message.from_user.id, msg_text) # я так сделал

    # await bot.send_message( # STONE так сделал
    #     message.chat.id,
    #     message.text,
    # )


async def start_bot():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())