import random
import string
import sys

key = "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"
def generateKey(key):
    finalKey= []
    mix = string.ascii_uppercase + string.digits
    for x in [char for char in key]:
        if x =='X':
            x = random.choice(mix)
            finalKey.append(x)
        else:
            finalKey.append("-")
    finalKey = "".join(finalKey)
    return finalKey
print(generateKey(sys.argv[1]))