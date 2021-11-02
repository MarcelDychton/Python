# print("hello") 
Player = {
    "nick": "Ziom",
    "level": 100,
    "speed": 2,
    "hp":100,
}
# print("Gracz "+Player["nick"]+" ma poziom "+str(Player["level"])) 
arr = [
    {
    "nick": "Ziom",
    "level": 100,
    "speed": 2,
    "hp":100,
},
{
    "nick": "Ziom2",
    "level": 80,
    "speed": 1,
    "hp":120,},
    ]
# print (arr[0]["nick"]  +" ma poziom "+str(arr[0]["level"])+ " a "+arr[1]["nick"] +" poziom "+str(arr[1]["level"]))
arr.append({
    "nick": "Ziom3",
    "level": 180,
    "speed": 4,
    "hp":115,})
# print(arr)
arr.pop()
# print(arr)
from collections import deque 
queue = deque(arr)
queue.append({"nick": "Ziom4",
    "level": 15,
    "speed": 4,
    "hp":115})
# print(queue)
queue.popleft()
# print(queue)
# if queue[0]["level"] > 50:
#     print(queue[0]["nick"])
# if queue[1]["level"] > 50:
#     print(queue[1]["nick"])
# for L in queue:
#     if 50 < L["level"]:
#         print(L)
# for L in queue:
#     if 50 < L["level"]:
#         if 100 < L["hp"]:
#             print(L) 
#   Funkcje  
def addExp(player,exp=20):
    player["hp"] += exp/2 
    player["level"] += exp
    print(player["level"])
    
addExp(Player)