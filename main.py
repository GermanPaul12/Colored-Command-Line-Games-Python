thing_you_like = input('Thing you like ')
thing_you_hate = input('Thing you hate ')
name_of_a_pet = input('Name of an animal you know')


print(f"Hello Adventurer. It's cool that you like \033[32m {thing_you_like} \033[0m. But you don't like \033[31m {thing_you_hate} \033[0m. But as long as \033[34m {name_of_a_pet} \033[0m is oke, everything is good!")

'''
Default	0
Black	30
Red	31
Green	32
Yellow	33
Blue	34
Purple	35
Cyan	36
White	37
'''
colors = [0,30,31,32,33,34,35,36,37]

for i in colors:
  print(f"\033[{i}m Hi \033[0m")