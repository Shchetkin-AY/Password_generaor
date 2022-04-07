import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''


def generator_pass(len_pass, chars):
    return ''.join(random.sample(chars, len_pass))


while True:
    count_pass = int(input('Введите количество паролей для генерации: '))
    len_pass = int(input('Введите длину одного пароля: '))
    include_num = input(
        'Использовать ли цифры "0123456789"? Если использовать, нажмите "д". Если не испоьзовать, нажмите "н" ')
    if include_num.lower() == 'д':
        chars = chars + digits
    include_uplit = input(
        'Использовать ли заглавные буквы латинского алфавита? Если использовать, нажмите "д". Если не испоьзовать, нажмите "н" ')
    if include_uplit.lower() == 'д':
        chars = chars + uppercase_letters
    include_lowlit = input(
        'Использовать ли строчные буквы латинского алфавита? Если использовать, нажмите "д". Если не испоьзовать, нажмите "н" ')
    if include_lowlit.lower() == 'д':
        chars = chars + lowercase_letters
    include_simb = input(
        'Использовать ли символы "!#$%&*+-=?@^_"? Если использовать, нажмите "д". Если не испоьзовать, нажмите "н" ')
    if include_simb.lower() == 'д':
        chars = chars + include_simb
    no_simbols = input(
        'Требуется ли исключать неоднозначные символы "il1Lo0O"? Если использовать, нажмите "д". Если не испоьзовать, нажмите "н" ')
    if no_simbols.lower() == 'д':
        chars = chars.replace('il1Lo0O', '')
    for i in range(1, count_pass + 1):
        print(f'Ваш сгенерированный пароль {i}: ', generator_pass(len_pass, chars))
    break
