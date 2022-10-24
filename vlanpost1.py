import requests
import getpass
import json

#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import urllib3
urllib3.disable_warnings()

username = input('Enter username: ')
password = getpass.getpass()
baseurl = 'https://172.16.40.2/rest/v10.04/'

creds = {'username': username, 'password': password}
vlan41 = {'id': 41, 'name': 'ubuntu-python'}

store = requests.session()

login = store.post(baseurl + 'login', params=creds, verify=False)
print("Login Status: ", login.status_code)

vlanpost = store.post(baseurl + 'system/vlans', data=json.dumps(vlan41), verify=False)
print("VLAN-POST Status: ", vlanpost.status_code)

#prints formated vlan table
vlanget = store.get(baseurl + 'system/vlans?depth=2', verify=False)

#print("type of vlanget:",type(vlanget))
#x=vlanget.json()
#print('{},{}'.format(x["41"]["id"],x["41"]["name"]))
#print("vlanget.json-output",vlanget.json())
#print(type(vlanget.json()))

# vlanget.json(), allows to iterate as dictionary using keys of "key:value pair in dictionary" 
for key in vlanget.json():
 print("key=",key)
 print('ID:{:<5} NAME:{}'.format(key,vlanget.json()[key]['name']))

logout = store.post(baseurl + 'logout', verify=False)
print("Logout Status: ", logout.status_code)
