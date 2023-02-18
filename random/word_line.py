def get_line(amount :int) -> str:
    return '-' * amount

def word_replacement(word :str, line_amount :int=10) -> str:
    word_length:int = len(word)
    if word_length > line_amount:  # if the character is lesser than the line, raise an exception
        return False
    line_needed = line_amount - word_length
    return word + get_line(line_needed)

print(word_replacement('Hello, world?!', 100))
print(word_replacement('Do you really like programming?', 100))

# output
# Hello, world?!--------------------------------------------------------------------------------------
# Do you really like programming?---------------------------------------------------------------------
