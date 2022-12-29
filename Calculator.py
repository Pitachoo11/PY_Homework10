from telegram.ext import ConversationHandler
from Local_log import log_message

def calculator_actions(update, context):
    #Calculate the result of a simple arithmetic expression.
    #update.message.reply_text('Ошибка: Некорректный формат\n')
    # Get the user's message
    message = update.message.text
    
    # Log the command
    log_message (update, context)

    # Split the message into a list of words
    words = message.split()
    
    # Check that the message has the correct format (i.e., three words: the command, an operator, and a number)
    if len(words) == 3:
        # Try to extract the operator and the number from the message
        try:
            operator = words[1]
            number1 = float(words[0])
            number2 = float(words[2])
            
            # Check that the operator is one of the supported ones  !!!! Использовать кортеж
            if operator in ['+', '-', '*', '/']:
                # Initialize the result
                result = 0
                # Perform the operation
                if operator == '+':
                    result = number1 + number2
                elif operator == '-':
                    result = number1 - number2
                elif operator == '*':
                    result = number1 * number2
                elif operator == '/':
                    # Check for division by zero
                    if number2 == 0:
                        result = 'Ошибка: Деление на 0'
                    else:
                        result = number1 / number2
                # Send the result back to the user
                update.message.reply_text(result)
            else:
                update.message.reply_text('Ошибка: Неподдерживаемый оператор')
        except ValueError:
            update.message.reply_text('Ошибка: Некорректное число')
    else:
        update.message.reply_text('Ошибка: Некорректный формат\n'
                                  'Правильный формат: /calculator [number1] [operator] [number2]\n'
                                  'где [operator] один из символов +, -, *, /')
    return ConversationHandler.END