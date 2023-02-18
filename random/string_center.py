import os

def text_center(text, length, char):
    return text.center(length, str(char))

def text_center_terminal(max_length:int, border_char:str='-', word:str=None) -> str:
    """
    The enhanced version; the length of the line characters will be adjusted to the length of the terminal.
    """
    terminal_width, terminal_height = os.get_terminal_size()
    if terminal_width < max_length:
        max_length = terminal_width
    if not word:
        word = border_char
    return text_center(word, max_length, border_char)

if __name__ == '__main__':
    print(text_center('What\'s up?', 100, '-'))
    print(text_center_terminal(100, '-', 'What\'s up?'))

    # output
    # ---------------------------------------------What's up?---------------------------------------------
    # ---------------------------------------------What's up?---------------------------------------------
