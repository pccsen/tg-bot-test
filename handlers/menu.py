from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.reply import confirm_keyboard, contact_keyboard
from keyboards.inline import confirm_data_keyboard, thank_you_keyboard 
from handlers.states import Form  


ParseMode = "HTML"
router = Router()

#start Реплай батн да и нет 
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Здравствуйте! 👋 Спасибо, что обратились в нашу школу английского языка. "
        "Подскажите, пожалуйста, вы интересуетесь пробным занятием? 📚",
        parse_mode=ParseMode,
        reply_markup=confirm_keyboard  
    )
    await state.set_state(Form.waiting_for_interest)
        
#if/else точный ответ ДА
@router.message(Form.waiting_for_interest)
async def process_interest(message: Message, state: FSMContext):
    user_input = message.text.lower()
    if any(word in user_input for word in ['да', 'yes']):
        await message.answer(
            "Отлично! 🎉 Чтобы подобрать для вас подходящую группу или преподавателя, "
            "подскажите, пожалуйста, какой у вас сейчас уровень английского? "
            "Какие цели вы ставите перед собой? (например, для учебы, работы, путешествий и т.д.) 🌍"
        )
        await state.set_state(Form.waiting_for_level)
    else:
        await message.answer(
            "Если передумаете, всегда можете вернуться к нам для записи на пробное занятие. 😊"
        )
        await state.clear()

#reply_buttpn да или нет точный ответ да
@router.message(Form.waiting_for_level)
async def process_level_and_goal(message: Message, state: FSMContext):
    level_goal = message.text
    await state.update_data(level_goal=level_goal)
    await message.answer(
        "Мы предлагаем бесплатное пробное занятие, чтобы вы могли познакомиться с нашим форматом и преподавателем. "
        "Занятие длится 40 минут и проходит онлайн/офлайн. Вы готовы записаться? 📝",
        reply_markup=confirm_keyboard
    )
    await state.set_state(Form.waiting_for_confirmation)

#отправить номер телефона reply_button
@router.message(Form.waiting_for_confirmation)
async def process_confirmation(message: Message, state: FSMContext):
    user_input = message.text.lower()
    if any(word in user_input for word in ['да', 'yes']):
        await message.answer(
            "Я записала вас на пробное занятие. 🎉 Могу я уточнить ваше имя и номер телефона для подтверждения и отправки напоминания? 📲",
            reply_markup=contact_keyboard
        )
        await state.set_state(Form.waiting_for_name_and_phone)
    else:
        await message.answer("Если передумаете, мы всегда готовы предложить пробное занятие. 😌")
        await state.clear()


@router.message(Form.waiting_for_name_and_phone)
async def process_name_and_phone(message: Message, state: FSMContext):
    if message.contact:
        contact_info = {
            "phone_number": message.contact.phone_number,
            "first_name": message.contact.first_name,
            "user_id": message.contact.user_id,
        }
        await state.update_data(contact_info=contact_info)
        await message.answer(
            "Спасибо! Вы успешно отправили контакт ✅",
            reply_markup=confirm_data_keyboard
        )
        await state.clear()
    else:
        await message.answer("Пожалуйста, нажмите кнопку ниже, чтобы отправить номер телефона 📲.")


@router.message(StateFilter(None))
async def fallback_handler(message: Message):
    return


@router.callback_query(F.data == "confirm_data")
async def on_confirm_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Спасибо! Мы свяжемся с вами для подтверждения записи. 🙏")
    await callback.message.answer("Мы благодарим вас за заявку! 🎉", reply_markup=thank_you_keyboard)  
    await state.clear()

@router.callback_query(F.data == "edit_data")
async def on_edit_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Хорошо, напишите, пожалуйста, имя и номер телефона ещё раз. ✍️")
    await state.set_state(Form.waiting_for_name_and_phone)
