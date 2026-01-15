import os
from collections import namedtuple

from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import FileManager
from utils.enum_path import Path
from .callback_data import CallbackMenu, CallbackTalk, CallbackQUIZ, CallbackTranslator

Button = namedtuple('Button', ['text', 'callback'])


def ikb_main_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Рандомный факт', 'random'),
        Button('Спросить GPT', 'gpt'),
        Button('Разговор со звездой', 'talk'),
        Button('КВИЗ!', 'quiz'),
        Button('Переводчик', 'translator'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    keyboard.adjust(2, 1, 2)
    return keyboard.as_markup()


def ikb_random():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Хочу еще!', 'random'),
        Button('Закончить!', 'start'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    return keyboard.as_markup()


def ikb_gpt_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Еще запрос', 'gpt'),
        Button('Закончить!', 'start'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    return keyboard.as_markup()


def ikb_cancel_gpt():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Отмена',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()


def ikb_talk_menu():
    keyboard = InlineKeyboardBuilder()
    celebrity = [file.rsplit('.', 1)[0] for file in os.listdir(Path.IMAGES_DIR.value) if file.startswith('talk_')]
    for item in celebrity:
        text_button = FileManager.read_txt(Path.PROMPTS, item).split(',', 1)[0].split(' - ')[-1]
        keyboard.button(
            text=text_button,
            callback_data=CallbackTalk(
                button='talk',
                celebrity=item,
            )
        )
    keyboard.button(
        text='В главное меню',
        callback_data=CallbackMenu(button='start'),
    )
    keyboard.adjust(1)
    return keyboard.as_markup()


def ikb_talk_back():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Закончить!',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()


def ikb_quiz_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Программирование', 'quiz_prog'),
        Button('Математика', 'quiz_math'),
        Button('Биология', 'quiz_biology'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackQUIZ(
                button='quiz',
                subject=button.callback,
            )
        )
    keyboard.button(
        text='В главное меню',
        callback_data=CallbackMenu(button='start'),
    )
    keyboard.adjust(1)
    return keyboard.as_markup()


def ikb_quiz_navigation():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Еще вопрос!',
        callback_data=CallbackQUIZ(
            button='quiz',
            subject='quiz_more',
        ),
    )
    keyboard.button(
        text='Сменить тему!',
        callback_data=CallbackMenu(button='quiz'),
    )
    keyboard.button(
        text='Закончить!',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()


def ikb_translator_menu():
    keyboard = InlineKeyboardBuilder()
    languages = [file.rsplit('.', 1)[0] for file in os.listdir(Path.IMAGES_DIR.value) if file.startswith('translator_')]
    for language in languages:
        text_button = FileManager.read_txt(Path.PROMPTS, language).split('.', 1)[0].split(' на ')[-1]
        keyboard.button(
            text=text_button,
            callback_data=CallbackTranslator(
                button='translator',
                language=language,
            )
        )
    keyboard.button(
        text='В главное меню',
        callback_data=CallbackMenu(button='start'),
    )
    keyboard.adjust(2, 2)
    return keyboard.as_markup()


def ikb_translator_navigation():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Сменить язык!',
        callback_data=CallbackMenu(button='translator'),
    )
    keyboard.button(
        text='Закончить!',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()


def ikb_back_to_main_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='В главное меню',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()