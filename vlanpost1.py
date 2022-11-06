''' 
    Aruba AOS-CX switch, Model 6300 is REST-API framework capable. Here rest v10.04 is used to make REST calls to the switch from a PC.
    Programs does following basic function:
    1. Takes switch remote login username and password, login to switch using POST call
    2. Adds vlan 41 to the existing list of vlans in switch. We need to know the correct API URL. URL was used from AOS-CX REST API Reference which is based on Swagger 3.0 UI(uses openapi.json).
    3. Uses .json() method to print the list of vlans in amore human friendly format.
    
'''
#import required modules

import requests
import getpass
import json

import urllib3
urllib3.disable_warnings()

#Ask user to enter switch login credentials
username = input('Enter username: ')
password = getpass.getpass()
#REST URL as defined in AOS-CX REST API Reference
baseurl = 'https://172.16.40.2/rest/v10.04/'

#Store credentials and vlan41 in a dictionary
creds = {'username': username, 'password': password}
vlan41 = {'id': 41, 'name': 'ubuntu-python'}

#Use requests library to make REST call.
store = requests.session()

#Use POST method to login to switch and print the login status(200 for success)
login = store.post(baseurl + 'login', params=creds, verify=False)
print("Login Status: ", login.status_code)

#Use POST method to make changes to switch configuration, also serialize the vlan data to JSON
vlanpost = store.post(baseurl + 'system/vlans', data=json.dumps(vlan41), verify=False)
print("VLAN-POST Status: ", vlanpost.status_code)

#prints formatted vlan table
vlanget = store.get(baseurl + 'system/vlans?depth=2', verify=False)


# Use .json() method to deserialize the text output, use in-built __iter__ to iterate over dictionary keys of vlanget.json() and print key:value pairs in required format. 
for key in vlanget.json():
# print("key=",key)
 print('ID:{:<5} NAME:{}'.format(key,vlanget.json()[key]['name']))

# Use POST method to logout out of the switch. 
logout = store.post(baseurl + 'logout', verify=False)
print("Logout Status: ", logout.status_code)
