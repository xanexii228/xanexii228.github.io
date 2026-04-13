import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Настройки
BOT_TOKEN = "7979368281:AAGddIF9lKwcFXXwgfoLGTMb1aE1VZvB6KI"  # Замените на ваш токен от @BotFather
WEB_APP_URL = "https://xanexii228.github.io/index.html"  # Замените на URL вашего HTML файла

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    # Создаем кнопку для запуска Web App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🚀 Открыть приложение", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    
    await message.answer(
        "👋 Привет! Нажми на кнопку ниже, чтобы открыть веб-приложение:",
        reply_markup=keyboard
    )

# Обработка данных, отправленных через tg.sendData()
@dp.message(lambda message: message.web_app_data is not None)
async def web_app_data_handler(message: types.Message):
    web_app_data = message.web_app_data
    data = json.loads(web_app_data.data)
    
    logging.info(f"Получены данные: {data}")
    
    # Отвечаем пользователю
    await message.answer(
        f"✅ Данные получены!\n\n"
        f"Действие: {data.get('action')}\n"
        f"Время: {data.get('timestamp')}"
    )
    
    # Здесь можно сохранять данные в БД или делать другие действия

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
