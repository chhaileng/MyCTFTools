def prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False

        return True


def check(before):
    for num in list(reversed(range(1,before))):
        if prime(num):
            return num

print check(1337)