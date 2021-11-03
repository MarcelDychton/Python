'''Kurs programowania w Python'''


# print("hello") 

# """Tworzenie pojdeynczego gracza"""
# Player = {
#     "nick": "Ziom",
#     "level": 100,
#     "speed": 2,
#     "hp":100,
# }
# # print("Gracz "+Player["nick"]+" ma poziom "+str(Player["level"])) 
# """Lista graczy"""
# arr = [
#     {
#     "nick": "Ziom",
#     "level": 100,
#     "speed": 2,
#     "hp":100,
# },
# {
#     "nick": "Ziom2",
#     "level": 80,
#     "speed": 1,
#     "hp":120,},
#     ]
# print (arr[0]["nick"]  +" ma poziom "+str(arr[0]["level"])+ " a "+arr[1]["nick"] +" poziom "+str(arr[1]["level"]))
# arr.append({
#     "nick": "Ziom3",
#     "level": 180,
#     "speed": 4,
#     "hp":115,})
# # print(arr)
# arr.pop()
# print(arr)
"""Tworzenie kolejki"""
# from collections import deque
# import collections 
# queue = deque(arr)
# queue.append({"nick": "Ziom4",
#     "level": 15,
#     "speed": 4,
#     "hp":115})
# # print(queue)
# queue.popleft()
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
'''Zadanie z rollercoasterem - kilka wariantów'''
# Rollercoaster = [
#     " Zosia ",
#     " Franek ",
#     " Marcin " ,
#     " Bogdan ",
#     " Maciek ",
# ]
'''Pierwszy zjeżdza i idzie na koniec kolejki (każdy ma zjechać)'''
# from collections import deque
# queue = deque(Rollercoaster)

# for p in Rollercoaster :
    # first_in_queue = queue[0]
#     queue.popleft()
#     print(queue)
#     queue.append(first_in_queue)
#     print(queue)
'''Kolejka ma zjechać po dwa razy'''
# for p in range(len(Rollercoaster)*2):
#     first_in_queue = queue[0]
#     queue.popleft()
#     queue.append(first_in_queue)
#     print(queue)
# for p in range(len(Rollercoaster)*2):
#     first_in_queue = queue[0]
#     if first_in_queue == " Maciek ":
#         break
#     queue.popleft()
#     queue.append(first_in_queue)
#     print(queue)
'''Marcin ma zjechac raz ale za drugim już nie jak jest pierwszy'''
# was_there=False
# for p in range(len(Rollercoaster)*2):
#     first_in_queue = queue[0]
#     if first_in_queue == " Marcin " and was_there:
#         break
#     queue.popleft()
#     if first_in_queue == " Marcin ":
#         was_there=True
#     queue.append(first_in_queue)
#     print(queue)
# 
users = [ 
    {
     "name": "Wacek",
     "level": 10,
     "wins": 0 ,},
     {
     "name": "Jarek",
     "level": 8,
     "wins": 0 ,},
     {
     "name": "Andrzej",
     "level": 1,
     "wins": 0 ,},
     {
     "name": "Zbyszek",
     "level": 15,
     "wins": 0 ,},
     {
     "name": "Tomek",
     "level": 4,
     "wins": 0 ,},
     {
     "name": "Mateusz",
     "level": 5,
     "wins": 0 ,}
 ]
from collections import deque
queue = deque(users)
# for p in (queue) :
#     first_in_queue = queue[0]
#     if lista_graczy[0]["level"]>lista_graczy[1]["level"]:
#         lista_graczy[0]["wins"]=+1
#         lista_graczy[1]["wins"]=-1
#     if lista_graczy[0]["level"]<lista_graczy[1]["level"]:
#         lista_graczy[0]["wins"]=-1
#         lista_graczy[1]["wins"]=+1
#     if lista_graczy[0]["level"] == lista_graczy[1]["level"]:
#         queue.popleft()
#         queue.append(first_in_queue)
# print(queue)
users_deque = deque(users)
for u in users:
  users_deque.popleft()
  for i in users_deque:
    if users_deque[0]["level"]>users_deque[1]["level"]:
        users_deque[0]["wins"]=+1
        users_deque[1]["wins"]=-1
    if users[0]["level"]<users_deque[1]["level"]:
        users_deque[0]["wins"]=-1
        users_deque[1]["wins"]=+1
    
print(users) 
