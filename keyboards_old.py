from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from app.database.requests import get_all_types, get_all_stories, get_all_acts, get_all_plots
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import app.sql as sql

main_text = 'Привет!\n\nЭто бот, в котором можно пройти истории\n\nПриступим?'
main = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [KeyboardButton(text='Поехали')]
])


async def types_2():
    types = await get_types()
    lst = []
    check = []
    for typ in types:
        if typ.type not in check:
            check.append(typ.type)
            lst.append([KeyboardButton(text=typ.type)])
    types_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=lst)
    return types_kb

async def types_all_lst():
    types = await get_all_types()
    lst = []
    for typ in types:
        if typ.type not in lst:
            lst.append(typ.type)
    return lst

async def types_all():

    types = await sql.state_type()
    lst = []
    for typ in types:
        lst.append([KeyboardButton(text=typ[1])])

    #lst.append([KeyboardButton(text='Назад')])
    types_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=lst)
    return types_kb

async def types_dict():
    types = await get_all_types()
    dict = {'Назад':'Back'}
    val = []
    key = []
    for typ in types:
        dict.update({typ.name : typ.stat})
    return dict



async def stories_cho(sost):

    stories = await get_all_stories()
    lst=[]
    for story in stories:
        if story.stat_type == sost:
            lst.append([KeyboardButton(text=story.name)])
    stories_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=lst)
    return stories_kb

async def stories_dict():
    stories = await get_all_stories()
    dict = {'Назад':'Back'}
    val = []
    key = []
    for story in stories:
        dict.update({story.name : story.stat_stories})
    return dict



async def acts_cho(sost):

    acts = await get_all_acts()
    lst=[]
    for act in acts:
        if act.stat_stories == sost:
            lst.append([KeyboardButton(text=act.name)])

    #lst.append([KeyboardButton(text='Назад')])
    acts_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=lst)
    return acts_kb



async def plots_cho(sta):
    plots = await get_all_plots()
    for plot in plots:

        if plot.stat == sta:
            result = plot
    return result

async def acts_dict():
    acts = await get_all_acts()
    dict = {'Назад':'Back'}
    val = []
    key = []
    for act in acts:
        dict.update({act.name : act.stat})
    return dict





async def types():
    types_kb = InlineKeyboardBuilder
    types = await get_types()
    for typ in types:
        types_kb.add(InlineKeyboardButton(text=typ.type, callback_data=f'type_{typ.id}'))
    return types_kb.adjust(2).as_markup()

async def new_sto_bt():
    types_bt = await sql.state_type()
    



menu_2_text= 'В боте есть 2 вида приключений:\n\nИстории - это полноценные приключения с сюжетом\n\nВыживалки - более простые приключения с простым сюжетом\n\nПриступим?'
menu_2 = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='Истории')],[KeyboardButton(text='Выживалки')]])

menu_3_text = 'В какое приключение будем играть:'
