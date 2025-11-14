import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ContentType

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def handler_start(message: types.Message):
    await message.answer("Привет! Я бот для обработки PDF-счетов. Жду файл или команду.")

@dp.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def handle_pdf_document(message: types.Message):
    await message.answer("PDF-файл получен (обработка будет добавлена после готовности backend).")

@dp.message()
async def echo_any(message: types.Message):
    await message.answer("Пока я умею только отвечать на /start и принимать сообщения!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
