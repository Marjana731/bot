import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


bot = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()
router = Router()

class RegistrationStates(StatesGroup):
    city = State()
    name = State()
    tel = State()


@dp.message(F.text=="/text")
async def cmd_register(message: Message, state: FSMContext):
    await message.answer("Привіт! Давайте зареєструємо вас.\nБудь ласка, введіть ваше місто:")
    await state.set_state(RegistrationStates.city)

@router.message(RegistrationStates.city)
async def process_city(message: Message, state: FSMContext):
    print(1)
    if not message.text or len(message.text) < 2:
        await message.answer("Будь ласка, введіть дійсне місто (мінімум 2 символи).")
        return
    await state.update_data(city=message.text)
    user_data = await state.get_data()

    await message.answer(
        f"Реєстрація завершена! Ваші дані:\n"
        f"місто: {user_data.get('city')}\n"
    )
    await state.clear()


@dp.message(F.text=="/start")
async def start(message: Message):
    await message.answer("Привіт")

@dp.message(F.text=="привіт")
async def hello(message: Message):
    await message.answer("Привіт")

@router.message(F.text)
async def debug(msg : Message, st: FSMContext):
    print( await st.get_state())

async def main():
    dp.include_router(router)
    await dp.start_polling(bot, skip_update=True)

if __name__ == "__main__":
    print("Бот запускається...")
    asyncio.run(main())
    print("Бот зупинено.")