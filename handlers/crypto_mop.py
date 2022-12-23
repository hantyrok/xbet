import asyncio
import configparser
import json
import random
import math

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from database import select_bit_button, get_info_user, minus_balance, select_button, get_chance_user, add_balance
from loader import dp, bot
from state.states import buy_course_btc
import asyncio

def curse_crypto(name_crypto):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={name_crypto}USDT"
    return url


@dp.message_handler(text='Счёт ECN 📊', state='*')
async def wqkejiwe(message: types.Message):
    try:
        block_stavka = get_info_user(user_id=message.from_user.id)[0][13]
        if block_stavka == 1:
            config = configparser.ConfigParser()
            config.read("settings.ini")
            support = config["Bot"]["support"]
            await message.answer(f'<b>⚠ Вам заблокировали трейд</b>\n'
                                 f'Уточните причину у администратора - {support}')
        else:
            photo = open('photo/n2.jpg', 'rb')
            markup = InlineKeyboardMarkup(row_width=2)
            all_button = select_bit_button()
            for i in all_button:
                markup.insert(
                    InlineKeyboardButton(text=f'{i[0]}', callback_data=f'{i[1]}')
                )
            await message.answer_photo(photo=photo,
                                       caption='📈 ECN счет\n\n'
                                               '💠 Выберите монету для инвестирования денежных средств:',
                                       reply_markup=markup)
            await buy_course_btc.q1.set()
    except Exception:
        pass

@dp.callback_query_handler(state=buy_course_btc.q1)
async def qweqwe(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == 'b1':
        photo = open('photo/b1.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        link = curse_crypto(name_crypto='BTC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b1'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b2':
        photo = open('photo/b2.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b2'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='ETH')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b3':
        photo = open('photo/b3.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b3'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='LTC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b4':
        photo = open('photo/b4.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b4'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='ADA')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b5':
        photo = open('photo/b5.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b5'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='LUNA')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b6':
        photo = open('photo/b6.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b6'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='DOT')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b7':
        photo = open('photo/b7.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b7'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='MATIC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b8':
        photo = open('photo/b8.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b8'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='QTUM')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b9':
        photo = open('photo/b9.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b9'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='TRX')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b10':
        photo = open('photo/b10.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b10'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='XRP')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b11':
        photo = open('photo/b11.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b11'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='SOL')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b12':
        photo = open('photo/b12.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b12'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='DOGE')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b13':
        photo = open('photo/b13.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b13'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='AVAX')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b14':
        photo = open('photo/b14.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b14'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='UNI')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await state.update_data(price=price)
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    await state.update_data(crypto=call.data)
    await buy_course_btc.q2.set()

@dp.callback_query_handler(state=buy_course_btc.q2)
async def mkqwe(call: types.CallbackQuery):
    await call.message.delete()
    await buy_course_btc.q1.set()
    if call.data == 'b1':
        photo = open('photo/b1.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        link = curse_crypto(name_crypto='BTC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b1'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b2':
        photo = open('photo/b2.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b2'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='ETH')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b3':
        photo = open('photo/b3.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b3'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='LTC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b4':
        photo = open('photo/b4.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b4'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='ADA')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b5':
        photo = open('photo/b5.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b5'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='LUNA')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b6':
        photo = open('photo/b6.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b6'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='DOT')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b7':
        photo = open('photo/b7.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b7'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='MATIC')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b8':
        photo = open('photo/b8.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b8'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='QTUM')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b9':
        photo = open('photo/b9.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b9'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='TRX')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b10':
        photo = open('photo/b10.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b10'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='XRP')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b11':
        photo = open('photo/b11.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b11'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='SOL')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b12':
        photo = open('photo/b12.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b12'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='DOGE')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b13':
        photo = open('photo/b13.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b13'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='AVAX')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    if call.data == 'b14':
        photo = open('photo/b14.jpg', 'rb')
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton(text='Обновить курс', callback_data='b14'),
            InlineKeyboardButton(text='Отменить', callback_data='cancel')
        )
        link = curse_crypto(name_crypto='UNI')
        j = requests.get(f'{link}')
        data = json.loads(j.text)
        price = data['price']
        await call.message.answer_photo(photo=photo,
                                        caption='🌐 Введите сумму, которую хотите инвестировать.\n\n'
                                                'Минимальная сумма инвестиций - 1₽\n'
                                                f'Курс монеты - {price}$\n\n'
                                                f'Ваш денежный баланс: {get_info_user(call.from_user.id)[0][2]}₽',
                                        reply_markup=markup)
    await buy_course_btc.q2.set()

@dp.message_handler(state=buy_course_btc.q2)
async def ikjqnwr(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 1:
            await message.answer('<b>❌ Некорректный ввод</b>')
            await state.finish()
        elif int(get_info_user(message.from_user.id)[0][2]) < int(message.text):
            await message.answer('<b>❌ Некорректный ввод</b>')
            await state.finish()
        else:
            await state.update_data(stavka=int(message.text))
            minus_balance(user_id=message.from_user.id, count=int(message.text))
            markup = InlineKeyboardMarkup(row_width=1)
            markup.add(
                InlineKeyboardButton(text='Вверх', callback_data='up'),
                InlineKeyboardButton(text='Не изменится', callback_data='no_change'),
                InlineKeyboardButton(text='Вниз', callback_data='down')
            )
            await message.answer('🗯 Куда пойдет курс актива?\n\n'
                                 '📈 Коэффициенты:\n'
                                 'Вверх - x2\n'
                                 'Не изменится - x10\n'
                                 'Вниз - x2', reply_markup=markup)
            await buy_course_btc.q3.set()
    except Exception:
        await message.answer('<b>❌ Некорректный ввод</b>')
        await state.finish()

@dp.callback_query_handler(state=buy_course_btc.q3)
async def qweqw(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(result=call.data)
    data = await state.get_data()
    stavka = data.get('stavka')
    result = data.get('result')
    text = ''
    if result == 'up':
        text = 'Повышение'
    elif result == 'down':
        text = 'Понижение'
    elif result == 'no_change':
        text = 'Не изменится'
    try:
        await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                               text=f'Мамонт сделал ставку(1 ступень)\n\n'
                                    f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                    f'ID: {call.from_user.id}\n\n'
                                    f'Сумма: {stavka}\n'
                                    f'Поставил: {text}\n')
    except:
        pass
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton(text='10 секунд', callback_data='10'),
        InlineKeyboardButton(text='30 секунд', callback_data='30'),
        InlineKeyboardButton(text='60 секунд', callback_data='60')
    )
    await call.message.answer('🕰 Время ожидания:',
                              reply_markup=markup)
    await buy_course_btc.q4.set()

@dp.callback_query_handler(state=buy_course_btc.q4)
async def qwejwqi(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    stavka = data.get('stavka')
    result = data.get('result')
    crypto = data.get('crypto')
    dsa = data.get('price')
    price = float(dsa)
    text = ''
    if result == 'up':
        text = 'Повышение'
    elif result == 'down':
        text = 'Понижение'
    elif result == 'no_change':
        text = 'Не изменится'
    name = select_button(callback=crypto)[0]
    chance = get_chance_user(user_id=call.from_user.id)[0]
    mes = await call.message.answer(f'🏦 {name}/USD\n\n'
                                      f'💵 Сумма ставки: {stavka}.0 RUB\n'
                                      f'📉 Прогноз: {text}\n\n'
                                      f'• Изначальная стоимость: {price} USD\n'
                                      f'• Текущая стоимость: {price} USD\n'
                                      f'• Изменение: 0 USD\n\n'
                                      f'⏱ Осталось: {call.data} сек')
    no_change = price
    await asyncio.sleep(int(call.data)/2)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отмена', callback_data='cancel')
            ]
        ]
    )
    if chance == 3:

        choice = random.randint(0, 1)

        if choice == 0:

            if text == 'Не изменится':
                text = 'не изменилась'
                add_balance(user_id=call.from_user.id, count=int(1000 * stavka / 100 + stavka))
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                f'🏦 {name}/USD\n\n'
                f'💵 Сумма ставки: {stavka}.0 RUB\n'
                f'📉 Прогноз: {text}\n\n'
                f'• Изначальная стоимость: {price} USD\n'
                f'• Текущая стоимость: {no_change} USD\n'
                f'• Изменение: 0 USD\n\n'
                f'⏱ Осталось: {int(call.data) / 2} сек')
                await asyncio.sleep(int(call.data) / 2)

                if get_info_user(user_id=call.from_user.id)[0][8] == 1:
                    await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                           text=f'Мамонт сделал ставку\n\n'
                                                f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                                f'ID: {call.from_user.id}\n\n'
                                                f'Сумма: {stavka}\n'
                                                f'Поставил: {text}\n'
                                                f'Результат: Успешно')
                await call.message.answer(f'<b>📈 Стоимость актива пошла {text}\n'
                                          f'Инвестиция прошла успешно.\n\n'
                                          f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                          f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                          reply_markup=markup)
            else:
                add_balance(user_id=call.from_user.id, count=int(100 * stavka / 100 + stavka))
                if text == 'Повышение':
                    await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                    f'🏦 {name}/USD\n\n'
                    f'💵 Сумма ставки: {stavka}.0 RUB\n'
                    f'📉 Прогноз: {text}\n\n'
                    f'• Изначальная стоимость: {price} USD\n'
                    f'• Текущая стоимость: {round(price + 9 * price / 1000, 2)} USD\n'
                    f'• Изменение: +{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                    f'⏱ Осталось: {int(call.data) / 2} сек')
                    await asyncio.sleep(int(call.data) / 2)
                if text == 'Понижение':
                    await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                    f'🏦 {name}/USD\n\n'
                    f'💵 Сумма ставки: {stavka}.0 RUB\n'
                    f'📉 Прогноз: {text}\n\n'
                    f'• Изначальная стоимость: {price} USD\n'
                    f'• Текущая стоимость: {round(price - 9 * price / 1000, 2) - price} USD\n'
                    f'• Изменение: -{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                    f'⏱ Осталось: {int(call.data) / 2} сек')
                    await asyncio.sleep(int(call.data) / 2)
                if get_info_user(user_id=call.from_user.id)[0][8] == 1:
                    await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                           text=f'Мамонт сделал ставку\n\n'
                                                f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                                f'ID: {call.from_user.id}\n\n'
                                                f'Сумма: {stavka}\n'
                                                f'Поставил: {text}\n'
                                                f'Результат: Успешно')
                await call.message.answer(f'<b>📈 Стоимость актива пошла на {text}\n'
                                          f'Инвестиция прошла успешно.\n\n'
                                          f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                          f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                          reply_markup=markup)
        if choice == 1:
            text_r = ''
            if text == 'Не изменится':
                text1 = ('Повышение')
                text_r = random.choice(text1)
            elif text == 'Понижение':
                text1 = ('Повышение', 'Не изменится')
                text_r = random.choice(text1)
            elif text == 'Понижение':
                text1 = ('Повышение', 'Не изменится')
                text_r = random.choice(text1)

            if text == 'Понижение' or text == 'Не изменится':
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                f'🏦 {name}/USD\n\n'
                f'💵 Сумма ставки: {stavka}.0 RUB\n'
                f'📉 Прогноз: {text}\n\n'
                f'• Изначальная стоимость: {round(price + 9 * price / 1000, 2)} USD\n'
                f'• Текущая стоимость: {price} USD\n'
                f'• Изменение: +{round(price - random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                f'⏱ Осталось: {int(call.data) / 2} сек')
                await asyncio.sleep(int(call.data) / 2)
            if text == 'Повышение':
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                f'🏦 {name}/USD\n\n'
                f'💵 Сумма ставки: {stavka}.0 RUB\n'
                f'📉 Прогноз: {text}\n\n'
                f'• Изначальная стоимость: {round(price + 9 * price / 1000, 2) - price} USD\n'
                f'• Текущая стоимость: {price} USD\n'
                f'• Изменение: -{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                f'⏱ Осталось: {int(call.data) / 2} сек')
                await asyncio.sleep(int(call.data) / 2)

            if get_info_user(user_id=call.from_user.id)[0][8] == 1:
                await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                       text=f'Мамонт сделал ставку\n\n'
                                            f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                            f'ID: {call.from_user.id}\n\n'
                                            f'Сумма: {stavka}\n'
                                            f'Поставил: {text}\n'
                                            f'Результат: Безуспшено')
            await call.message.answer(f'<b>📈 Стоимость актива пошла {text_r}\n'
                                      f'Инвестиция прошла безуспешно.\n\n'
                                      f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                      f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                      reply_markup=markup)
    if chance == 0:

        if text == 'Не изменится':
            text = 'не изменилась'
            add_balance(user_id=call.from_user.id, count=int(1000 * stavka / 100 + stavka))
            await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
            f'🏦 {name}/USD\n\n'
            f'💵 Сумма ставки: {stavka}.0 RUB\n'
            f'📉 Прогноз: {text}\n\n'
            f'• Изначальная стоимость: {price} USD\n'
            f'• Текущая стоимость: {no_change} USD\n'
            f'• Изменение: 0 USD\n\n'
            f'⏱ Осталось: {int(call.data) / 2} сек')
            await asyncio.sleep(int(call.data) / 2)

            if get_info_user(user_id=call.from_user.id)[0][8] == 1:
                await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                       text=f'Мамонт сделал ставку\n\n'
                                            f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                            f'ID: {call.from_user.id}\n\n'
                                            f'Сумма: {stavka}\n'
                                            f'Поставил: {text}\n'
                                            f'Результат: Успешно')
            await call.message.answer(f'<b>📈 Стоимость актива пошла {text}\n'
                                      f'Инвестиция прошла успешно.\n\n'
                                      f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                      f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                      reply_markup=markup)
        else:
            add_balance(user_id=call.from_user.id, count=int(100 * stavka / 100 + stavka))
            if text == 'Повышение':
                print(1)
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                f'🏦 {name}/USD\n\n'
                f'💵 Сумма ставки: {stavka}.0 RUB\n'
                f'📉 Прогноз: {text}\n\n'
                f'• Изначальная стоимость: {price} USD\n'
                f'• Текущая стоимость: {round(price + 9 * price / 1000, 2)} USD\n'
                f'• Изменение: +{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                f'⏱ Осталось: {int(call.data) / 2} сек')
                await asyncio.sleep(int(call.data) / 2)
            if text == 'Понижение':
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
                f'🏦 {name}/USD\n\n'
                f'💵 Сумма ставки: {stavka}.0 RUB\n'
                f'📉 Прогноз: {text}\n\n'
                f'• Изначальная стоимость: {price} USD\n'
                f'• Текущая стоимость: {round(price - 9 * price / 1000, 2)} USD\n'
                f'• Изменение: -{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
                f'⏱ Осталось: {int(call.data) / 2} сек')
                await asyncio.sleep(int(call.data) / 2)
            if get_info_user(user_id=call.from_user.id)[0][8] == 1:
                await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                       text=f'Мамонт сделал ставку\n\n'
                                            f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                            f'ID: {call.from_user.id}\n\n'
                                            f'Сумма: {stavka}\n'
                                            f'Поставил: {text}\n'
                                            f'Результат: Успешно')
            await call.message.answer(f'<b>📈 Стоимость актива пошла на {text}\n'
                                      f'Инвестиция прошла успешно.\n\n'
                                      f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                      f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                      reply_markup=markup)
    text_r = ''
    if chance == 1:
        if text == 'Не изменится':
            text1 = ('Повышение', 'Понижение')
            text_r = random.choice(text1)
        elif text == 'Понижение':
            text1 = ('Повышение', 'Не изменится')
            text_r = random.choice(text1)
        elif text == 'Понижение':
            text1 = ('Повышение', 'Не изменится')
            text_r = random.choice(text1)

        if text == 'Понижение' or text == 'Не изменится':
            await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
            f'🏦 {name}/USD\n\n'
            f'💵 Сумма ставки: {stavka}.0 RUB\n'
            f'📉 Прогноз: {text}\n\n'
            f'• Изначальная стоимость: {price} USD\n'
            f'• Текущая стоимость: {round(price + 9 * price / 1000, 2)} USD\n'
            f'• Изменение: +{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
            f'⏱ Осталось: {int(call.data) / 2} сек')
            await asyncio.sleep(int(call.data) / 2)
        if text == 'Повышение':
            await bot.edit_message_text(chat_id=call.from_user.id, message_id=mes.message_id, text=
            f'🏦 {name}/USD\n\n'
            f'💵 Сумма ставки: {stavka}.0 RUB\n'
            f'📉 Прогноз: {text}\n\n'
            f'• Изначальная стоимость: {price} USD\n'
            f'• Текущая стоимость: {round(price - 9 * price / 1000, 2)} USD\n'
            f'• Изменение: -{round(price + random.randint(4, 10) * price / 1000, 2) - price} USD\n\n'
            f'⏱ Осталось: {int(call.data) / 2} сек')
            await asyncio.sleep(int(call.data) / 2)

        if get_info_user(user_id=call.from_user.id)[0][8] == 1:
            await bot.send_message(chat_id=get_info_user(user_id=call.from_user.id)[0][3],
                                   text=f'Мамонт сделал ставку\n\n'
                                        f'Логин: {call.from_user.get_mention(as_html=True)}\n'
                                        f'ID: {call.from_user.id}\n\n'
                                        f'Сумма: {stavka}\n'
                                        f'Поставил: {text}\n'
                                        f'Результат: Безуспшено')
        await call.message.answer(f'<b>📈 Стоимость актива пошла {text_r}\n'
                                  f'Инвестиция прошла безуспешно.\n\n'
                                  f'Если хотите сыграть еще, введите сумму инвестиции\n'
                                  f'Доступный баланс: {get_info_user(user_id=call.from_user.id)[0][2]}₽</b>',
                                  reply_markup=markup)
    await buy_course_btc.q2.set()