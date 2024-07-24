from collections import defaultdict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import main_btn
from keyboards.inline.inline import admin_check_ruxsat
from states.state import *
from data.config import ADMINS

from loader import dp, bot

fake_data = defaultdict(dict)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}\nKampyuterga tuwiw uchun ruxsat botiga hush kelibsiz",
                         reply_markup=main_btn)
    fake_data[message.from_user.full_name]['user_name'] = message.from_user.full_name


@dp.message_handler(text="ruxsat sorash")
async def ruxsat_sorash(message: types.Message):
    await message.answer("Nechida tuwmoqchisiz\n\nMasalan: 14:00")
    await Rampage.time.set()


@dp.message_handler(content_types=["text"], state=Rampage.time)
async def handle_rampage_time(message: types.Message, state: FSMContext):
    global user_id
    fake_data[message.from_user.id]['rampage_vaqt'] = message.text

    await bot.send_message(259083453, f"Sizdan shu vaqt uchun - {message.text}\n"
                                      f"Bu foydalanuvchi ruxsat so'radingiz - @{message.from_user.username}",
                           reply_markup=admin_check_ruxsat)
    await message.answer("Sorov Yuborildi javobni kuting")
    user_id = message.from_user.id
    await state.finish()

from aiogram import types


@dp.callback_query_handler(text="ha_ruxsat")
async def process_callback_ha_ruxsat(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.bot.send_message(user_id, "Sizga ruxsat berildi ✅")


from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="yoq_ruxsat")
async def handle_yoo_ruxsat_callback(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.bot.send_message(user_id, "Sizga ruxsat yoq ❌")
