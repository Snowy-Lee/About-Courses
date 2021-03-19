names=['Cidny','Tom','Aim','Mike']
mes="I would like to eat dinner with "+names[2]+"."
print(names[0]+" don't have time to eat with us.")

names.remove('Cidny')
names.insert(0, 'Eric')

print("I would like to eat dinner with "+names[0]+".")
print("I would like to eat dinner with "+names[1]+".")
print("I would like to eat dinner with "+names[2]+".")
print("I would like to eat dinner with "+names[3]+".")
