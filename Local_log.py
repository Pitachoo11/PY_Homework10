import logging

# Set up logging to a file

logging.basicConfig(
    filename='messages.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Format recieved message and log it
def log_message(update, context):
    message = update.message
    logger.info(f"{message.from_user.first_name} ({message.from_user.id}): {message.text}")
    