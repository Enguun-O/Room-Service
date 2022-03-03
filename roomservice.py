"""
This program...
Made by ...
"""

guests = {'1':'Jonathan', '2': 'Joseph', '3': 'Jotaro'}
correct_info = False
room = input ('Pleae, enter your room number: ')
if room in guests.keys():
    correct_info = True
else:
    correct_info = False
name = input ('Please, enter your name: ') 
if correct_info and guests[room].lower()==name.lower():
    correct_info = True
    print('Correct')
else:
    correct_info = False
    print('Incorrect')
