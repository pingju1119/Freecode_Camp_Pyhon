"List"
friends = ["Kevin","Karen","Jim"]
friends2 = ["Katy", 2, False]
print(friends)
print(friends[0])
print(friends2[1])
print(friends[-1])
print(friends[0:2])
print(friends[1:])
"just grabs from 0 to 1, except 2 elements in list"
friends[1]="Mike"
print(friends[1])

"list function"
lucky_numbers = [3,6,8,9,12,16]
friends = ["Kevin","Karen","Jim","Ellie","Elliott"]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Oscar")
friends.insert(1,"kelly")
friends.remove("Jim")
"friends.clear()" "clear all the elements"
"friends.pop()""remove the last element"
print(friends)

lucky_numbers = [3,6,9,8,2,12,16]
friends = ["Kevin","Karen","Jim","Ellie","Ellie","Elliott"]
print(friends.index("Ellie"))
print(friends.count("Ellie"))
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2=friends.copy()
print(friends2)

"Tuple: immutble,can't change elements"
coordinates = (4,5)
print(coordinates[0])

"Functions in python"

def say_hi():
    print("Hello, User")
say_hi()

def sayhi(name,age):
    print("Hello "+ name + ", you are " +age)
sayhi("Mike","35")
sayhi("Ellie","6")










