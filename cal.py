# from datatypes import add, subtr, div, mul





# def new_funct(a, b):
#     add_new = add(a,b)
#     subtr_new = subtr(a,b)
#     div_new = div(a,b)
#     mul_new = mul(a,b)
#     return add_new, subtr_new, div_new, mul_new
# var1 = new_funct(10,5)
# print(var1)


#create a function called make_album
# def make_album (*Album):
#     Print()

# make_album("Mariah Carey", "buterfly")
# make_album("Celine Dion", "a new day has come")
# make_album("Beyonce", )

"""
Problem statement
1. create the function with name make_album
2. function should take in parameters: Artist_name, album_title
3. Return a dict. with keys, album_name and album_title
4. Call the function 3times to create 3 diff. albums
5. print each return value

Version 2
1. Add parameter thats the album tracks tracks_numb
2. call function and include the number of tracks

"""

# def make_album(artist_name, album_title):
#     album = {
#         "artist": artist_name,
#          "title": album_title
#          }
#     return album

# album1 = make_album("Beyonce", "Lemonade")
# album2 = make_album("Mariah carey", "Butterfly")
# album3 = make_album("Celine Dion", "A new day has come")

# print(album1)
# print(album2)
# print(album3)

# from datetime import date

# today = date.today()
# print("Today's date:", today)

# from datetime import datetime

# datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

import glob, os
file = os.getcwd()

print(file)