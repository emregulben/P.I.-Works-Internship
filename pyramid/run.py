import copy


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    k = 5
    while k <= r:
        if n % k == 0:
            return False
        if n % (k+2) == 0:
            return False
        k += 6
    return True


with open("input.txt", "r") as f:
    pyramid_strings = []
    for line in f.readlines():
        pyramid_strings.append(line.strip().split())

pyramid = []
for line in pyramid_strings:
    pyramid.append([])
    for number in line:
        pyramid[pyramid_strings.index(line)].append(eval(number.lstrip('0')))

temp = copy.deepcopy(pyramid)
for i in range(len(pyramid)-1, -1, -1):
    for j in range(len(pyramid[i])-1):
        if (temp[i][j] > temp[i][j+1]) and (not isPrime(pyramid[i][j])):
            temp[i-1][j] += temp[i][j]
        elif not isPrime(pyramid[i][j+1]):
            temp[i-1][j] += temp[i][j+1]
        elif not isPrime(pyramid[i][j]):
            temp[i-1][j] += temp[i][j]
        else:
            temp[i - 1][j] = -9999999


if temp[0][0] < 0:
    print pyramid[0][0]
else:
    print temp[0][0]