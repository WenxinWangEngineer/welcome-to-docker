from itertools import groupby


def compress_string(s):
    return ' '.join(f"({len(list(g))}, {k})" for k, g in groupby(s))


s = '    1222311  '
# print(compress_string(s))
# clean the head and tail white spaces before process the string
print(compress_string(s.strip()))
