# -*- coding: utf-8 -*
def censor(text, word):
    result = ''  # result 用于拼接返回的字符串
    strList = text.split()
    for x in strList:
        if x == word:
            x = '*' * len(word)
            print(x)
            print("strList数据没有变:\t")
            print(strList)  # strList 是不会有变化的
        result = result + x + ' '
    return result


print(censor("I love you", "love"))
