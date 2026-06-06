import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


a = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()

btn1 = KeyboardButton(text="Вибір інструменту")
btn2 = KeyboardButton(text="Список пісень")
btn3 = KeyboardButton(text="Пошук акордів")


kb = ReplyKeyboardMarkup(keyboard=[[btn1, btn2],[btn3]])


btn = [
    [
        InlineKeyboardButton(text="Гітара", callback_data="button_1_pressed")
    ],
    [
        InlineKeyboardButton(text="Укулеле", callback_data="button_2_pressed")
    ]
]
kb2= InlineKeyboardMarkup(inline_keyboard=btn)




@dp.message(F.text=="/start")
async def start(message: Message, state: FSMContext):
    await message.answer("Привіт! Ласкаво просимо до «Збірника акордів»! Тут ти можеш швидко знайти акорди до улюблених пісень, переглянути тексти, підібрати тональність та вдосконалювати свою гру на гітарі. Просто напиши назву пісні або виконавця, і я допоможу знайти потрібні акорди.")
    await message.answer("Виберіть дію", reply_markup=kb)

@dp.message(F.text=="Вибір інструменту")
async def inst(message: Message):
    await message.answer("Виберіть інструмент", reply_markup=kb2)

@dp.callback_query(F.data=="button_1_pressed")
async def prs1(callback_query: CallbackQuery):
    await callback_query.message.answer("Ви вибрали гітару")


@dp.callback_query(F.data=="button_2_pressed")
async def prs2(callback_query: CallbackQuery):
    await callback_query.message.answer("Ви вибрали укулеле")


@dp.message(F.text=="Список пісень")
async def inst(message: Message):
    await message.answer("..........")

@dp.message(F.text=="Пошук акордів")
async def inst(message: Message):
    await message.answer("...........")




async def main ():
   await dp.start_polling(a)


asyncio.run(main())