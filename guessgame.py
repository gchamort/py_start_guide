secret = "Balou"
guess = ""

for s in secret:
    guess+="*"

while guess != secret:
    print("Mot : " + guess)
    inguess = input("Devine le mot :")
    i = 0
    for s in secret:
        if inguess[i] == secret[i]:
            guess = guess[:i] + secret[i] + guess[i+1:]
        i += 1

print("Bravo !")