import csv
from Local_log import log_message
from telegram.ext import ConversationHandler

# Set the phonebook database as a dictionary
phonebookDB = {'Ivan': '+79260000000', 'Semen': '+79261111111', 'Nikita': '+79262222222'}

def phonebook_actions(update, context):
        
    # Get the user's message
    message = update.message.text
    
    # Log the command
    log_message (update, context)
    
    # Split the message into a list of words
    words = message.split()
    
    # Check that the message has the correct format (i.e., at least two words: the command and a subcommand)
    if len(words) >= 2:
        # Extract the subcommand from the message
        subcommand = words[0]
        # Check the subcommand
        if subcommand == 'search':
            # Check that the message has the correct format (i.e., three words: the command, the subcommand, and the name to search)
            if len(words) == 2:
                # Extract the name to search from the message
                name = words[1]
                # Check if the name is in the phonebook
                if name in phonebookDB:
                    # Send the phone number back to the user
                    update.message.reply_text(f'{name}: {phonebookDB[name]}')
                else:
                    update.message.reply_text(f'Ошибка: {name} не найдено в телефонной книге')
            else:
                update.message.reply_text('Ошибка: неправильный формат\n'
                                          'Используй формат "search [name]"\n'
                                          'для поиска в справочнике')
        
        elif subcommand == 'export':
            export_phonebook(update, context)
        
        elif subcommand == 'add':
            # Check that the message has the correct format (i.e., four words: the command, the subcommand, the name, and the phone number)
            if len(words) == 3:
                # Extract the name and phone number from the message
                name = words[1]
                phone_number = words[2]
                # Add the name and phone number to the phonebook
                phonebookDB[name] = phone_number
                update.message.reply_text(f'{name} добавлено в телефонную книгу')
            else:
                update.message.reply_text('Ошибка: неправильный формат\n'
                                          'Используй формат "add [name] [phone number]"\n'
                                          'для добавления контакта в телефонную книгу')
        elif subcommand == 'remove':
            # Check that the message has the correct format (i.e., three words: the command, the subcommand, and the name to remove)
            if len(words) == 2:
                # Extract the name to remove from the message
                name = words[1]
                # Check if the name is in the phonebook
                if name in phonebookDB:
                    # Remove the name and phone number from the phonebook
                    del phonebookDB[name]
                    update.message.reply_text(f'{name} удалено из телефонной книги')
                else:
                    update.message.reply_text(f'Ошибка: {name} не найдено в телефонной книге')
            else:
                update.message.reply_text('Ошибка: неправильный формат\n'
                                          'Используй формат "remove [name]"\n'
                                          'для удаления контакта из телефонной книги')
    return ConversationHandler.END

def export_phonebook(update, context):
    # Get the user's message
    message = update.message.text
    
    # Split the message into a list of words
    words = message.split()
    
    # Check that the message has the correct format (i.e., two words: the command and the file name)
    if len(words) == 2:
        # Extract the file name from the message
        file_name = words[1]
        
        # Open the CSV file in write mode
        with open(file_name, 'w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)
            
            # Write the header row to the CSV file
            csv_writer.writerow(['Name', 'Phone Number'])
            
            # Iterate through the phonebook database and write each name and phone number to the CSV file
            for name, phone_number in phonebookDB.items():
                csv_writer.writerow([name, phone_number])
        
        # Use the telegram API to send the CSV file to the user
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_name, 'rb'))
    else:
        update.message.reply_text('Ошибка: неправильный формат\n'
                         'Используй формат /export [file name]\n'
                         'для экспорта телефонной книги в CSV-файл')