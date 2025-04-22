import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from handlers import menu, ai

API_TOKEN = "8150201468:AAFAd8oavlHRItERZsb4pvn5ZB4owCBYono"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

 #хендлерлергой
    dp.include_routers(
        menu.router,
        ai.router
    )

#менюгой /menu /ai любой нарсе салуга болады
    await bot.set_my_commands([
        BotCommand(command="menu", description="📋 Меню"),
        BotCommand(command="ai", description="🧠 Запросить помощь ИИ")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
