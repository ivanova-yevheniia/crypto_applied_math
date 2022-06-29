p = int(input("Enter p:"))
g = int(input("Enter g:"))
#y = int(input("Enter y:"))
#x = int(input("Enter secret key x:"))
#y = (g**x)%p
y = int(input("enter y: "))
print("Your public key is ", g,",", p,",", y)

input_message = int(input("Enter message to encrypt:"))
while input_message > p-1:
    print("Message M must be less than p-1")
    input_message = int(input("Enter message to encrypt:"))

def find_prime_numb():
    lst = [2]
    for i in range(3, p, 2):
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
print_prime = print("Prime numbers for p-2:",find_prime_numb())
k = int(input("Choose 1 number k:"))

a = (g**k) % p
b = ((y**k) * input_message) % p
print("Cipertext","{a},{b}".format(a = a, b = b))

x=3333
decryptedM = ((a**(p-1-x)*b)%p)
print(decryptedM)