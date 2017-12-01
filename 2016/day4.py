day4 = open("day4.txt")
rooms = day4.readlines()
totalsum = 0

letters = "abcdefghijklmnopqrstuvwxyz"

def most_common(lst):
    return max(set(lst), key=lst.count)

for room in rooms:
    room = room.lower()
    room = room.rstrip()
    encrypted = room[:-11]
    checksum = room[-6:-1]

    if(most_common(encrypted) == checksum[0]):
        encrypted = encrypted.replace(checksum[0], "")
        if(most_common(encrypted) == checksum[1]):
            encrypted = encrypted.replace(checksum[1], "")
            if(most_common(encrypted) == checksum[2]):
                encrypted = encrypted.replace(checksum[2], "")
                if(most_common(encrypted) == checksum[3]):
                    encrypted = encrypted.replace(checksum[3], "")
                    if(most_common(encrypted) == checksum[4]):
                        print(room[-10:-7])
                        totalsum += int(room[-10:-7])
    

print(totalsum)