from os import system
user = {
    'username': 'johny777', 
    'online'  : True, 
    'email'   :'johny777@lucky.me', 
    'rating'  : 10000000000,
    'friend'  : [
       'marry888',
        'candy001',
        'peter99'
       ]
}
###### Add new friends
control = True
while control:
    system('cls')
    new_friend = input('Add new friend: ')
    
    if new_friend =='':
        control = False
        input('press enter to exit')
    user['friend'].append(new_friend)

#####Rating Print condition
if user['rating'] == 0:
    user['rating'] = "No Likes"
elif 0 <user['rating'] <1000:
    user['rating']= user['rating']
elif 999<user['rating'] <1000000:
    user['rating']= int(user['rating']/ 1000)    
    user['rating'] =str(user['rating'])+ '' + "K likes"
elif 999999<user['rating'] <1000000000:
    user['rating']= int(user['rating']/ 1000000)    
    user['rating'] =str(user['rating'])+ '' + "M likes"
else:
    user['rating']= int(user['rating']/ 1000000000)    
    user['rating'] =str(user['rating'])+ '' + "T likes"
print(user['username'])
print(user['email'])
print(user['rating'])
print('FRIENDS LIS: ')
for i in range(len(user['friend'])):
    print('>>',user['friend'][i])

