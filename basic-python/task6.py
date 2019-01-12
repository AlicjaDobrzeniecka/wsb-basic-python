
# Write a program where basing on the data from the user (length of the blocks) checks whether
# it is possible to build a triangle and whether it is a right triangle. The circuit and
# the area should be displayed.


def triangle_check(l1, l2, l3):

    l1, l2, l3 = sorted([l1, l2, l3])
    r = abs(l1 ** 2 + l2 ** 2 - l3 ** 2)
    s = (l1 + l2 + l3) / 2
    area = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
    circuit = l1 + l2 + l3

    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')

    elif r < 0.1:
        print("Yes, a right triangle can be formed out of it")
        print("The circuit is equal to: %0.2f, the are is equal to: %0.2f" % (circuit, area))

    else:
        print('Yes, a triangle can be formed out of it, but not a right one.')
        print("The circuit is equal to: %0.2f, the are is equal to: %0.2f" % (circuit, area))


length1 = int(input('Enter first length: '))
length2 = int(input('Enter second length 2: '))
length3 = int(input('Enter third length 3: '))

triangle_check(length1,length2,length3)
