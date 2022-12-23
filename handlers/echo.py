from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types

@dp.message_handler(state='*')
async def qwewqe(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('❌ Некорректный ввод')
