import os

from pytube import YouTube
from aiogram import types,Dispatcher,Bot,executor

bot = Bot(token="**********************************************")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
   chat_id = message.chat.id
   await bot.send_message(chat_id, f'Привет, {message.from_user.first_name} \nТут вы можете скачать видео с YouTube \nЧто-бы скачать отправьте ссылку на видео')

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    link1 = 'https://youtu.be/'
    link2 = 'https://www.youtube.com/'
    if message.text.startswith == link1 or link2:
       await bot.send_message(chat_id, f"*Начало загрузки* : *{yt.title}*\n"
                                       f"*С канала* : [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
       await download_youtube_video(url, message, bot)


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}',f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}','rb') as video:
       await bot.send_video(message.chat.id, video, caption='*Ваше видео готово!*', parse_mode="Markdown")
       os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")

if __name__ == '__main__':
    #executor.start_polling(dp)
    executor.start_polling(dp)



