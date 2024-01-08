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

############################################
def list_sitegroups():
    import requests
    import os
    import json
    import sys
    APIKEY = os.environ.get('MistAPIKey')

    header = {
        'Authorization': 'Token ' + APIKEY,
        'Content-Type' : "application/json",
    }

    site = input('Enter the site number: ')
    site = str(site).rjust(5,'0')

    allsites = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/sites'
    response = requests.get(allsites, headers=header, verify=False)

    output = response.json()
    name = "0"
    for line in output:
        if site in line['name']:
            name = line['name']
            groups = line['sitegroup_ids']

    if name == "0":
        print("Unable to find the specified site")
        sys.exit()
    allsitegroups = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/sitegroups'
    response = requests.get(allsitegroups, headers=header, verify=False)
    output = response.json()
    print(name + ' is assigned to the following site groups:')
    for group in groups:
        for line in output:
            if(line['id'] == group):
                print(line['name'])

###################################################################
def add_sitegroup():
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

    site = input('Enter the site number: ')
    site = str(site).rjust(5,'0')


    print("")
    print('Select a site group (1-9): ')
    print('(1) - Profile 1`')
    print('(2) - Profile 2')
    ChosenProfile = input('Enter your selection: ')

    if ChosenProfile == '1':
        ProfileID = '2222'
    elif ChosenProfile == '2':
        ProfileID = '1111'
    else:
        print('The option selected does not exist')
        sys.exit()


    allsites = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/sites'
    response = requests.get(allsites, headers=header, verify=False)

    sitecheck = "0"
    output = response.json()
    for line in output:
        if site in line['name']:
            sitecheck = line['name']
            groups = line['sitegroup_ids']
            SiteID = line['id']
    if sitecheck == "0":
        print("Unable to find the specified site")
        sys.exit()

    if isinstance(groups, str):
        groups = [groups]
    else:
        pass
    groups.append(ProfileID)
    groups = list(dict.fromkeys(groups))
    addgroups = {"sitegroup_ids" : groups}


    SiteEndpoint = 'https://api.gc1.mist.com/api/v1/sites/' + SiteID
    response = requests.put(SiteEndpoint, headers=header, verify=False, data=json.dumps(addgroups))

    output = response.json()
    print('You have successfully updated the site group for site ' + sitecheck)


################################################################################
    
def remove_sitegroup():
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

    site = input('Enter the site number: ')
    site = str(site).rjust(5,'0')

    print("")
    print('Select a site group (1-9): ')
    print('profile 1')
    print('profile 2')

    ChosenProfile = input('Enter your selection: ')

    if ChosenProfile == '1':
        ProfileID = '2222'
    elif ChosenProfile == '2':
        ProfileID = '1111' 
    else:
        print('The option selected does not exist')
        sys.exit()

    allsites = 'https://api.gc1.mist.com/api/v1/orgs/<org ID>/sites'
    response = requests.get(allsites, headers=header, verify=False)

    sitecheck = "0"
    output = response.json()
    for line in output:
        if site in line['name']:
            sitecheck = line['name']
            groups = line['sitegroup_ids']
            SiteID = line['id']
    if sitecheck == "0":
        print("Unable to find the specified site")
        sys.exit()

    if isinstance(groups, str):
        groups = [groups]
    else:
        pass
    try:
        groups.remove(ProfileID)
    except:
        print("You cannot remove the site group (" + ProfileID + ") because it is currently not assigned to " + sitecheck)
        sys.exit()
    groups = list(dict.fromkeys(groups))
    addgroups = {"sitegroup_ids" : groups}


    SitenEndpoint = 'https://api.gc1.mist.com/api/v1/sites/' + SiteID
    response = requests.put(SitenEndpoint, headers=header, verify=False, data=json.dumps(addgroups))

    output = response.json()
    print('You have successfully updated the site group for site ' + sitecheck)

