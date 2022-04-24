K = int(input())
room_no = list(input().split(' '))
fam = set()
cap = set()
for room in room_no:
    if room not in fam:
        fam.add(room)
        cap.add(room)
    else:
        cap.discard(room)
cap = list(cap)
print(cap[0])