import os
import string
import shutil

#Write any fixed address, as per your choice and create a new folder named 'random' in the path
''' As this code is to access, so for accessing there should be files you will be accessing. So, to generate files run Generate.py.
As you already generated the file, then you must be having fixed_address and random file inside it in which there will be files which is to be accessed. 
So, set fixed_address, same as of Generate.py and run this code.'''

fixed_address = 'C:/Users/krish/PythonTask'

folder_path = fixed_address+'/random' 

a = os.listdir(folder_path)
#print(a)

def f_ext(k):
    return k.split('.')[1]

list_ = []

for i in range(len(a)):
    if f_ext(a[i]) not in list_:
        list_.append(f_ext(a[i]))

print(list_)

for k in list_:
    new_folder =  fixed_address +'/'+ k
    if not os.path.exists(new_folder): 
        os.makedirs(new_folder) 
 
for j in range(len(a)):
    #every file will be moved from 'random' folder to the satisfying extension folders above created 
    os.rename(folder_path + a[j] , fixed_address + '/{}/{}'.format(f_ext(a[j]),a[j]))