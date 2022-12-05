def Create_li_poly(string):
    if (string[0] != '-'):
        string = '+' + string
    string += '+'
    li = []
    j = 0
    # count = len(string) if ((len(string)-1) %
    #                         5 == 0) else len(string)+(4-(len(string)-1) % 5)
    # for i in range(1, count):
    #     if (string[i] == 'x') and ((string[i-1] == '+') or (string[i-1] == '-')):
    #         string = string[:i] + '1' + string[i:]
    #     if (string[i-1] == 'x') and ((string[i] == '+') or (string[i] == '-')):
    #         string = string[:i] + '^1' + string[i:]
    #         print('da')
    if ('+x' in string):
        string = string.replace('+x', '+1x')
    if ('-x' in string):
        string = string.replace('-x', '+1x')
    if ('x+' in string):
        string = string.replace('x+', 'x^1+')
    if ('x-' in string):
        string = string.replace('x-', 'x^1-')
    if (string[-2].isdigit()) and (string[-3] != '^'):
        string = string[:-1] + 'x^0' + string[-1]
    for i in range(1, len(string)):
        if (string[i] == '+') or (string[i] == '-'):
            li.append(string[j:i])
            j = i
    return li


def Parse_poly(s):
    value_, key_ = s.split('x^')
    return key_, int(value_)


def Sum_dict_poly(x: dict, y: dict):
    new_dict = dict()
    for key in x:
        if key in y:
            new_dict[key] = x[key]+y[key]
        else:
            new_dict[key] = x[key]
    for key in y:
        if key not in new_dict:
            new_dict[key] = y[key]
    for key in new_dict:
        if (new_dict[key] > 0):
            new_dict[key] = '+' + str(new_dict[key])
        else:
            new_dict[key] = str(new_dict[key])
    return new_dict


def List_to_string_poly(li: list):
    for el in li:
        if (el[1] == '0'):
            li.remove(el)
    string=''
    for el in li:
        if (el[0] != '0') and (el[0] != '1'):
            if (el[1] == '+1'):
                string += '+x^' + el[0]
            elif (el[1] == '-1'):
                string += '-x^' + el[0]
            else:
                string += el[1] + 'x^' + el[0]
        elif (el[0] == '1'):
            if (el[1] == '+1'):
                string += '+x'
            elif (el[1] == '-1'):
                string += '-x'
            else:
                string += el[1] + 'x'
        else:
            string += el[1]
    if (string[0] == '+'):
        string = string[1:]
    return string
