import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6737307475:AAGeYrikXp7JEYWohxc8zBL65i-6RUrzXCI")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    mes = 'Привет!\nСейчас мы находимся на этапе закрытого тестирования!\nНажми на кнопку ниже,если хочешь присоедениться к нему!'
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Я хочу!",
        url='https://forms.yandex.ru/u/65a6e3c473cee71bfbc91fac/')
    )
    builder.add(types.InlineKeyboardButton(
        text="Я с вами!",
        callback_data='done')
    )
    await message.answer(mes, reply_markup=builder.as_markup())


@dp.callback_query(F.data == "done")
async def send_random_value(callback: types.CallbackQuery):
    ans = 'Супер!Спасибо за проявлянный интерес!\nНе останавливай меня,я напишу тебе когда откроется бета-тестирование.'
    await callback.message.answer(ans)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())