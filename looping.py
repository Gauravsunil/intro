print("LOOPING")

for i in range(1,3):
    print("today is {0} square is={1} and cube is={2} ".format(i,i**2,i**3))


print("NOW  USING INPUT FUNCTION")

name= input("ENTER YOUR NAME: ")
age= int(input("WHAT IS YOUR AGE {0}? ".format(name)))
print(age)
if age<18:
    print("You are not eligible to vote come after {0}".format(18-age))
else:
    print("You can vote")
