import random, string


def randomSequence(r, l):
    s = string.ascii_letters + string.digits + '@#$%&*'
    random_seq = []

    stringList = list(s)
    while 1:
        random.shuffle(stringList)
        res = ''.join(stringList[:l])
        if res in set(random_seq):
            continue
        random_seq.append(res)
        if len(random_seq) >= r:
            break
    return random_seq


if __name__ == '__main__':
    result = randomSequence(200, 8)
    print(result)
