from mistfunctions import blockmac
from mistfunctions import unblockmac
from mistfunctions import showblocks
from cutovermist import mistcutover
import argparse


mistscripts = argparse.ArgumentParser(description="Mist API Scripts")
mistscripts.add_argument("--blockmac", type=str)
mistscripts.add_argument("--unblockmac", type=str)
mistscripts.add_argument("--listblocks", action='store_true')
mistscripts.add_argument("--cutover", type=str)
mistargs = mistscripts.parse_args()

if mistargs.blockmac:
    macaddress = mistargs.blockmac
    blockmac(macaddress)
elif mistargs.unblockmac:
    macaddress = mistargs.unblockmac
    unblockmac(macaddress)
elif mistargs.listblocks:
    showblocks()
elif mistargs.cutover:
    site = mistargs.cutover
    mistcutover(site)
else:
    print(r"""
    Available options:
    --blockmac: <specify a MAC address to be blocked>
    --unblockmac: <specify a MAC address to be unblocked>
    --listblocks: no input is required. This will list all blocked MAC addresses within Mist
    --cutover: <specify a site number that will be converting from Cisco to Mist APs>
    """)


