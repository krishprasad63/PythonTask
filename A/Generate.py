import os 
import secrets
import random
import string
ext = ['.txt','.doc','.xls','.py','.c','.html','.ppt','.cpp','.css','.js']

#Write any fixed address, as per your choice and create a new folder named 'random' in the path
'''For simplicity, go to your c file then users then your respective name file, and then create folder name PythonTask.
Copy this address and set it to fixed_address variable. Now, in 'PythonTask' folder create folder named 'random'.
This code will be generating n files of random extension from the ext list give above.'''

fixed_address = 'C:/Users/krish/PythonTask'
folder_path = fixed_address +'/random' 

# 'n' is number of file to be generated
n = 1000
for i in range(n):
    k = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    a = secrets.choice(ext)
    file_name = k+a 
    file_path = os.path.join(folder_path, file_name) 

    with open(file_path, 'w') as f: 
        f.write('This is an example file.') 


