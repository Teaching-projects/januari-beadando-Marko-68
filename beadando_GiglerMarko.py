#Ez a program megnézi, hogy milyen Poker sorod van.

a = ("A" "K" "Q" "J" "10")  #Royal Flush
b = ("10" "9" "8" "7" "6") #Straight Flush
c = ("Q" "Q" "Q" "Q" "5")  #Four of a King
d = ("A" "A" "A" "K" "K")  #Full House
e = ("K" "8" "6" "4" "2")  #Flush
f = ("8" "7" "6" "5" "4")  #Straight
g = ("Q" "Q" "Q" "7" "2")  #Three of a King
x = ("J" "J" "9" "9" "5")  #Two Pair
y = ("K" "K" "9" "8" "4")  #One Pair
z = ("A" "Q" "6" "4" "2")  #High Card

sor = input("Add meg a sorodat(Egybe nagybetűkkel) : ")

if a in sor:
    print("Royal Flush")
    print("Ezzel elversz mindenkit.")
elif b in sor:
    print("Straight Flush")
elif c in sor:
    print("Four of a King")
elif d in sor:
    print("Full House")
elif e in sor:
    print("Flush")
elif f in sor:
    print("Straight")
elif g in sor:
    print("Three of a King")
elif x in sor:
    print("Two Pair")
elif y in sor: 
    print("One Pair")
elif z in sor:
    print("High Card")
else:
    print("Ezzel a sorral nincs nagy esélyed.")
