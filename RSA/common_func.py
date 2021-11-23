
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def convert(text):
    pValue = 0
    qValue = 0
    for i in range(len(text)):
        if len(text[i]) == 0:
            pValue += ord(" ")
            qValue += ord(" ")
        elif len(text[i]) < 2:
            pValue += ord(text[0])
            qValue += ord(text[0])
        else:
            pValue = pValue + ord(text[0]) + ord(text[1])
            qValue = qValue + ord(text[(len(text) // 2)]) + ord(text[1 + (len(text) // 2)])

    f = open("../common/primeNumbers.txt", "r")
    file = f.read()
    array = file.split(" ")
    pi = 5
    for i in range(len(array)):
        if pValue == array[i]:
            pi = int(array[i])
            break
        elif int(array[i]) < pValue < int(array[i + 1]):
            pi = int(array[i + 1])
            break
    qu = 3
    for i in range(len(array)):
        if qValue == array[i]:
            qu = int(array[i])
            break
        elif int(array[i]) < pValue < int(array[i + 1]):
            qu = int(array[i])
            break
    return qu, pi
