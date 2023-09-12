#Lüfterüberwachung

a = 1 #Lüfter aus
b = 0 #Lüfter an
c = 1 #Lüfter aus

if a == 0 and b == 0 and c == 0:
    green = 1
else:
    green = 0

if a == 1 and b == 0 and c == 0 or b == 1 and a == 0 and c == 0 or a == 0 and b == 0 and c == 1:
    yellow = 1
else:
    yellow = 0

if a == 0 and b == 1 and c == 1 or b == 0 and a == 1 and c == 1 or c == 0 and a == 1 and b == 1:
    red = 1
else:
    red = 0

print("Lüfter aus:", a)
print("Lüfter an:", b)
print("Lüfter aus:", c)
print("---------------")
print("Grün:", green)
print("Gelb:", yellow)
print("Rot:", red)
print("---------------")
print("")
print("")
print("")
print("")