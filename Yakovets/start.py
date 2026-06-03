import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import  Message

a = Bot(token="8958110452:AAFz1pbTyQFg3a4Nem4h6Sd7LoMPQRoWpuM")
dp = Dispatcher()

async def main ():
   await dp.start_polling(a)


asyncio.run(main())
