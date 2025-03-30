import asyncio import logging from datetime import datetime, timedelta from aiogram import Bot, Dispatcher, types from aiogram.types import ReplyKeyboardMarkup, KeyboardButton from aiogram.fsm.state import State, StatesGroup from aiogram.fsm.storage.memory import MemoryStorage from aiogram.fsm.context import FSMContext from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "8070823925:AAHCI22gXmHzp8JDm8V9hHYkpSqg8_OLQgc" bot = Bot(token=TOKEN) dp = Dispatcher(storage=MemoryStorage()) scheduler = AsyncIOScheduler() users = {}

class AntiFap(StatesGroup): choosing_gender = State() choosing_days = State()

def get_days_left(start_date, end_date): now = datetime.now().date() passed = (now - start_date).days left = (end_date - now).days return passed, left

@dp.message(lambda message: message.text == "/start") async def start(message: types.Message, state: FSMContext): kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton("!male!"), KeyboardButton("!female!")]], resize_keyboard=True) await state.set_state(AntiFap.choosing_gender) await message.answer("Выбери свой пол:", reply_markup=kb)

@dp.message(AntiFap.choosing_gender) async def set_gender(message: types.Message, state: FSMContext): gender = message.text if gender not in ["!male!", "!female!"]: return await message.answer("Выбери пол кнопкой!") await state.update_data(gender=gender) await state.set_state(AntiFap.choosing_days) await message.answer("Напиши дату окончания в формате ДД.ММ.ГГГГ")

@dp.message(AntiFap.choosing_days) async def set_days(message: types.Message, state: FSMContext): try: end_date = datetime.strptime(message.text, "%d.%m.%Y").date() start_date = datetime.now().date() if end_date <= start_date: return await message.answer("Дата должна быть в будущем!") users[message.from_user.id] = (start_date, end_date) await state.clear() passed, left = get_days_left(start_date, end_date) await message.answer(f"Ты не дрочишь {passed} дней! Тебе осталось терпеть: {left} дней!") except ValueError: await message.answer("Неверный формат! Напиши дату в формате ДД.ММ.ГГГГ")
def daily_check(): for user_id, (start_date, end_date) in users.items(): passed, left = get_days_left(start_date, end_date) asyncio.create_task(bot.send_message(user_id, f"Ты не дрочишь {passed} дней! Тебе осталось терпеть: {left} дней!"))
async def main(): logging.basicConfig(level=logging.INFO) scheduler.add_job(daily_check, "cron", hour=9)  # Сообщение раз в день в 9 утра scheduler.start() await dp.start_polling(bot)
if name == "main": asyncio.run(main())

