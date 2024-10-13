import os
import string
import shutil

#Write any fixed address, as per your choice and create a new folder named 'random' in the path
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
    new_folder =  fixed_address + k
    if not os.path.exists(new_folder): 
        os.makedirs(new_folder) 
 
for j in range(len(a)):
    os.rename(fixed_address+'/random/{}'.format(a[j]), fixed_address+'/{}/{}'.format(f_ext(a[j]),a[j]))