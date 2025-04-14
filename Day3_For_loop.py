"for loop"
for letter in "Giraffe Academy":
    print(letter)

friends=["Jim","Ellie","Elliott","Ping"]
for name in friends:
    print(name)

for index in range(10):
    print(index)

for index in range(6,8):
    print(index)

print(len(friends))
for index in range(len(friends)):
    print(friends[index])

"Exponent Function"
print(2**3)

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(2,3))
print(raise_to_power(3,4))

"2D list and Nested loop"
number_grid = [[1,3,5],
               [2,4,6],
               [7,9,11],
               [8,10]
]
print(number_grid[0][0])
print(number_grid[2][1])

"Nestex for loop"
for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)

"Build a translator"

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
           translation=translation+"g"
        else:
           translation=translation+letter
    return translation

print(translate(input("Enter a phrase1:  ")))


def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"G"
            else:
                translation=translation+"g"
        else:
             translation=translation+letter
    return translation

print(translate(input("Enter a phrase2:  ")))

"Comments"

print("Comments are fun.")
# This program is cool,hashtag is a signal of comments

# print("Comments are fun.")

# Try Except
try:
    number=int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# if we input a string it will print the Invalid Input
# to notice other than block the python.
try:
    value=10/0
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err) #use this try except to check if
    #the coding has specific error.actually not too useful
except:
    print("Invalid Input")











