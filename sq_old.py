import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    #cur.execute("CREATE TABLE IF NOT EXISTS types(type_id TEXT PRIMARY KEY, name TEXT, stat TEXT, next_level TEXT)")

    #cur.execute(
    #    "CREATE TABLE IF NOT EXISTS stories(story_id TEXT PRIMARY KEY, type_stat_old TEXT, name TEXT, stat_sto_next TEXT, next_level TEXT)")

    #cur.execute(
    #    "CREATE TABLE IF NOT EXISTS acts(act_id TEXT PRIMARY KEY, sto_stat_old TEXT, name TEXT, stat_act_next TEXT, next_level TEXT)")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS plots(plot_id TEXT PRIMARY KEY, story TEXT, act TEXT, stat TEXT,  text TEXT, if_attach TEXT, path_attach TEXT, health TEXT, options TEXT, action TEXT)")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(user_id TEXT ,user_level TEXT ,user_stat TEXT, if_to_change TEXT, user_exp TEXT, user_health TEXT,user_choices TEXT, user_others TEXT, user_username TEXT)")

    db.commit()


async def create_user(user_id, username):
    user = cur.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'").fetchone()
    if not user:
        cur.execute(f"INSERT INTO users(user_id, user_level, user_stat, if_to_change, user_exp, user_health, user_choices, user_others, user_username) VALUES('{user_id}', '1','menu_1', 'no', 'null' ,'1', 'null', 'null', '{username}')")
        db.commit()
    else:
        querry = f"UPDATE users SET if_to_change = 'no', user_stat = 'menu_1', if_to_change = 'no', user_health = '1' WHERE user_id='{user_id}'"
        cur.execute(querry)
        db.commit()


async def get_user_info(user_id):
    user = cur.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'").fetchone()
    return user

async def get_plots_info(stat):
    plots = cur.execute(f"SELECT * FROM plots WHERE stat = '{stat}'").fetchone()
    return plots

async def update_stat_to_change(user_id, stat_TC):
    querry = f"UPDATE users SET if_to_change = '{stat_TC}' WHERE user_id = '{user_id}'"
    cur.execute(querry)
    db.commit()
    
async def stat_change(user_id, stat, plot, restext):

    old_buts = plot[8].split('!')
    texts = old_buts[1::2]
    stats_new = old_buts[2::2]
    stat = stats_new[texts.index(restext)]
    querry = f'UPDATE users SET user_stat="{stat}" WHERE user_id = "{user_id}"'
    cur.execute(querry)
    db.commit()
    return stat

async def stat_change_dead(user_id, plot):

    statnw = plot[1]
    querry = f'UPDATE users SET user_stat="{statnw}", if_to_change = "no" WHERE user_id = "{user_id[0]}"'
    cur.execute(querry)
    db.commit()

    







async def state_type():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()


    request = "SELECT * FROM types"
    cur.execute(request)

    return cur.fetchall()
    db.commit()
    db.close()





async def start_plot(ui, pl):
    querry = f"UPDATE users SET user_health = {pl[7]} WHERE user_id = {ui[0]}"
    cur.execute(querry)
    db.commit()


async def health_change(hlh, ui):
    querry = f"UPDATE users SET user_health = {hlh} WHERE user_id = {ui[0]}"
    cur.execute(querry)
    db.commit()
    