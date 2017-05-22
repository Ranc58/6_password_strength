import re


def get_words_strength(user_pass):
    strength=0


def get_symbols_strength(user_pass):
    strength = 0


def get_digits_strength(user_pass):
    strength = 0


def get_len_strength(user_pass):
    strength = 0


def user_info_in_pass_strength(user_pass):
    strength = 0


def get_password_strength(user_pass):
    strength = 0
    company = 'roga_i_kopita'
    if re.search(r'^.*[A-Z]+.*$', user_pass):
        strength += 1
    if re.match(r'^.*[@#$%_]+.*$', user_pass):
        strength += 3
    if re.match(r'^.*[a-z]+.*$', user_pass):
        strength += 1
    if re.match(r'^.*[0-9]+.*$', user_pass):
        strength += 2
    if len(user_pass) > 8:
        strength += 2
    if company in user_pass:
        strength -= 1
    print(n)


if __name__ == '__main__':
    user_pass = {'first_name':'Vasya',
                 'last_name':'Pupkin',
                 'company_name':'RogaKopita',
                 'telephone':'202020',
                 'date':'200588'
                 }
    #get_password_strength(user_pass)
