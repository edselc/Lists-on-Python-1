
import random
import sys
import os

name = 'edsel'

grocery_list = ['milk', 'tea', 'juice', 'coffe', 'softdrink']
clean_list = ['sweep', 'floor', 'window', 'car', 'roof',]
to_do_list = [grocery_list,clean_list] #combine two lists into a list


print (grocery_list) #print the grocery list
print(clean_list,"\n"*2) #print the clean lists

print('first grocery item is', grocery_list[0]) #displaying the first item on the grocery list. index 0
print ('last item on grocery list is',grocery_list[4],'\n'*2) #displaying the last itme on the grocery list index 4

print(to_do_list) # print the combined lists
to_do_list.sort() # ".sor" comand is used to sort the items on a list on order
print ('to_do_lists is now sorted. results shown next line')
print(to_do_list) # print the combined lists
print('first item to do on the second list is to',to_do_list[1][0])# displaying the first item index[0] on the second[1] list
to_do_list.append('bike') # '.append' command adds a object on the last part of the list
print (to_do_list)
to_do_list.clear() # '.clear()' command clears all the item on the lists
print (to_do_list)
to_do_list = [grocery_list,clean_list] #combining again the two lists into a list
grocery_list.append('Super Tocino')
print (grocery_list)
clean_list.append('clean bathroom')
print (clean_list)

print (grocery_list[5].split()[0]) #displaying the first word on the grocery list item 'Super Tocino'
print (clean_list[5].split()[-1]) # displaying the second word on the clean list item 'clean bathroom'

for item in to_do_list: #getting the a item on to_do_list
    print(item[5].split()[0]) #displating both first word the grocery list and clean list

