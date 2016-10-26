# coding=utf-8


# 1.using assert to replace print
# assert grammar: is assert's juge statement is not TRUE, print the follow msg
def foo(s):
    n = int(s)
    assert n != 0, "n is not zero"
    return 10 / n


def main():
    foo(0)


main()
