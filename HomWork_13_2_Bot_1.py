import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = ''

# Создаем экземпляр бота
bot = Bot(token=API_TOKEN)

# Создаем диспетчер
dp = Dispatcher(bot)

# Функция, обрабатывающая команду /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.reply('Привет! Я бот помогающий твоему здоровью.')

# Функция, обрабатывающая все остальные сообщения
@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)