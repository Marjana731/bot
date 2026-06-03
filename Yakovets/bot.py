import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


bot = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()

class RegistrationStates(StatesGroup):
    name = State()
    email = State()
    age = State()
    tel = State()


@dp.message(F.text=="/start")
async def start(message: Message):
    await message.answer("Привіт")

@dp.message(F.text=="/morning")
async def morning(message: Message):
    await message.answer("Добрий ранок")

@dp.message(F.text=="/sad")
async def sad(message: Message):
    await message.answer("Все буде добре")

@dp.message(F.text=="/happy")
async def happy(message: Message):
    await message.answer("Радий за тебе")

@dp.message(F.text=="/goodbye")
async def goodbye(message: Message):
    await message.answer("До зустрічі")

@dp.message(F.text=="привіт")
async def hello(message: Message):
    await message.answer("привіт")

@dp.message(F.text=="як справи")
async def a(message: Message):
    await message.answer("норм")

@dp.message(F.text=="register")
async def register(message: Message, state: FSMContext):
    await message.answer("Введіть ваше ім'я")
    await state.set_state(RegistrationStates.name)

async def main():
    await dp.start_polling(bot, skip_update=True)


if __name__ == "__main__":
    print("Бот запускається...")
    asyncio.run(main())
    print("Бот зупинено.")



