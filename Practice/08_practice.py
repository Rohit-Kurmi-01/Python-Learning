Password = "vbrgieifuhieuf"

char = len(Password)

if char < 6:
    strenght = "Waek"
elif char <= 10 :
    strenght = "medium"
else:
    strenght = "strong"

print(strenght) 