#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

NAPI = "http://api.open-notify.org/astros.json"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(NAPI).json()
    #print(type(gotresp))
    #print(dir(gotresp))

    #print(gotresp.keys())
    print("People in Space:", gotresp["number"])

    for astro in gotresp["people"]:
        astroname = astro["name"]
        astrocraft = astro["craft"]
        print (f"{astroname} is on the  {astrocraft}")
main()


