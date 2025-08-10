"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""
def canVisitAllRooms_ver1(rooms):
    IsRoomVisted = [False] * len(rooms)
    IsRoomVisted[0] = True
    rooms_to_enter = [0]

    while rooms_to_enter:
        current_room_key = rooms_to_enter.pop() # Note pop
        future_room_keys = rooms[current_room_key]
        for future_key in future_room_keys:
            if not IsRoomVisted[future_key]:
                IsRoomVisted[future_key] = True
                rooms_to_enter.append(future_key)
    return all(IsRoomVisted)

def canVisitAllRooms_ver2(rooms):
    keys = rooms[0]
    visited = [0]

    while keys:
        key = keys.pop()
        if key not in visited:
            next_set_of_keys = rooms[key]
            keys.extend(next_set_of_keys)
            visited.append(key)
    return len(visited) == len(rooms)

if __name__ == "__main__":
    # rooms are two dimensional array
    print(canVisitAllRooms_ver1([[1],[2],[3],[]]))
    print(canVisitAllRooms_ver2([[1],[2],[3],[]]))
    print("---"*10)

    print(canVisitAllRooms_ver1([[1,3],[3,0,1],[2],[0]]))
    print(canVisitAllRooms_ver2([[1,3],[3,0,1],[2],[0]]))
    print("---"*10)

    print(canVisitAllRooms_ver1([[1,3],[3,0,1],[2],[2]]))
    print(canVisitAllRooms_ver2([[1,3],[3,0,1],[2],[2]]))