from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton, BotCommand
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Эта команда начинает бот"),
        BotCommand(command="/help", description='Эта команда помогает'),
        BotCommand(command='/neperejivay', description='эта команда чилит')
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await set_commands(bot)

    knopka_1 = KeyboardButton(text = 'Команда 1')
    knopka_2 = KeyboardButton(text = "Команда 2")
    knopka_3 = KeyboardButton(text = "Команда 3")
    knopka_4 = KeyboardButton(text = "Команда 4")
    keyboard =  ReplyKeyboardMarkup(
        keyboard = [[knopka_1],[knopka_2, knopka_3],[knopka_4] ], # передаем кнопки / формируем клавиатуру
        resize_keyboard=True, # чтобы сжать кнопки до размеров текста
    )

    @dp.message(Command(commands = 'start'))
    async def command_start(message: Message):
        await message.answer(
            text = "вот",
            reply_markup = keyboard
        )

    @dp.message(F.text == "Команда 1")
    async def command(message: Message):
        await message.answer(
            text = "ты выбрал первую команду",
            reply_markup = keyboard
        )

    @dp.message(F.text == "Команда 2")
    async def command2(message: Message):
        await message.answer(
                text="ты выбрал вторую команду",
                reply_markup=keyboard
            )
    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
# if name == '__main__':
run(main()) # запускает цикла событий(dispatcher)