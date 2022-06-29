p = int(input("Enter p:"))
#g = int(input("Enter g:"))
#y = int(input("Enter y:"))
#print("Your public key is ", g,",", p,",", y)

input_text = input("Enter (a,b)")
inputed = input_text.split(",")
a = int(inputed[0])
b = int(inputed[1])
'''def find_x():
    for x in range(p):
        if y == ((g**x) % p):
            print("Your secret key x = ", x)
            return x'''
xx = int(input("x: "))

f = a**((p-1)-xx)
decryptedM = (f * b) % p
print("Message: ", decryptedM)