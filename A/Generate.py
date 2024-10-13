import os 
import secrets
import random
import string
ext = ['.txt','.doc','.xls','.py','.c','.html','.ppt','.cpp','.css','.js']

#Write any fixed address, as per your choice and create a new folder named 'random' in the path
fixed_address = 'C:/Users/krish/PythonTask'
folder_path = fixed_address +'/random' 

for i in range(1000):
    k = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    a = secrets.choice(ext)
    file_name = k+a 
    file_path = os.path.join(folder_path, file_name) 

    with open(file_path, 'w') as f: 
        f.write('This is an example file.') 


