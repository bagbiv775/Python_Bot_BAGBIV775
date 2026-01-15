from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from keyboards import ikb_main_menu, ikb_back_to_main_menu
from utils import FileManager
from misc import timestamp
from utils.enum_path import Path

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message, command: CommandObject):
    await message.answer_photo(
        photo=FSInputFile(Path.IMAGES.value.format(file=command.command)),
        caption=FileManager.read_txt(Path.MESSAGES, command.command),
        reply_markup=ikb_main_menu(),
    )


# Вылавливаем любые некорректные текстовые команды
# Пользователю выдаем сообщение о неверной команде и предлагаем перейти в главное меню
# В консоль выводим сообщение о дате, времени, имени и ID пользователя, допустившего некорректное сообщение
@command_router.message()
async def all_messages(message: Message, bot: Bot):
    msg_text = f'{timestamp()}\nпользователь: {message.from_user.full_name}\nID: {message.from_user.id}\nнаписал: {message.text}\n'
    print(msg_text)

    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )

    await message.answer_photo(
        photo=FSInputFile(Path.IMAGES.value.format(file='error')),
        caption='Введена неверная команда!\nПожалуйста, воспользуйтесь главным меню.',
        reply_markup=ikb_back_to_main_menu(),
    )