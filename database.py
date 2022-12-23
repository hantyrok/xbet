import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('db.db')
    return __connection

def new_user(user_id, name, fullname):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users (user_id, name, fullname) VALUES (?, ?, ?)', (user_id, name, fullname))
    conn.commit()

def get_info_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchall()

def get_all_info_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE refer=(?)', (user_id,))
    return c.fetchall()

def update_rules(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET rules=1 WHERE user_id=(?)', (user_id,))
    conn.commit()

def select_worker(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT worker FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def select_bit_button():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM b_button')
    return c.fetchall()

def select_min_dep(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT min_dep FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def info_trade():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT text FROM info WHERE type=(?)', ('trade',))
    return c.fetchone()

def info_trade_update(text):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE info SET text=(?) WHERE type=(?)', (text, 'trade'))
    conn.commit()

def qiwi_token():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT khm FROM payments WHERE type=(?)', ('qiwi',))
    return c.fetchone()

def btc_adres():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT khm FROM payments WHERE type=(?)', ('btc',))
    return c.fetchone()

def update_payments(tap, fap):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE payments SET khm = ? WHERE type = ?',(tap,fap))
    conn.commit()

def update_min_dep1(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET min_dep=(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def add_balance(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance+(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def minus_balance(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance-(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def select_button(callback):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT Button FROM b_button WHERE callback=(?)', (callback,))
    return c.fetchone()

def get_chance_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT chance FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def add_worker(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET worker=+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

def on_ved(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET uved=1 WHERE refer=(?)', (user_id,))
    conn.commit()

def off_ved(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET uved=0 WHERE refer=(?)', (user_id,))
    conn.commit()

def get_referral(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT refer FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def new_referral(referral, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET refer=(?) WHERE user_id=(?)', (referral, user_id))
    conn.commit()

def add_count_ref(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET count_ref=count_ref + 1 WHERE user_id=(?)', (user_id,))
    conn.commit()

def update_min_dep(count, refer):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET min_dep=(?) WHERE refer=(?)', (count, refer))
    conn.commit()

def get_all_refer(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE refer=(?)', (user_id,))
    return c.fetchall()

def new_promo(user_id, promo, price):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO all_promo (user_id, promo, price) VALUES (?, ?, ?)', (user_id, promo, price))
    conn.commit()

def get_all_promo(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM all_promo WHERE user_id=(?)', (user_id,))
    return c.fetchall()

def get_all_promo_no_user():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM all_promo')
    return c.fetchall()

def plus_disable_promo(promo):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE all_promo SET active=1 WHERE promo=(?)', (promo,))
    conn.commit()

def update_balance(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def win_or_lose_stavka(chance, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET chance=(?) WHERE user_id=(?)', (chance, user_id))
    conn.commit()

def on_or_off_verif(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET verif=(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def on_or_off_without(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET withdraw=(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def delete_mamont(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET refer="n" WHERE user_id=(?)', (user_id,))
    conn.commit()

def get_all_user():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(user_id) FROM users')
    return c.fetchone()

def get_all_workers():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(user_id) FROM users WHERE worker=1')
    return c.fetchone()

def get_all_mamonts():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(user_id) FROM users WHERE worker=0')
    return c.fetchone()

def get_all_user_id():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT user_id FROM users')
    return c.fetchall()

def update_stavka(count, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET stavka=(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

def language_change(lang, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET language=(?) WHERE user_id=(?)', (lang, user_id))
    conn.commit()

def get_lang_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT language FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def get_deposit_pro(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET deposit_pro=1 WHERE user_id=(?)', (user_id,))
    conn.commit()

def select_deposit_pro(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET deposit_pro=0 WHERE user_id=(?)', (user_id,))
    conn.commit()

def dep_pro(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT deposit_pro FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def get_refes(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT refer FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def get_procent_worker():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT procent FROM procent_worker')
    return c.fetchone()

def update_proc(count):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE procent_worker SET procent=(?)', (count,))
    conn.commit()

def select_worker_count(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT worker FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

def update_worker(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET worker=1 WHERE user_id=(?)', (user_id,))
    conn.commit()

def update_worke1r(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET worker=1 WHERE user_id=(?)', (user_id,))
    conn.commit()

