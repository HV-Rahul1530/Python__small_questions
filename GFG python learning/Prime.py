def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(3, int((n/2)+1)):
        if n % i == 0:
            return False
    return True

lst = []
limit = int(input("Give the range: "))
for i in range(limit):
    if is_prime(i):
        lst.append(i)
print(lst)