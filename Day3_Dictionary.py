monthConversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"november",
    "Dec":"December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv","Not a Valid Key"))
"key can be string or number"


"While loop"
i=1
while i<=10:
    print(i)
    i=i+1
    print("Done with loop")

i=1
while i<=10:
    print(i)
    i=i+1
print("Done with loop")

"Build a guess game"

secret_word = "giraffe"
guess=""
while guess != secret_word:
    guess = input("Enter guess: ")
print("You win!")


secret_word = "giraffe"
guess=""
guess_count =0
guess_limit =3
out_of_guess= False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
       guess = input("Enter guess: ")
       guess_count +=1
    else:
       out_of_guess =True

if out_of_guess:
    print("Out of Guesses, You Lose!")
else:
    print("You win!")


secret_word = "giraffe"
guess=""
guess_count =0
continue_guess= True

while guess != secret_word and continue_guess:
    if guess_count < 3:
       guess = input("Enter guess: ")
       guess_count +=1
    else:
       continue_guess = False

if not(continue_guess):
    print("Out of Guesses, You Lose!")
else:
    print("You win!")


