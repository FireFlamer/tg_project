from telebot import types

#Кнопки для комманды /start
tutor_btn = types.InlineKeyboardButton(text="Я куратор", callback_data='tutor')
teacher_btn = types.InlineKeyboardButton(text="Я учитель", callback_data='teacher')

#Кнопки для меню
company_info_btn = types.InlineKeyboardButton(text="О компании", url='https://ya.ru')
structure_btn = types.InlineKeyboardButton(text="Структура(Что?Где?Когда?)", url='https://ya.ru')
courses_btn = types.InlineKeyboardButton(text="Карта курсов", callback_data='courses')
partners_btn = types.InlineKeyboardButton(text="Партнеры", callback_data='partners')
motivation_btn = types.InlineKeyboardButton(text="Мотивация", callback_data='motivation')
working_methods_btn = types.InlineKeyboardButton(text="Методы работы", url='https://ya.ru')
instruction_btn = types.InlineKeyboardButton(text="Инструкции и регламенты", callback_data='instructions')
axo_btn = types.InlineKeyboardButton(text="АХО", callback_data='axo')

menu_buttons_profiles = { #Профили для клавиатуры меню
    "teacher": [company_info_btn, structure_btn, courses_btn, partners_btn, motivation_btn, working_methods_btn],
    "tutor": [company_info_btn, instruction_btn, courses_btn, structure_btn, partners_btn, motivation_btn, axo_btn]
    }

#Кнопки для партнёров
partners_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='menu')
partner_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='partners]')
partner_menu_btn = types.InlineKeyboardButton(text="В главное меню", callback_data='menu')

partner_buttons = {
    "Рост":{
        'olympiad_btn': types.InlineKeyboardButton(text="Олимпиада", url='https://ya.ru'),
        'cources_btn': types.InlineKeyboardButton(text="Курсы", url='https://ya.ru')
        },
    "Проскул":{
        'cources_btn': types.InlineKeyboardButton(text="Курсы", url='https://ya.ru')
        },
    "10ая гимназия":{
        'cources_btn': types.InlineKeyboardButton(text="Курсы", url='https://ya.ru')
        }
    }

#Кнопки курсов
basic_cources_btn = types.InlineKeyboardButton(text="Основные курсы", url='https://ya.ru')
summer_school_btn = types.InlineKeyboardButton(text="Летняя школа", url='https://ya.ru')
short_groups_btn = types.InlineKeyboardButton(text="Краткосрочные группы", url='https://ya.ru')
courses_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='menu')

#Кнопки мотивации
feedback_btn = types.InlineKeyboardButton(text="Обратная связь", url='https://ya.ru')
movavi_boost_btn = types.InlineKeyboardButton(text="Мовави Буст инструкция/пароли", url='https://ya.ru')
motibation_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='menu')

#Кнопки инструкции
doc_manage_btn = types.InlineKeyboardButton(text="Документооборот", url='https://ya.ru')
box_office_btn =types.InlineKeyboardButton(text="Касса", url='https://ya.ru')
fire_evac_btn = types.InlineKeyboardButton(text="Пожарная эвакуация", url='https://ya.ru')
partners_work_btn = types.InlineKeyboardButton(text="Работа с контрагентами", url='https://ya.ru')
first_aid_btn = types.InlineKeyboardButton(text="Первая помощь", url='https://ya.ru')
crm_btn = types.InlineKeyboardButton(text="СРМ", callback_data='crm')
instruction_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='menu')

#Кнопки для срм
contract_create_info_btn = types.InlineKeyboardButton(text="Как создать договор", url='https://ya.ru')
how_to_pay_btn = types.InlineKeyboardButton(text="Как произвести оплату", url='https://ya.ru')
cpm_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='instructions')
cpm_menu_btn = types.InlineKeyboardButton(text="В главное меню", callback_data='menu')

#AXO кнопки
mobile_numbers_btn = types.InlineKeyboardButton(text="Полезные телефоны", url='https://ya.ru')
axo_back_btn = types.InlineKeyboardButton(text="<-- Назад", callback_data='menu')
axo_menu_btn = types.InlineKeyboardButton(text="В главное меню", callback_data='menu')

