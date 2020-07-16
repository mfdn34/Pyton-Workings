def parrot_trouble(talking, hour):
    if talking == True and (hour < 6 or hour >21):
        return True
    else:
        return False

print(parrot_trouble(True, 5))
print(parrot_trouble(True, 8))
print(parrot_trouble(False, 22))