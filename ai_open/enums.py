from enum import Enum


class GPTRole(Enum):
    USER = 'user'
    CHAT = 'assistant'
    SYSTEM = 'system'


class GPTModel(Enum):
    # GPT_3_TURBO = 'gpt-3.5-turbo'
    # GPT_4_TURBO = 'gpt-4-turbo'
    GPT_4_MINI = 'gpt-4o-mini'
    WHISPER = 'whisper-1' # для преобразования голоса в текст
    GPT_IMAGE = 'dall-e-3' # для создания картинок