def get_line(amount :int) -> str:
    return '-' * amount

def word_replacement(word :str, line_amount :int=10, right:bool=False) -> str:
    word_length:int = len(word)
    line_needed = line_amount - word_length
    if right:
        return get_line(line_needed) + word
    return word + get_line(line_needed)

print(word_replacement('Hello, world?!', 100))
print(word_replacement('Do you really like programming?', 100))
print(word_replacement('Never stop learning!', 100, right=True))
print(word_replacement('Never stop learning!', 10, right=True))

# output
# Hello, world?!--------------------------------------------------------------------------------------
# Do you really like programming?---------------------------------------------------------------------
# --------------------------------------------------------------------------------Never stop learning!
# Never stop learning!
