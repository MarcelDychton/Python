'''Kurs programowania w Python'''


# print("hello") 

"""Tworzenie pojdeynczego gracza"""
Player = {
    "nick": "Ziom",
    "level": 100,
    "speed": 2,
    "hp":100,
}
# print("Gracz "+Player["nick"]+" ma poziom "+str(Player["level"])) 
"""Lista graczy"""
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
"""Tworzenie kolejki"""
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
'''Funkcja dodaje exp do levela gracza i połowe exp do hp gracza'''
# def addExp(player,exp=20):
#     '''Funkcja dodaje exp do levela gracza i połowe exp do hp gracza'''
#     player["hp"] += exp/2 
#     player["level"] += exp
# for p in arr:
#     addExp(p)
    
# print(arr)
# print((addExp.__doc__))
 
"""Funkcja range"""
# # FUNKCJE
# names = ["Jarek", "Grzesiek", "Marysia", "Piotrek","Zenon"]
# for i in range(3):
#     print(names[i])