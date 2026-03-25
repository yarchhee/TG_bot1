from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove
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

    knopka_1 = KeyboardButton(text = 'Заказать еду')
    knopka_2 = KeyboardButton(text = 'Пицца')
    knopka_3 = KeyboardButton(text = "Суши")
    knopka_4 = KeyboardButton(text = "Назад")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[knopka_1]],  # Передаем туда кнопки, формируем клавиатуру
        resize_keyboard=True,  # сжалась кнопка до высоты текста и ширины экрана телефона
        input_field_placeholder="Клавиатура есть в плейсходлере ..."
    )
    keyboard_2 = ReplyKeyboardMarkup(
        keyboard = [[knopka_2], [knopka_3], [knopka_4]],
        resize_keyboard=True,
    )

    @dp.message(Command(commands=['start']))
    async def start(message: Message):
        await message.answer(
            text = "Вот бот",
            reply_markup=keyboard
        )

    @dp.message(F.text == "Заказать еду")
    async def zakazat(message: Message):
        await message.answer(text = 'Выбирай',
            reply_markup = keyboard_2
        )

    @dp.message(F.text == "Пицца")
    async def pizza(message: Message):
        await message.answer_photo(photo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIlg5ZsLdACP_BM5qEPoLV5n_W06XozzL1zg&s')
    @dp.message(F.text == "Суши")
    async def sushi(message: Message):
        await message.answer_photo(photo = 'https://sushiwok.ru/img/5717b143e944ea4ea04cff6c1112a584')

    @dp.message(F.text == "Назад")
    async def nazad(message: Message):
        await start(message)

    # @dp.message(F.text == 'Команда 1')
    # async def com1_handler(message: Message):
    #     print(message.contact.phone_number)
    #     await message.answer(
    #         text = "Вот команда 1",
    #         reply_markup=ReplyKeyboardRemove()
    #     )
    #
    # @dp.message(F.contact)
    # async def get_contacts(message: Message):
    #     data = message.contact.phone_number
    #     print(data)
    #
    #
    # @dp.message(F.location)
    # async def loc_handler(message: Message):
    #     loc_1 = message.location.latitude
    #     loc_2 = message.location.longitude
    #     print(loc_1, loc_2)
    #
    # @dp.message(F.text == "Команда 2")
    # async def com2_handler(message: Message):
    #     print(message.contact.location)
    #     await message.answer('Ваши данные успешно украдены')



    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
# if name == '__main__':
run(main()) # запускает цикла событий(dispatcher)