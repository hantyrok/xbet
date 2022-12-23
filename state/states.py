from aiogram.dispatcher.filters.state import StatesGroup, State


class deposit_qiwi(StatesGroup):
    q1 = State()
    q2 = State()

class withdraw_money(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()

class buy_course_btc(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()

class new_min_dep(StatesGroup):
    q1 = State()

class add_refer_id(StatesGroup):
    q1 = State()

class Create_promo(StatesGroup):
    q1 = State()

class Enter_promo(StatesGroup):
    q1 = State()

class Info_on_my_mamont(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()

class Mailing_message(StatesGroup):
    q1 = State()

class Message_mamount(StatesGroup):
    q1 = State()

class Choice_language(StatesGroup):
    q1 = State()

class new_proc_wokr(StatesGroup):
    q1 = State()

class Pencilsad(StatesGroup):
    q1 = State()
    
class InfoText(StatesGroup):
    q1 = State()
    
class SetPayments(StatesGroup):
    q1 = State()