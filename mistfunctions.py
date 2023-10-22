def blockmac(macaddress):
    #blocks macs
    import sys
    import os
    import requests
    import json
    import re
    APIKEY = os.environ.get('MistAPIKey')
    macaddress = str(macaddress)
    macaddress = re.sub(r'[^a-zA-Z0-9]', '', macaddress)
    if len(macaddress) != 12:
        print("You have provided an incorrect MAC address")
        sys.exit()

    header = {
        'Authorization': "Token "+ APIKEY ,
        'Content-Type' : "application/json",
    }

    endpoint = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/setting'

    response = requests.get(endpoint, headers=header)

    output = response.json()
    blacklisturl = output["blacklist_url"]

    getmacs = requests.get(blacklisturl, headers=header)
    macs = getmacs.json()
    newurl = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/setting/blacklist'
    macs.append(macaddress)
    blockmacs = {
    "macs" : macs
    }
    requests.post(newurl, headers=header, json=blockmacs)

    print(macaddress + " has been blocked successfully")



def unblockmac(macaddress):
    #unblocks macs
    import sys
    import requests
    import json
    import os
    import re
    APIKEY = os.environ.get('MistAPIKey')
    macaddress = str(macaddress)
    macaddress = re.sub(r'[^a-zA-Z0-9]', '', macaddress)
    if len(macaddress) != 12:
        print("You have provided an incorrect MAC address")
        sys.exit()

    header = {
        'Authorization': 'Token ' + APIKEY,
        'Content-Type' : "application/json",
    }

    endpoint = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/setting'

    response = requests.get(endpoint, headers=header)

    output = response.json()
    blacklisturl = output["blacklist_url"]

    getmacs = requests.get(blacklisturl, headers=header)
    macs = getmacs.json()

    newurl = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/setting/blacklist'
    macs.remove(macaddress)
    unblockmacs = {
    "macs" : macs
    }
    requests.post(newurl, headers=header, json=unblockmacs)
    print(macaddress + " has been unblocked successfully")


def showblocks():
    #lists all blocked macs
    import requests
    import os
    APIKEY = os.environ.get('MistAPIKey')
    
    header = {
        'Authorization': 'Token ' + APIKEY,
        'Content-Type' : "application/json",
    }

    endpoint = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/setting'

    response = requests.get(endpoint, headers=header)

    output = response.json()
    blacklisturl = output["blacklist_url"]

    getmacs = requests.get(blacklisturl, headers=header)
    macs = getmacs.json()
    print(macs)

def assign_device_profile():
    import requests
    import os
    import sys
    import re
    import json

    APIKEY = os.environ.get('MistAPIKey')
    header = {
        'Authorization': 'Token ' + APIKEY,
        'Content-Type' : "application/json",
    }

    MacAdd = input('Enter the AP MAC: ')
    macaddress = str(MacAdd)
    macaddress = re.sub(r'[^a-zA-Z0-9]', '', macaddress)
    if len(macaddress) != 12:
        print("You have provided an incorrect MAC address")
        sys.exit()
    print("")
    print('Select a Device Profile (1-5): ')
    print('(1) - MDO')
    print('(2) - Regional APs')
    print('(3) - Warehouse Outdoor')
    print('(4) - Warehouse Default')
    print('(5) - Warehouse Majors')
    ChosenProfile = input('Enter your selection: ')

    if ChosenProfile == '1':
        ProfileID = '<Unique Profile ID>' #profile1
    elif ChosenProfile == '2':
        ProfileID = '<Unique Profile ID>' #profile2
    elif ChosenProfile == '3':
        ProfileID = '<Unique Profile ID>' #profile3
    elif ChosenProfile == '4':
        ProfileID = '<Unique Profile ID>' #profile4
    elif ChosenProfile == '5':
        ProfileID = '<Unique Profile ID>' #profile5
    else:
        print('You have chosen an option that doesnt exist')
        sys.exit()

    JSON_With_MAC = {
    "macs" : [macaddress]
    }

    endpoint = 'https://api.gc1.mist.com/api/v1/orgs/<ORG ID>/deviceprofiles/'+ ProfileID + '/assign'
    urlreq = requests.post(endpoint, headers=header, json=JSON_With_MAC)
    APIresponse = urlreq.json()
    if APIresponse['success']:
        print('Device profile assigned successfully')
    else:
        print("Device was not assigned successfuly. The MAC address might be problematic")
