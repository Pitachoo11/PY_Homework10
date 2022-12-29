from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Constants
BOARD_SIZE = 3

# Global variables
game_state = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = "X"

def start_game(update, context):
    """Старт новой игры"""
    global game_state, current_player
    game_state = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "X"
    send_game_message(update, context)

def make_move(update, context):
    """Ход очередного игрока"""
    global game_state, current_player
    query = update.callback_query
    row, col = map(int, query.data.split())
    if game_state[row][col] is not None:
        # Square is already taken
        query.answer(text="Неправильный ход!")
        return
    game_state[row][col] = current_player
    if check_game_won():
        text = f"{current_player} победил!"
        game_over = True
    elif check_game_drawn():
        text = "Игра вничью!"
        game_over = True
    else:
        text = f"{current_player} походил ({row}, {col})"
        game_over = False
        # Switch players
        current_player = "O" if current_player == "X" else "X"
    query.edit_message_text(text=text)
    if not game_over:
        send_game_message(update, context)

def check_game_won():
    """Проверка выигрыша и завершения игры"""
    global game_state
    # Check rows
    for row in game_state:
        if all(cell == "X" for cell in row):
            return True
        if all(cell == "O" for cell in row):
            return True
    # Check columns
    for col in range(BOARD_SIZE):
        if all(game_state[row][col] == "X" for row in range(BOARD_SIZE)):
            return True
        if all(game_state[row][col] == "O" for row in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(game_state[i][i] == "X" for i in range(BOARD_SIZE)):
        return True
    if all(game_state[i][i] == "O" for i in range(BOARD_SIZE)):
        return

def check_game_drawn():
    """Проверка выигрыша и завершения игры (больше нет ходов)."""
    global game_state
    return all(cell is not None for row in game_state for cell in row)

def send_game_message(update, context):
    """Отправка сообщения о текущем статусе игры"""
    keyboard = [[
        InlineKeyboardButton(f"{game_state[i][j] or ' '}", callback_data=f"{i} {j}")
        for j in range(BOARD_SIZE)
    ] for i in range(BOARD_SIZE)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Сейчас ходит {current_player}",
        reply_markup=reply_markup
    )