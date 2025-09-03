import sys

print(' user given input is: ', sys.argv[1:])

states = []
capitals = []

for string in sys.argv[1:]:
    temp_list = string.split(' ')
    states.append(temp_list[0])
    capitals.append(temp_list[1])

print('-' * 30)
print(' %-15s %-15s' % ('State', 'Capital'))
print('-' * 30)
for i in range(len(states)):
    print(' %-15s %-15s' % (states[i], capitals[i]))

