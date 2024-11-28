input("emoticon ")
sad = input("Enter sad emoticon: ")
happy = input("Enter happy emoticon: ")
angry = input("Enter angry emoticon: ")
evil = input("Enter evil emoticon: ")

newsad = sad.replace(":(", "😕")
newhappy = happy.replace(":)", "😸")
newangry = angry.replace(">:(", "🤬")
newevil = evil.replace(">:)", "😈")

if sad:
    print(newsad)

if happy:
    print(newhappy)

if angry:
    print(newangry)

if evil:
    print(newevil)