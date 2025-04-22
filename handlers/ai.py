from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from services.openai_client import get_openai_response  

router = Router()

@router.message(Command("ai"))
async def ai_handler(message: Message):
    await message.answer("🧠 Как я могу помочь вам с использованием ИИ? Напишите ваш запрос.")
    
@router.message()  
async def handle_ai_request(message: Message):
    user_message = message.text 
    if user_message.lower() != "/ai": 
        ai_response = await get_openai_response(user_message)
        await message.answer(ai_response)
#к сожалению openai у меня не работает просто у меня денег нет))) 