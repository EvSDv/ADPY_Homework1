

def adv_print(*args, start='', max_line=0, in_file=False,):
    result = str(start)
    result_sep = ''
    for value in args:
        result += str(value)

    if max_line > 0 and len(result) > max_line:
        for symbol in range(0, len(result), max_line):
            result_sep += result[symbol:symbol + max_line] + '\n'
        result = result_sep

    if in_file:
        print(result)
        with open('result.txt', 'w', encoding='utf8') as file:
            print(result, file=file)
    else:
        print(result)








adv_print(31531 + 153, 'qwertyuio', start='----',max_line=5)