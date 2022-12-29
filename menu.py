from telegram import ReplyKeyboardMarkup

def start(update, context):
    # Create the menu keyboard
    menu_keyboard = [['Калькулятор', 'Игра'],
                     ['Тел.книга', 'abc remover']]

    # Create the ReplyKeyboardMarkup object
    reply_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True)

    # Send the message with the menu
    update.message.reply_text('Please choose an option:', reply_markup=reply_markup)
    
def options(update, context):
    # Get the user's choice
    choice = update.message.text

    # Do something with the choice
    if choice == 'Калькулятор':
        update.message.reply_text(r'''Введите операцию для расчета в формате: [number1] [operator] [number2]
Например: 12 + 80 (ПРОБЕЛ между символами!!!)''')
        return 1  # Set the state to 1

    elif choice == 'Игра':
        update.message.reply_text(r'''Игра в Крестики-Нолики :
Для старта введите /game"''')
        return 2
    elif choice == 'Тел.книга':
        update.message.reply_text(r'''Телефонный справочник - Поиск и управление телефонной книгой:
Поиск: "search [name]"
Добавление: "add [name] [phone number]"
Удаление: "remove [name]"
Экспорт: "export [file name.csv]"''')
        return 3  # Set the state to 3
    elif choice == 'abc remover':
        update.message.reply_text('Удаление комбинации "abc" из всех слов введенной строки:')
        return 4  # Set the state to 3