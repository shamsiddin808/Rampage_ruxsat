from aiogram.dispatcher.filters.state import StatesGroup, State


class Rampage(StatesGroup):
    time = State()