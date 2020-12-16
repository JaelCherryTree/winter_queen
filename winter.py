#!pip install pymorphy2
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()


def make_list(string): #разделяет строку на слова
    my_list = string.split(' ')
    for x in range(len(my_list)):
        if my_list[x].endswith(','): #убираем запятые, потом будем расставлять заново
            my_list[x] = my_list[x][:-1]
    return my_list


def double(s, l): #удваивает буквы из списка l в строке s, если они не стоят в начале слова
    for ll in l:
        if not s.startswith(ll):
            s = s.replace(ll, ll*2)
    return s


def beautiful_words(w_list): #всячески извращается над словами
    a = 0
    b_w = []
    for w in w_list:
        form = morph.parse(w)[0].tag.case
        if form == 'nomn':
            w += ',' #ставит запятую после слова в именительном падеже
        w = double(w, ['ф', 'л'])
        if 'ё' in w:
            w = w.replace('и', 'е')
        if w.startswith('пре'):
            w = w.replace('пре', 'при')
        elif w.startswith('при'):
            w = w.replace('при', 'пре')
        if w.endswith('!'):
            if a%2 == 0:
                w = w.replace('!', '!!!')
            a += 1
        b_w.append(w)
    return b_w


def corr(w_list, d_one, d_two):
    end = []
    yes = 0
    for w in w_list:
        for k in d_one.keys():
            if k in w:
                w = w.replace(k, d_one[k])
                yes = 1
        if yes == 0:
            for k in d_two.keys():
                if k in w:
                    w = w.replace(k, d_two[k])
        end.append(w)
    sentence = ' '.join(end)
    return sentence


def main():
    correct_one = {'ара': 'оро', 'ана': 'оно', 'ере': 'ири', 'еле': 'или'}
    correct_two = {'оро': 'ара', 'ири': 'ере', 'одо': 'ада'}
    my_text = input()
    my_list = make_list(my_text)
    b_w = beautiful_words(my_list)
    s = corr(b_w, correct_one, correct_two)
    print(s)


if __name__ == "__main__":
    main()

