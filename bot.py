from  aiogram import Bot ,Dispatcher
import asyncio

from aiogram.types import  Message

TOKEN = ''
dp =Dispatcher()

@dp.massage()
async def index(message: Message)-> None:
    await  message.answer(text='Принял')


async def main():
    bot = Bot(token=TOKEN)
    dp.run_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())

