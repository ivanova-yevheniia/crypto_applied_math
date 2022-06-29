from math import *

p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = ",n ,"\n")
f=(p-1)*(q-1)
print("Euler's function f(n): " + str(f) + "\n")

def find_prime_numb():
    lst = [2]
    for i in range(3, f + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst
print_prime = print("Prime numbers for f:",find_prime_numb())
select_e = int(input("Choose 1 number for list of prime numbers"))

def find_d(select_e, f):
    for d in range(f):
        if ((select_e * d) % f) == 1:
            return d

dd = find_d(select_e,f)
print("Your private key is a pair of numbers (d=",dd, ", n=",n ,").\n")
print("Your public key is a pair of numbers (e=",select_e, ", n=",n, ").\n")


c = [71, 98, 95, 51, 91, 106, 73, 28]
print("Chipered message:", c)
def get_index(c):
    for i in c:
        yield i

new = get_index(c)
def ind():
    for i in new:
     return i

def m():
    new_lst = []
    for elem in range(len(c)):
        mi = (ind()**dd) % n
        new_lst.append(mi)

    return new_lst
def message_to_text(list):
    txt =""
    for el in list:
        txt += chr(el)
    return txt
message = m()
print("Decrypted message: ", message)
print("Message in text form: ", message_to_text(message))