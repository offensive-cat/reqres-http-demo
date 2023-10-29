import requests
import json

# global variable
url = 'https://reqres.in/api/'
headers = {"content-type": "application/json"}
payload = json.dumps({})

url_request = url + 'users'
r = requests.get(url_request)
user_data = json.loads(r.text)['data']

def user_data():
  url_request = url + 'users'
  r = requests.get(url_request)
  print(r)
  user_data = json.loads(r.text)['data']
  
  for data in user_data:
    print('\n=================================')
    print('ID   :', data['id'])
    print('EMAIL:', data['email'])
    print('NAME :', data['first_name'] + ' ' + data['last_name'])
  print('=================================')

def get_user(user_id):
  url_getId = url + 'users' + '/' + str(user_id)
  r = requests.get(url_getId)
  
  if r.status_code == 200:
    user_data = json.loads(r.text)['data']
    
    if user_id == user_data['id']:
      print('\nID   :', user_data['id'])
      print('EMAIL:', user_data['email'])
      print('NAME :', user_data['first_name'] + ' ' + user_data['last_name'])
  else:
    print("Error:", r.status_code)

def registration(email, password):
  url_register = url + 'register'
  payloads = json.dumps({
      'email': email,
      'password': password
      })
  r = requests.post(url_register, data = payloads, headers = headers)
  print('')
  print(r)
  print(r.json())

def login(email, password):
  url_login = url + 'login'
  payloads = json.dumps({
      'email': email,
      'password': password
      })
  
  r = requests.post(url_login, data = payloads, headers = headers)
  print('')
  print(r)
  print(r.json())

def edit_user(user_id, first_name, last_name, email, password):
  url_edit = url + 'users' + '/' + str(user_id)
  payloads = json.dumps(
      {'email': email,
       'first_name':first_name,
       'last_name':last_name,
       'password': password})
  
  r_code = requests.get(url_edit).status_code
  
  if r_code == 200 :
    r = requests.put(url_edit, data = payloads, headers = headers)
    print('')
    print(r.json())
  else:
    print('\nID Not Found!')

def delete_user(user_id):
  url_delete = url + 'users' + '/' + str(user_id)
  r_code = requests.delete(url_delete).status_code
  if r_code == 204:
    print('\nUSER is removed! Code:', r_code)