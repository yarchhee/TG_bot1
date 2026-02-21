import requests
import asyncio
from config import Config, load_config, TgBot
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED, MEMBER
from aiogram.types import Message, ChatMemberUpdated, ContentType

config: Config = load_config()
bot_token = config.bot.token

bot = Bot(token=bot_token)

dp = Dispatcher()
def my_help_filter(message: Message) -> bool:
    return message.text and message.text == '\help'

def small_message(message: Message) -> bool:
    return message.text and len(message.text) <= 80

@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("Nice photo")
    # F.photo
    # F.video
    # F.audio
    # F.voice
    # F.document
    # F.sticker
    # F.animation
    # F.contact
    # F.location
ADMIN_IDS = {123,456,789}
@dp.message(F.from_user.id.in_(ADMIN_IDS))  # проверяет принадлежность
async def admin_handler(message: Message):
    await message.answer("Команда для админов")

@dp.message(F.content_type.in_({ContentType.PHOTO, ContentType.VIDEO}))  # проверяет принадлежность
async def media_handler(message: Message):
    await message.answer("медийка тут")

@dp.message(F.text.startswith('Привет'))
async def hello_handler(message: Message):
        await message.answer("Привет")

@dp.message(~F.text.len() < 80)
async def short_message_handler(message: Message):
    await message.answer("wow >= 80")

# @dp.message(Command(commands=["start"], prefix="$"))
@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer("Привет!")

# изменения со стороны пользователя
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated ):
    print(f"Пользователь {event.from_user.id} - {event.from_user.full_name} заблокировал бота")

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def user_unblocked_bot(event: ChatMemberUpdated ):
    print(f"Пользователь {event.from_user.id} - {event.from_user.full_name} разблокировал бота")
# help
@dp.message(my_help_filter)
async def process_help(message: Message):
    await message.answer("Команды:\n/start - Старт \n/help - О боте")

@dp.message(small_message)
async def process_80_cht(message: Message):
    await message.answer(str(len(message.text)))


@dp.message(F.text.len() < 20)
async def process_20_cht(message: Message):
    await message.answer("Коротко и ясно")
@dp.message(F.text.len() >= 20)
async def process_more20_cht(message: Message):
    await message.answer("Много букв но я осилил")
@dp.message()
async def process_nottext(message: Message):
    await message.answer("Не прошло фильтры")


IDs = {53, 456, 789}
@dp.message(Command(commands=['secret']), F.from_user.id.in_(IDs))
async def proc(message: Message):
    await message.answer("Добро пожаловать в бойцовский клуб!")


async def main():
    await dp.start_polling(bot)


if __name__ == 'main':
    asyncio.run(main())

# git clone -b название_ветки ссылка_на_проект
# git checkout - b название_новой_ветки_hw