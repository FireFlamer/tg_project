from telebot import types
from buttons import *

def start_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(tutor_btn, teacher_btn)

    return keyboard
    
def menu_keyboard(profile_name: str) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=3) 
    keyboard.add(*menu_buttons_profiles[profile_name])

    return keyboard

def partners_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for partner in partner_buttons.keys():
        keyboard.add(types.InlineKeyboardButton(text=partner, callback_data=f'partner/{partner}'))
    keyboard.row(partners_back_btn)
   
    return keyboard

def partner_keyboard(partner: str) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    for btn in partner_buttons[partner].values():
        keyboard.add(btn)
    keyboard.row(partner_back_btn, partner_menu_btn)
    
    return keyboard

def courses_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(basic_cources_btn, summer_school_btn, short_groups_btn)
    keyboard.row(courses_back_btn)

    return keyboard

def motivation_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(feedback_btn, movavi_boost_btn, motibation_back_btn)
    
    return keyboard

def instruction_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=3)    
    keyboard.add(doc_manage_btn, box_office_btn, fire_evac_btn, partners_work_btn, first_aid_btn, crm_btn)
    keyboard.row(instruction_back_btn)

    return keyboard

def crm_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(contract_create_info_btn, how_to_pay_btn)
    keyboard.row(cpm_back_btn, cpm_menu_btn)

    return keyboard

def axo_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(mobile_numbers_btn)
    keyboard.row(axo_back_btn, axo_menu_btn)

    return keyboard