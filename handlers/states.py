from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    waiting_for_interest = State()
    waiting_for_level = State()
    waiting_for_confirmation = State()
    waiting_for_name_and_phone = State()