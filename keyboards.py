from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from requests import get_all_types, get_all_stories, get_all_acts, get_all_plots
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import sql as sql


async def form_keyboard(pi):
    buts = pi[8].split('!')
    numering = pi[8].split('!')[0]
    buts_only = buts[1::2]
    lst = []
    if numering == '1':
        for but in buts_only:
            if but != '':
                lst.append([KeyboardButton(text=but)])
        return lst
    else:
        i = 0
        for n in numering:
            lst_in = []
            for d in range(int(n)):
                lst_in.append(KeyboardButton(text=buts_only[i]))

                i = i + 1
            lst.append(lst_in)
        return lst








async def types_all():

    types = await sql.state_type()
    lst = []
    for typ in types:
        lst.append([KeyboardButton(text=typ[1])])

    #lst.append([KeyboardButton(text='Назад')])
    types_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=lst)
    return types_kb

menu_2_text= 'В боте есть 2 вида приключений:\n\nИстории - это полноценные приключения с сюжетом\n\nВыживалки - более простые приключения с простым сюжетом\n\nПриступим?'
menu_2 = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='Истории')],[KeyboardButton(text='Выживалки')]])

menu_3_text = 'В какое приключение будем играть:'

main_text = 'Привет!\n\nЭто бот, в котором можно пройти разнообразные квесты и похихикать\n\nПрежде чем мы приступим, подтверди, что тебе больше 18 лет. Так вышло, что в историях могут содержаться элементы, которые лучше не показывать детям (ничего криминального, просто маты...). \n\nP.S. Все в боте - всего лишь шутка, ненамеренная кого-то обижать или оскорблять'
main = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [KeyboardButton(text='Мне есть 18')]
])

main_text_olduser = 'Привет!\n\nЭто бот, в котором можно пройти разнообразные квесты и похихикать\n\nВсе в боте - всего лишь шутка, ненамеренная кого-то обижать или оскорблять'


main_olduser = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [KeyboardButton(text='Далее')]
])


async def send_message(user_info, message_user_id, plots_info, message, health_bar):
    await sql.update_stat_to_change(user_id=message_user_id, stat_TC='yes')

    if plots_info[9] == 'final':
        await sql.final_change(ui=user_info, plot=plots_info)

    if plots_info[5] == 'no':
        mestext = plots_info[4]
        if plots_info[9] == 'story':
            mestext = mestext + f"\n\nЗдоровье: {'❤️' * health_bar}"

        await message.answer(mestext, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                                       keyboard=await form_keyboard(
                                                                           plots_info)), parse_mode='html')
    if plots_info[5] == 'photo':
        photo = plots_info[6]
        mestext = plots_info[4]
        if plots_info[9] == 'story':
            mestext = mestext + f"\n\nЗдоровье: {'❤️' * health_bar}"
        await message.answer_photo(photo=photo, caption=mestext,
                                   reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                                    keyboard=await form_keyboard(
                                                                        plots_info)), parse_mode='html')
    if plots_info[5] == 'track':
        audio = plots_info[6]
        mestext = plots_info[4]
        if plots_info[9] == 'story':
            mestext = mestext + f"\n\nЗдоровье: {'❤️' * health_bar}"
        await message.answer_audio(audio=audio, caption=mestext,
                                   reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                                    keyboard=await form_keyboard(
                                                                        plots_info)),
                                   parse_mode='html')

    if plots_info[5] == 'video':
        video = plots_info[6]
        mestext = plots_info[4]

        if plots_info[9] == 'story':
            mestext = mestext + f"\n\nЗдоровье: {'❤️' * health_bar}"
        await message.answer_video(video=video, caption=mestext,
                                   reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                                    keyboard=await form_keyboard(
                                                                        plots_info)),
                                   parse_mode='html')

