from aiogram.filters.callback_data import CallbackData


class CallbackMenu(CallbackData, prefix='CM'):
    button: str


class CallbackTalk(CallbackData, prefix='CT'):
    button: str
    celebrity: str


class CallbackQUIZ(CallbackData, prefix='CQ'):
    button: str
    subject: str


class CallbackTranslator(CallbackData, prefix='CTR'):
    button: str
    language: str