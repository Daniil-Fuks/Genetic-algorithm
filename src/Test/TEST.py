f = open('settings.txt', mode='r', encoding='UTF-8').read().splitlines()

print(f)
print(f[0].split('|'))