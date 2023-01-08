armor = 1
boots = input("Would you like to pickup the boots")
if boots == 'yes':
    boots = 1
    if boots == 1:
        print('you decided to pickup the boots +1 armor ')
        print('New total armor value = ', boots + armor)
else:
    print('you decided to leave the boots')

newArmor = boots + armor
print(newArmor)

shirt = input("Would you like to pickup the shirt")
if shirt == 'yes':
    shirt = 1
    if shirt == 1:
        print('you decided to pickup the shirt +1 armor ')
        print('New total armor value = ', shirt + newArmor)
else:
    print('you decided to leave the shirt')

newArmor = boots + armor
print(newArmor)

intentory_check = input()
if inventory_check == 'inventory' and (boots = 1) and (shirt = 1):
    print('boots', 'shirt')
else:
    print('empty')
