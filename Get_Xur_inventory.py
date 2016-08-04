###################################################################################################
# Introduction:	This program sends a HTTP GET request to Bungie's servers and reads Xurs inventory
# 				It will then take the encrypted itemHash and send another request for the items full details. 
# 				For details on how to use this code, visit:
#				http://allynh.com/blog/creating-a-python-app-for-the-destiny-api/
#				Important note: This code will only work from 10am Friday morning to 10am Sunday morning!
#
# Usage:		python Get_Xur_inventory.py
# Created by:	Allyn Hunt - www.AllynH.com
###################################################################################################

from lxml import html
import requests
import json

# Uncomment this line to print JSON output to a file:
#f = open('output.txt', 'w')

HEADERS = {"X-API-Key":'<YOUR-X-API-Key>'}

base_url = "https://www.bungie.net/platform/Destiny/"
xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"
hashType = "6"

# Send the request and store the result in res:
print "\n\n\nConnecting to Bungie: " + req_string + "\n"
print "Fetching data for: Xur's Inventory!"
res = requests.get(xur_url, headers=HEADERS)

# Print the error status:
error_stat = res.json()['ErrorStatus']
print "Error status: " + error_stat + "\n"

# Uncomment this line to print JSON output to a file:
#f.write(json.dumps(res.json(), indent=4))

print "##################################################"
print "## Printing Xur's inventory:"
print "##################################################"

for saleItem in res.json()['Response']['data']['saleItemCategories']:
	mysaleItems = saleItem['saleItems']
	for myItem in mysaleItems:
		hashID = str(myItem['item']['itemHash'])
		hashReqString = base_url + "Manifest/" + hashType + "/" + hashID
		res = requests.get(hashReqString, headers=HEADERS)
		item_name = res.json()['Response']['data']['inventoryItem']['itemName']
		print "Item is: " + item_name
		item_type = res.json()['Response']['data']['inventoryItem']['itemTypeName']
		item_tier = res.json()['Response']['data']['inventoryItem']['tierTypeName']
		print "Item type is: " + item_tier + " " + item_type + "\n"
		