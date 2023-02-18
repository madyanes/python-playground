def text_center(text, length, char):
    return text.center(length, str(char))

if __name__ == '__main__':
    print(text_center('What\'s up?', 100, '-'))

    # output
    # ---------------------------------------------What's up?---------------------------------------------
