from aiogram import Router, F, Bot
from aiogram.methods.send_photo import SendPhoto as send_photo
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import sql as sql
import random

import keyboards as kb
from config import TOKEN
bot = Bot(token=TOKEN)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):

    await sql.db_start()

    user_info = await sql.get_user_info(message.from_user.id)
    if user_info == None:
        await sql.create_user(user_id=message.from_user.id, username=message.from_user.username)
        await message.answer_photo(photo='AgACAgIAAxkBAAMKZ9mtuZ6ewn22HTCdL_obKn5ReUAAAp7rMRvndtFKtk5eG0M3Id8BAAMCAANzAAM2BA', caption=kb.main_text, reply_markup=kb.main, parse_mode='html')
    else:
        await sql.create_user(user_id=message.from_user.id, username=message.from_user.username)
        await message.answer_photo(photo = 'AgACAgIAAxkBAAMKZ9mtuZ6ewn22HTCdL_obKn5ReUAAAp7rMRvndtFKtk5eG0M3Id8BAAMCAANzAAM2BA', caption=kb.main_text_olduser, reply_markup=kb.main_olduser, parse_mode='html')

@router.message(F.photo)
async def handle_files(message: Message):
    if message.from_user.id == 600335172 or message.from_user.id == 1370964537:
        await message.answer(text = message.photo[0].file_id)
    else:
        await message.answer(text='Я тебя не понял')

@router.message(F.audio)
async def handle_files(message: Message):
    if message.from_user.id == 600335172 or message.from_user.id == 1370964537:
        await message.answer(text = message.audio.file_id)
    else:
        await message.answer(text='Я тебя не понял')

@router.message(F.video)
async def handle_files(message: Message):
    if message.from_user.id == 600335172 or message.from_user.id == 1370964537:
        await message.answer(text = message.video.file_id)
    else:
        await message.answer(text='Я тебя не понял')



@router.message()
async def main_func(message: Message):
    #user_channel_status = await bot.get_chat_member(chat_id=-1001991921457, user_id=message.from_user.id)
    user_channel_status = 'ok'
    if user_channel_status != 'left':
        async def health(ui, pl):
            global stat

            health_bar = int(ui[5]) + int(pl[7])
            await sql.health_change(health_bar, ui)
            return health_bar

        restext = message.text
        user_info = await sql.get_user_info(message.from_user.id)
        stat = user_info[2]

        plots_info = await sql.get_plots_info(stat)

        if user_info[3] == 'yes':
            stat = await sql.stat_change(user_id=message.from_user.id, stat=stat, plot=plots_info, restext=restext)
            await sql.update_stat_to_change(user_id=message.from_user.id, stat_TC='no')
            plots_info = await sql.get_plots_info(stat)


        if plots_info[9] == 'fight: cy-e-fa':
            if user_info[9] == 'null':
                rules = 'Чтобы победить, тебе нужно выиграть 3 раза в камернь-ножницы-бумагу'
                await message.answer(rules, parse_mode='html')
                rnd1 = 'Раунд 1: Выбери свою фигуру'
                await sql.game_stat_change(user_info[0],'knb!1!0:0')
                await message.answer(rnd1, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='🗿'), KeyboardButton(text='✂️'), KeyboardButton(text='⬜️')]]), parse_mode='html')
            else:
                random_number_knb = random.randint(0, 2)
                knm_dict = {0:'🗿', 1:'✂️', 2: '⬜️'}
                knn_ans = knm_dict[random_number_knb]
                gamknb = user_info[9].split('!')

                if restext == knn_ans:
                    await message.answer(f'Твой соперник выбрал: {knn_ans}\n\nНичья! Еще раз', parse_mode='html')
                    schet_2 = gamknb[2]
                elif restext == '🗿' and random_number_knb == 1 or restext == '✂️' and random_number_knb == 2 or restext == '⬜️' and random_number_knb == 0:
                    schet = gamknb[2].split(":")
                    schet_2 = f'{int(schet[0])+1}:{schet[1]}'
                    await sql.game_stat_change(user_info[0], '!'.join(['knb', str(int(gamknb[1])+1), schet_2]))

                    if '3' not in schet_2:
                        await message.answer(f'Твой соперник выбрал: {knn_ans}\n\nПобеда!!\n\nСчёт: {schet_2}\n\nРаунд {int(gamknb[1])+1}: Выбери свою фигуру',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='🗿'), KeyboardButton(text='✂️'), KeyboardButton(text='⬜️')]]), parse_mode='html')
                else:
                    schet = gamknb[2].split(":")
                    schet_2 = f'{schet[0]}:{int(schet[1])+1}'


                    await sql.game_stat_change(user_info[0], '!'.join(['knb', str(int(gamknb[1])+1), schet_2]))

                    if '3' not in schet_2:
                        await message.answer(f'Твой соперник выбрал: {knn_ans}\n\nПоражение!!\n\nСчёт: {schet_2}\n\nРаунд {int(gamknb[1])+1}: Выбери свою фигуру',reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='🗿'), KeyboardButton(text='✂️'), KeyboardButton(text='⬜️')]]), parse_mode='html')

                if '3' in schet_2:
                    await sql.game_stat_change(user_info[0], 'null')
                    if schet_2[0] == '3':
                        await message.answer(
                            f'Твой соперник выбрал: {knn_ans}\n\nПобеда!!\n\nСчёт: {schet_2} - Победа в игре!!\n\n',
                            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
                                [KeyboardButton(text='урааа')]]),
                            parse_mode='html')

                        stat = await sql.stat_change(user_id=message.from_user.id, stat=stat, plot=plots_info, restext='победа')
                    else:
                        await message.answer(
                            f'Твой соперник выбрал: {knn_ans}\n\nПоражение!!\n\nСчёт: {schet_2} - Поражение в игре\n\n',
                            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
                                [KeyboardButton(text='жаль')]]),
                            parse_mode='html')
                        stat = await sql.stat_change(user_id=message.from_user.id, stat=stat, plot=plots_info,
                                                     restext='поражение')

        else:
            plots_info = await sql.get_plots_info(stat)
            health_bar = await health(user_info, plots_info)
            if plots_info[9] == 'start':
                await sql.start_plot(user_info, plots_info)
            else:
                await health(user_info, plots_info)
            await kb.send_message(user_info=user_info, message_user_id=message.from_user.id, plots_info=plots_info, message=message, health_bar=health_bar)

            if health_bar < 1:
                random_number = random.randint(0, 5)
                if random_number == 0:
                    await message.answer('Прости, пупсик, но ты умер', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='Жаль-жаль')]]))
                elif random_number == 1:

                    await message.answer_photo(photo='AgACAgIAAxkBAAINwmV7Oh2y3PYLvmz_iXsFAAE6ZzYcGQACht0xG7vy4UtjI-EBZ8B5vAEAAwIAA3MAAzME', caption='Прости, пупсик, но ты умер', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Светлая память')]]), parse_mode='html')
                elif random_number == 2:
                    await message.answer_photo(photo='AgACAgIAAxkBAAINxGV7OsSdlVVmDvxVSvCnwcNsO6icAAKO3TEbu_LhS2SCEjghpxh_AQADAgADcwADMwQ', caption='Прости, пупсик, но ты умер', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='Светлая память')]]), parse_mode='html')
                elif random_number == 3:
                    await message.answer_photo(photo='AgACAgIAAxkBAAINxmV7OymIkXG9ntEtcVJ8wkdneH3zAAKW3TEbu_LhS8P_A9IiYTFxAQADAgADcwADMwQ', caption='Прости, пупсик, но ты умер',
                                               reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='Мертв(а), но не сломлен(а)')]]), parse_mode='html')
                elif random_number == 4:
                    await message.answer_photo(photo='AgACAgIAAxkBAAINyGV7O5TJDomk02Xp1etlkQPMpgUXAAKk3TEbu_LhS621qgYF_9JwAQADAgADcwADMwQ', caption='Прости, пупсик, но ты умер',
                                               reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='RIP')]]), parse_mode='html')



                await sql.stat_change_dead(user_id=user_info, plot=plots_info)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text="Подписаться",
            url="https://t.me/+JA8oHnooWzllMTIy")
        )
        await message.answer(
            "Прежде чем мы продолжим, пожалуйста, подпишись на наш тгк 👉👈🥺🥺🥺  \n\nЭто не реклама и мы не будем засорять твою тгшку - просто так ты будешь знать все о делах проекта, а также иногда хихикать с шуточек. \nЗаранее благодарим\n\nP.S. Если подписался 🥳🥳 и пропали кнопки, то их можно их вернуть через квадратик с кружочками внизу",
            reply_markup=builder.as_markup()
        )
