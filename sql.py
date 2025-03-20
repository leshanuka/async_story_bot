import  sqlite3  as sq

async def db_start():
    global db, cur

    db = sq.connect("new.db")
    cur = db.cursor()


    cur.execute(
        "CREATE TABLE IF NOT EXISTS plots(plot_id TEXT PRIMARY KEY, story TEXT, act TEXT, stat TEXT,  text TEXT, if_attach TEXT, path_attach TEXT, health TEXT, options TEXT, action TEXT)")

    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(user_id TEXT ,user_level TEXT ,user_stat TEXT, if_to_change TEXT, user_exp TEXT, user_health TEXT,user_choices TEXT, user_others TEXT, user_username TEXT, game_stat TEXT)")

    db.commit()


async def create_user(user_id, username):

    user = cur.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'").fetchone()

    if not user:
        cur.execute(f"INSERT INTO users(user_id, user_level, user_stat, if_to_change, user_exp, user_health, user_choices, user_others, user_username, game_stat) VALUES('{user_id}', '1','menu_1', 'no', 'null' ,'1', 'null', 'null', '{username}', 'null')")
        db.commit()
    else:
        querry = f"UPDATE users SET if_to_change = 'no', user_stat = 'menu_1', if_to_change = 'no', user_health = '1', game_stat = 'null' WHERE user_id='{user_id}'"
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

async def final_change(ui, plot):
    querry_1 = f'SELECT user_others FROM users WHERE user_id = {ui[0]}'
    plstory = cur.execute(querry_1)
    plst = plstory.fetchone()[0].split(', ')
    if plst == None:
        querry = f"UPDATE users SET user_others = menu_1, {plot[1]} WHERE user_id = {ui[0]}"
        cur.execute(querry)

    else:
        if plot[1] not in plst:
            plst.append(plot[1])
            querry = f"UPDATE users SET user_others = '{', '.join(plst)}' WHERE user_id = {ui[0]}"
            cur.execute(querry)

async def game_stat_change(user_id, game):

    querry = f'UPDATE users SET game_stat="{game}" WHERE user_id = "{user_id}"'
    cur.execute(querry)
    db.commit()