#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

NAPI = "http://api.open-notify.org/astros.json"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(NAPI)

    got_dj = gotresp.json()
    ## Decode the response

    for single_item in got_dj["people"]:
    ## print the response
       #print(single_item['number'])
       print(single_item)

if __name__ == "__main__":
    main()


