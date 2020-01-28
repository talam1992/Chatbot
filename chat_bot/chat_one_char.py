__author__ = 'Timothy Lam'

def _number(x):
    return x + 1


def _char(ch):
    if ch == 'z':
        return 'z'
    else:
        return chr(ord(ch)+1)


def main(msg):
    if msg.isdigit():
        return _number(int(msg))
    else:
        return _char(msg)
