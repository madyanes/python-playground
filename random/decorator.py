import time
import string_center

def decorator_border(func):
    def inner_func(*args, **kwargs):
        print(string_center.text_center_terminal(100))
        print(string_center.text_center_terminal(100, ' ', func()))
        print(string_center.text_center_terminal(100))
    return inner_func

@decorator_border
def just_text():
    return 'I ♥ PYTHON'

if __name__ == '__main__':
    just_text()

    # output
    # ----------------------------------------------------------------------------------------------------
    #                                              I ♥ PYTHON
    # ----------------------------------------------------------------------------------------------------
