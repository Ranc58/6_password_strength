import re
import getpass


def words_strength_check(user_pass):
    if re.search(r'^.*[A-Za-zА-Яа-я]+.*$', user_pass):
        return True


def symbols_strength_check(user_pass):
    if re.search(r'^.*[@#$%_-]+.*$', user_pass):
        return True


def digits_strength_check(user_pass):
    if re.search(r'^.*[0-9]+.*$', user_pass):
        return True


def len_strength_check(user_pass):
    min_good_len_for_pass = 10
    if len(user_pass) >= min_good_len_for_pass:
        return True


def blacklist_strength_check(user_pass, blacklist):
    blacklist = [password.rstrip('\n') for password in blacklist]
    for password in blacklist:
        if user_pass == password:
            return True


def print_pass_strength_result(pass_strength_result):
    print('Your password has {}/10 points of strength.'
          .format(pass_strength_result))


if __name__ == '__main__':
    user_pass = getpass.getpass('Please enter password: ')
    with open('PassBlackList.txt') as blacklist:
        blacklist_strength = blacklist_strength_check(user_pass, blacklist)
    pass_strength_result = 0
    if words_strength_check(user_pass):
        pass_strength_result += 2
    if symbols_strength_check(user_pass):
        pass_strength_result += 2
    if digits_strength_check(user_pass):
        pass_strength_result += 3
    if len_strength_check(user_pass):
        pass_strength_result += 3
    if blacklist_strength:
        pass_strength_result -= 2
    print_pass_strength_result(pass_strength_result)
