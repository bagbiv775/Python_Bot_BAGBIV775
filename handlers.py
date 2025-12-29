from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from keyboards import keyboard_main_menu

import config
from utils import FileManager
from utils.enum_path import Path


main_router = Router()


@main_router.message(Command('start', 'random', 'gpt', 'talk', 'quiz'))
async def command_handler(message: Message, command: CommandObject):
    keyboard = None
    if command.command == 'start':
        keyboard = keyboard_main_menu()
    await message.answer_photo(
        photo=FSInputFile(Path.IMAGES.value.format(file=command.command)),
        caption=FileManager.read_txt(Path.MESSAGES, command.command),
        reply_markup=keyboard,
    )


# @main_router.message(Command('random'))
# async def random_command(message: Message):
#     await message.answer_photo(
#         photo=FSInputFile(Path.IMAGES.value.format(file='random')),
#         caption=FileManager.read_txt(Path.MESSAGES, 'random'),
#         reply_markup=keyboard_main_menu(),
#     )
#
#
# @main_router.message(Command('gpt'))
# async def gpt_command(message: Message):
#     await message.answer_photo(
#         photo=FSInputFile(Path.IMAGES.value.format(file='gpt')),
#         caption=FileManager.read_txt(Path.MESSAGES, 'gpt'),
#         reply_markup=keyboard_main_menu(),
#     )
#
#
# @main_router.message(Command('talk'))
# async def talk_command(message: Message):
#     await message.answer_photo(
#         photo=FSInputFile(Path.IMAGES.value.format(file='talk')),
#         caption=FileManager.read_txt(Path.MESSAGES, 'talk'),
#         reply_markup=keyboard_main_menu(),
#     )
#
#
# @main_router.message(Command('quiz'))
# async def quiz_command(message: Message):
#     await message.answer_photo(
#         photo=FSInputFile(Path.IMAGES.value.format(file='quiz')),
#         caption=FileManager.read_txt(Path.MESSAGES, 'quiz'),
#         reply_markup=keyboard_main_menu(),
#     )


# @main_router.message()
# async def all_messages(message: Message, bot: Bot):
#     msg_text = f'Пользователь {message.from_user.full_name} написал:\n{message.text}'
#     await bot.send_message(
#         chat_id=config.ADMIN_ID,
#         text = msg_text,
#     )
