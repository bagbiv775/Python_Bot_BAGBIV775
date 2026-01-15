from aiogram.fsm.state import State, StatesGroup


class GPTRequest(StatesGroup):
    wait_for_request = State()


class CelebrityTalk(StatesGroup):
    dialog = State()


class QUIZ(StatesGroup):
    game = State()


class Translator(StatesGroup):
    language = State()
    wait_for_text = State()