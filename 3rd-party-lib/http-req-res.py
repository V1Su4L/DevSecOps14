import requests

url = 'https://jsonplaceholder.typicode.com/usesssrs'
res = requests.get(url)  # GET request to the url and the response stored in the res variable

print(res)  # <class name and the status code>
print(res.status_code)  # get the status code of the http res

if 200 <= res.status_code < 400:  # check if the status code valid or not
    print('healthy api')
else:
    print('oooooops unhealthy api')

page_content = res.text  # return the html page

# print(type(page_content)) # str
#
# print(page_content)

data = res.json()  # new variable -> list of dict
print(type(data))  # list
print(type(data[0]))  # dict

#     v
#   [{ },{ },{ },{ }]
print(data[0])
# data[0]['key'] -> dict

# DRY

# for i in  range(len(data)): # get the user name by the index of the list
#     print(data[i]['name'])

for user in data:  # iterate over the list and user will be the alias for each dict
    print(user['name'])

for user in data:  # for each user <dict> in the data list
    print('\n----------new user--------\n')  # new liner for each user
    for k, v in user.items():  # for each key and value pair in the user dict
        if k in ['name', 'email']:  # check if the key is name or email
            print(f'{k} <==> {v}')  # print the key and the value in this formate
