from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, ConversationHandler, CallbackQueryHandler

from Local_log import log_message 
from game import start_game, make_move
from Phonebook import phonebook_actions
from Calculator import calculator_actions
from menu import start, options
from abc_remove import handle_message

def cancel(update, context):
    update.message.reply_text("Операция отменена")
    return ConversationHandler.END

def main():
    # Create the Updater and pass it the bot's token
    updater = Updater('TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    
    # Define the conversation handler
    conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text, options)],  # The entry point is the options function
    states={
        1: [MessageHandler(Filters.text, calculator_actions)],
        2: [CommandHandler('game', start_game)],
        3: [MessageHandler(Filters.text, phonebook_actions)],
        4: [MessageHandler(Filters.text, handle_message)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]  # The cancel command is a fallback for the conversation
)

    # Add the conversation handler to the dispatcher
    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(make_move))
    dp.add_handler(MessageHandler(Filters.text, options))
    
    # Add handler for the rest of the messages
    dp.add_handler(MessageHandler(None, log_message))
    
    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == "__main__":
  main()