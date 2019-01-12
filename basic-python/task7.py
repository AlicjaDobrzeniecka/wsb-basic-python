
# Display alphabet in a format AaBbCcDd and then as aAbBcCdD.

import string

a = string.ascii_lowercase


def double_string(s):
    return ''.join([x*2 for x in s])


a = (double_string(a))

print(''.join(a[i-1].upper() if i % 2 else a[i-1] for i in range(1, len(a) + 1)))
print(''.join(a[i-1] if i % 2 or i == 0 else a[i-1].upper() for i in range(1, len(a) + 1)))