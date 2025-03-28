from telebot import TeleBot, types
from keyboards import *
from config import TOKEN
from db.User import User

bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    if User.check_user_existance(user_id=message.from_user.id):
        menu(message=message, user_id=message.from_user.id)
    else:
        text = f"Приветствую, {message.from_user.username}! Выбери свою роль: "
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=start_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ['tutor', 'teacher'])
def user_reg(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id, timeout=1)
    User.create_user(id=call.from_user.id, username=call.from_user.username, role=call.data)
    menu(message=call.message, user_id=call.from_user.id)

def menu(message: types.Message, user_id: int):
    if User.get_user_role(user_id=user_id):
        text = f"Добро пожаловать!\nВаша роль: {User.get_user_role(user_id=user_id)}"
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=menu_keyboard(profile_name=User.get_user_role(user_id=user_id)))
    else:
        bot.send_message(chat_id=message.chat.id, text="Вы не зарегестрированны! Для регистрации введите команду /start")
        
@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def return_to_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    menu(message=call.message, user_id=call.from_user.id)


@bot.callback_query_handler(func=lambda call: call.data == 'courses')
def courses_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Наши курсы"
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=courses_keyboard(), timeout=1)

@bot.callback_query_handler(func=lambda call: call.data == 'motivation')
def motivation_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Мотивационные программы:"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=motivation_keyboard(), timeout=1)

@bot.callback_query_handler(func=lambda call: call.data == 'instructions')
def instructions_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Вот все инструкции для вас: "
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=instruction_keyboard(), timeout=1)

@bot.callback_query_handler(func=lambda call: call.data == 'partners')
def partners_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Наши партнёры: "

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=partners_keyboard(), timeout=1)

@bot.callback_query_handler(func=lambda call: 'partner' in call.data)
def partner_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Вся информация о партнёре: "

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=partner_keyboard(call.data.split('/')[1]))

@bot.callback_query_handler(func=lambda call: call.data == 'crm')
def cpm_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Инструкции: "

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=crm_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == 'axo')
def axo_menu(call: types.CallbackQuery):
    bot.answer_callback_query(callback_query_id=call.id)
    text = "Полезная информация: "

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=axo_keyboard())

@bot.message_handler(content_types=['text'])
def wrong_command_answer(message: types.Message):
    if message.text.strip().startswith('/'):
        bot.send_message(chat_id=message.chat.id, text="Неверно ведённая команда!")

if __name__ == '__main__':
    bot.polling(
        non_stop=True,
        interval=1
    )