import time

from copy import deepcopy
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.exceptions import TelegramBadRequest

from keyboards.base_kb import create_kb
from lexicon.lexicon import LEXICON_COMMAND, LEXICON
from database.database import users_db, new_user
from services.funcs import wait_process, main_process_answer, mantra_process, to_k_m

router = Router()

# Обработка команды СТАРТ
@router.message(CommandStart())
async def process_start_command(message: Message):

    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(new_user)
        users_db[message.from_user.id]['time_0'] = time.time()

    await message.answer(text='🕉 <b>СОЗЕРЦАЙ</b> 🕉\n\n'
                              'Цветение <b>Чакр</b>\n'
                              'Питай их соком <b>Самадхи</b>\n'
                              'Пожни цветения <b>Мантрами</b>\n'
                              'Обрети из них <b>Волю</b>\n'
                              'Что бы укрепить\n\n'
                              '🕉 <b>СОЗЕРЦАНИЕ</b> 🕉', 
                         reply_markup=create_kb(f"{to_k_m('speed', message.from_user.id)}👁 -> 1🌀"))
    
    

# Обработка команды ХЕЛП
@router.message(Command(commands='mantras'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


# ИнЛайн обработка СОЗЕРЦАНИЯ
@router.callback_query((F.data == 'wait') | (F.data == 'muladhara' ) | (F.data == 'svadhishthana') | (F.data == 'manipura') | 
                (F.data == 'anahata') | (F.data == 'vishuddha') | (F.data == 'ajna') | 
                (F.data == 'sahasrara') | (F.data == 'will' ))
async def process_wait_command(callback: CallbackQuery):

    if callback.data == 'wait':

        # Обработка процесса
        wait_process(callback.from_user.id)

        # Что бы убрать ошибку одинаковых сообщений
        try:    
            await callback.message.edit_text(text=main_process_answer(callback.from_user.id),
                                            reply_markup=create_kb(f"{to_k_m('speed', callback.from_user.id)}👁 -> 1🌀"))
        except TelegramBadRequest:
            await callback.answer()
    
    else:
        mantra_process(callback.from_user.id, callback.data)

        # Что бы убрать ошибку одинаковых сообщений
        try:    
            await callback.message.edit_text(text=main_process_answer(callback.from_user.id),
                                            reply_markup=create_kb(f"{to_k_m('speed', callback.from_user.id)}👁 -> 1🌀"))
        except TelegramBadRequest:
            await callback.answer()
     



   
