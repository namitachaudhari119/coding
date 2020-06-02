# weapons = [0, 1, 1, 0, 1, 0]
# soldiers = [1, 1, 1, 0, 1, 0]

# weapons = [0, 0, 1, 0]
# soldiers = [1, 0, 0, 0]

weapons = [1, 0, 1, 0]
soldiers = [0, 0, 0, 0]

total_soldiers = len(soldiers)

while True and soldiers and weapons:
    # pop weapon from the stack
    # deque soldier from the queue
    soldier = soldiers.pop(0)
    weapon = weapons.pop(0)
    if soldier == weapon:
        total_soldiers = len(soldiers)
    else:
        soldiers.append(soldier)
        weapons.insert(0, weapon)
        total_soldiers -= 1
        if total_soldiers == 0:
            break

print("{} number of soldier(s)".format(len(soldiers)))
