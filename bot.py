from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram import types
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


# def square(num):
#    return num ** 2


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("LessGoooo!!!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС", callback_data="button_1")
    markup.add(button_1)
    question = 'сколько океанов в мире?'
    answer = [
        '5',
        '8',
        '4',
        '12']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Их 4: Атлантический, Индийский, Тихий, Северный Ледовитый',
        reply_markup=markup)


@dp.callback_query_handler()
async def quiz_2(call: types.CallbackQuery):
    question = 'сколько на планете материков?'
    answer = [
        '2',
        '96',
        'Я футбол не смотрю',
        '6']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Ну ты тупой конечно')


@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://thelaughingotter.com/wp-content/uploads/2023/02/cats-funny-cats-funny-cat-memes-animals-animal-memes-funny-animal-memes-wholesome-cute-animal-memes-wey3wJ.png')

    # await bot.send_message(chat_id=message.from_user.id, text=message.text)


@dp.message_handler()
async def square(message: types.Message):
    if message.text is int:
     num= message.text
     square = num ** 2
    if num <= 0:
        await bot.send_message(chat_id=message.from_user.id, text='wrong number')
    elif num > 0:
        await bot.send_message(chat_id=message.from_user.id, text=f'{int(square)}')
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)