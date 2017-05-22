import re


def get_symbols_strength(user_pass):
    strength=0
    if re.search(r'^.*[A-Z]+.*$', user_pass):
        strength += 1
    if re.search(r'^.*[a-z]+.*$', user_pass):
        strength += 2
    if re.match(r'^.*[@#$%_]+.*$', user_pass):
        strength += 2
    if re.match(r'^.*[0-9]+.*$', user_pass):
        strength += 2
    return strength


def get_len_strength(user_pass):
    strength = 0
    if len(user_pass) > 8:
        strength += 2
    return strength


def get_black_list_strength(user_pass):
    strength = 0
    black_list = ['qwerty', '123456', '123', 'password', 'pass','user']
    strength+=11 if list(map(lambda black_pass : user_pass.count(black_pass), black_list)) else strength = 0
    print(s)
    return strength


if __name__ == '__main__':
    user_pass = input('Please enter password: ')
    total_strength=(get_symbols_strength(user_pass)+
                    get_len_strength(user_pass)+
                    get_black_list_strength(user_pass))
    if total_strength > 0:
        print('Your password has %s/10 balls of strength.' % (total_strength))
    if total_strength <= 0:
        print('Your password in blacklist! Please change it!')
