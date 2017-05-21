import re


def get_password_strength(user_pass):
    n=0
    company='StroiInvest'
    if re.match(r'^\w', user_pass):
        n += 1
    if re.match(r'[^@#$]', user_pass):
        n += 2
    if re.match(r'[^A_Z]', user_pass):
        n += 3
    if company in user_pass:
        n-=1
    print(n)



if __name__ == '__main__':
    user_pass='ddFg5@StroiInvest'
    get_password_strength(user_pass)
