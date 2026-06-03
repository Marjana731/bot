import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


a = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()

class RegistrationStates(StatesGroup):
    song = State()
    c = State()

btn1 = KeyboardButton(text="Am")
btn2 = KeyboardButton(text="E")
btn3 = KeyboardButton(text="G")
btn4 = KeyboardButton(text="F")

kb = ReplyKeyboardMarkup(keyboard=[[btn1, btn2],[btn3, btn4]])

@dp.message(F.text=="/start")
async def start(message: Message, state: FSMContext):
    await message.answer("Яка улюблена пісня")
    await state.set_state(RegistrationStates.song)

@dp.message(RegistrationStates.song)
async def song(message: Message, state: FSMContext):
    await state.update_data(song=message.text)
    user_data = await state.get_data()

    await message.answer("Виберіть акорд", reply_markup=kb)
    await state.set_state(RegistrationStates.c)

@dp.message(RegistrationStates.c)
async def c(message: Message, state: FSMContext):
    await state.update_data(c=message.text)
    user_data = await state.get_data()

    await message.answer(
        f"Реєстрація завершена! Ваші дані:\n"
        f"пісня: {user_data.get('song')}\n"
        f"акорд: {user_data.get('c')}\n"
    )
    await state.clear()

@dp.message(F.text=="Привіт!")
async def hello(message: Message):
    await message.answer("Привіт")

@dp.message(F.text=="як справи")
async def b(message: Message):
    await message.answer("добре", reply_markup=ReplyKeyboardRemove())

async def main():
    await dp.start_polling(a)


asyncio.run(main())