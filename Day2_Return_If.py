def cube(num):
    num*num*num
print(cube(3))

def cube1(num):
    return num*num*num
print(cube1(3))
print(cube1(4))
result=cube1(5)
print(result)


is_male= True

if is_male:
    print("you are a male.")
else:
    print("you are not a male.")

is_male = True
is_tall = True

if is_male and is_tall:
        print("you are a tall male.")
else:
        print("you are either not a male or not tall or both")


is_male = True
is_tall = True

if is_male or is_tall:
        print("you are a male or tall or both.")
else:
        print("you are neither a male nor tall.")


is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall male.")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a male and not tall.")

"find the max number"
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(2,40,8))
print(max_num(200,34,56))

num1=float(input("Enter first number:   "))
oper=input("Enter operator:   ")
num2=float(input("Enter second number:   "))

if oper =="+":
    print(num1+num2)
elif oper=="-":
    print(num1-num2)
elif oper=="/":
    print(num1/num2)
elif oper=="*":
    print(num1*num2)
else:
    print("invalid operator")