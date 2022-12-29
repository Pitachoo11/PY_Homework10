import re
from Local_log import log_message
from telegram.ext import ConversationHandler

def remove_abc(input_string):
    # Use a regular expression to search for "abc" in the input string
    pattern = re.compile(r"abc")

    # Replace all occurrences of "abc" with an empty string
    output_string = pattern.sub("", input_string)

    return output_string

def handle_message(update, context):
    # Get the message from the update
    message = update.message
    text = message.text
    
    # Log the command
    log_message (update, context)

    # Remove "abc" from the message text
    modified_text = remove_abc(text)

    # Send the modified message back to the user
    context.bot.send_message(chat_id=message.chat_id, text=modified_text)
    return ConversationHandler.END