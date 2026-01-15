from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto
from aiogram.types.input_file import FSInputFile

from ai_open import chat_gpt
from ai_open.enums import GPTRole
from ai_open.messages import GPTMessage
from keyboards import ikb_gpt_menu, ikb_talk_back, ikb_quiz_navigation, ikb_translator_navigation
from utils import FileManager
from utils.enum_path import Path
from .fsm import GPTRequest, CelebrityTalk, QUIZ, Translator

fsm_router = Router()


@fsm_router.message(GPTRequest.wait_for_request)
async def wait_for_user_request(message: Message, state: FSMContext, bot: Bot):
    msg_list = GPTMessage('gpt')
    msg_list.update(GPTRole.USER, message.text)
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )
    response = await chat_gpt.request(msg_list, bot)
    message_id = await state.get_value('message_id')
    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile(Path.IMAGES.value.format(file='gpt')),
            caption=response,
        ),
        chat_id=message.from_user.id,
        message_id=message_id,
        reply_markup=ikb_gpt_menu(),
    )


@fsm_router.message(CelebrityTalk.dialog)
async def user_dialog_with_celebrity(message: Message, state: FSMContext, bot: Bot):
    message_list = await state.get_value('messages')
    celebrity = await state.get_value('celebrity')
    message_list.update(GPTRole.USER, message.text)
    response = await chat_gpt.request(message_list, bot)
    message_list.update(GPTRole.CHAT, response)
    await state.update_data(messages=message_list)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile(Path.IMAGES.value.format(file=celebrity)),
        caption=response,
        reply_markup=ikb_talk_back(),
    )


@fsm_router.message(QUIZ.game)
async def user_answer(message: Message, state: FSMContext, bot: Bot):
    message_list = await state.get_value('messages')
    message_id = await state.get_value('message_id')
    score = await state.get_value('score')
    message_list.update(GPTRole.USER, message.text)
    response = await chat_gpt.request(message_list, bot)
    message_list.update(GPTRole.CHAT, response)
    await state.update_data(messages=message_list)
    if response == 'Правильно!':
        score += 1
        await state.update_data(score=score)
    response += f'\n\nВаш счет: {score} баллов!'
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )
    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile(Path.IMAGES.value.format(file='quiz')),
            caption=response,
        ),
        chat_id=message.from_user.id,
        message_id=message_id,
        reply_markup=ikb_quiz_navigation(),
    )


@fsm_router.message(Translator.wait_for_text)
async def translate_text(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    language = data['language']
    message_id = data['message_id']

    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )

    await bot.edit_message_media(
        media=InputMediaPhoto(
            # media=FSInputFile(Path.IMAGES.value.format(file='translator')),
            media=FSInputFile(Path.IMAGES.value.format(file=language)),
            caption='Пожалуйста, подождите.\nПеревожу вашу фразу...',
        ),
        chat_id=message.from_user.id,
        message_id=message_id,
    )

    msg_list = GPTMessage('translator')
    text_prompt = FileManager.read_txt(Path.PROMPTS, language) + '\n' + message.text
    msg_list.update(GPTRole.USER, text_prompt)

    response = await chat_gpt.request(msg_list, bot)

    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile(Path.IMAGES.value.format(file=language)),
            caption=response,
        ),
        chat_id=message.from_user.id,
        message_id=message_id,
        reply_markup=ikb_translator_navigation(),
    )