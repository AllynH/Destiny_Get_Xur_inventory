# Destiny_Get_Xur_inventory

#Introduction:	
Using Bungies Destiny API to get Xurs inventory.
This program sends a HTTP GET request to Bungie's servers and reads Xurs inventory
It will then take the encrypted itemHash and send another request for the items full details. 
For details on how to use this code, visit:
http://allynh.com/blog/creating-a-python-app-for-the-destiny-api/

#Usage:
python Get_Xur_inventory.py
#Created by:
Allyn Hunt - www.AllynH.com

#Important note:
This code will only work from 10am Friday morning to 10am Sunday morning!
The user will need to fill in the value of their X-API-Key in the Get_Xur_inventory.py file:
HEADERS = {"X-API-Key":'<YOUR-X-API-Key>'}
