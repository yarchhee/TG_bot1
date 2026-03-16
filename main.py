from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message
from requests import get
from random import choice
from aiogram import F
import os
# dp.run_polling()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # async def get_photo(message: Message, bot: Bot):
    #     print(f"[LOG] Пользователь {message.from_user.id} вызвал get_photo")
    #     photo = message.photo[-1]
    #     file = await bot.get_file(photo.file_id)
    #     print(f"[LOG] получение файла {file.file_unique_id}")
    #     PATH = os.path.join("file", f"{file.file_unique_id}.jpg")
    #     await bot.download_file(file.file_path, destination = "files/file1.jpg")
    #     print(f"[LOG] сохранение файла {PATH}")
    #     await message.answer("Крутое фото!")
    #
    # @dp.message(F.video)
    # async def get_video(message: Message, bot: Bot):
    #     print(f"[LOG] Пользователь {message.from_user.id} вызвал get_photo")
    #     video = message.video[-1]
    #     file = await bot.get_file(video.file_id)
    #     print(f"[LOG] получение файла {file.file_unique_id}")
    #     PATH = os.path.join("file", f"{file.file_unique_id}.mp4")
    #     await bot.download_file(file.file_path, destination=PATH)
    #     print(f"[LOG] сохранение файла {PATH}")
    #     await message.answer("Крутое видео!")

    @dp.message(F.photo | F.video)
    async def get_photo(message: Message):
        os.makedirs("downloads", exist_ok=True)

        if message.photo:
            file = await bot.get_file(message.photo[-1].file_id)
            PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")
        else:
            file = await bot.get_file(message.video.file_id)
            PATH = os.path.join("downloads", f"{file.file_unique_id}.mp4")
        await bot.download_file(file.file_path, destination = PATH)
        await message.answer("Крутое фото или видео")


print(f"[LOG] Бот запущен.")
run(main()) # запускает цикл событий