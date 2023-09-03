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
