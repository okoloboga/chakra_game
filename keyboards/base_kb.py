from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

from lexicon.lexicon import LEXICON
from database.database import users_db

def create_kb(button): 
    # Кнопки
    wait_button = InlineKeyboardButton(text=LEXICON['wait'], 
                                    callback_data='wait')

    muladhara_button = InlineKeyboardButton(text=LEXICON['muladhara'], 
                                            callback_data='muladhara')

    svadhishthana_button = InlineKeyboardButton(text=LEXICON['svadhishthana'], 
                                                callback_data='svadhishthana')

    manipura_button = InlineKeyboardButton(text=LEXICON['manipura'], 
                                        callback_data='manipura')

    anahata_button = InlineKeyboardButton(text=LEXICON['anahata'], 
                                        callback_data='anahata')

    vishuddha_button = InlineKeyboardButton(text=LEXICON['vishuddha'], 
                                            callback_data='vishuddha')

    ajna_button = InlineKeyboardButton(text=LEXICON['ajna'], 
                                    callback_data='ajna')

    sahasrara_button = InlineKeyboardButton(text=LEXICON['sahasrara'], 
                                            callback_data='sahasrara')

    will_button = InlineKeyboardButton(text=button, callback_data='will')

    keyboard = [[wait_button], [muladhara_button, svadhishthana_button, manipura_button, anahata_button],
                [vishuddha_button, ajna_button, sahasrara_button], [will_button]]

    inline_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return inline_markup