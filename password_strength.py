import re


def symbols_strength_check(user_pass):
    strength = 0
    symbols_list = [r'^.*[A-Z]+.*$', r'^.*[a-z]+.*$', r'^.*[@#$%_-]+.*$', r'^.*[0-9]+.*$']
    for symbols in symbols_list:
        if re.search(symbols, user_pass):
            strength += 2
    return strength


def len_strength_check(user_pass):
    strength = 0
    if len(user_pass) > 10:
        strength += 2
    return strength


def black_list_strength_check(user_pass):
    strength = 0
    black_list = ['qwerty', '123456', '123', 'password', 'pass', 'user']
    for password in black_list:
        if user_pass.count(password):
            strength -= 3
    return strength


def print_pass_strength_result(pass_strength_result):
    print('Your password has %s/10 balls of strength.'
          % (pass_strength_result))


if __name__ == '__main__':
    user_pass = input('Please enter password: ')
    pass_strength_result = (symbols_strength_check(user_pass) +
                            len_strength_check(user_pass) +
                            black_list_strength_check(user_pass))
    print_pass_strength_result(pass_strength_result)
