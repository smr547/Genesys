#!/usr/bin/env python3

import json
# import Space, Access, AccessType, Region
from Space import * 
from Region import * 
from AccessType import * 
from Access import *
from R1 import * 
from R2 import * 
from R3 import * 


if __name__ == "__main__":

    Region.load_db()
    Space.load_db()
    R1.load_db()
    R2.load_db()
    R3.load_db()

    print("Database loaded")

    # Create Regions

    Region(None, "Shore").save()
    Region(None, "Top deck").save()
    Region(None, "Cockpit").save()
    Region(None, "Companionway").save()
    Region(None, "Galley").save()
    Region(None, "Saloon").save()
    Region(None, "Master suite").save()
    Region(None, "Port cabin").save()
    Region(None, "Engine space").save()
    Region(None, "Nav Station").save()
    Region(None, "Stern Lazarette").save()
    Region(None, "Sail Locker").save()
    Region(None, "Transom").save()
    Region(None, "Settee").save()
    Region(None, "Starboard cabin").save()
    Region(None, "Aft heads").save()
    Region(None, "Port Lazarette").save()
    Region(None, "Stb Lazarette").save()
    Region(None, "Landing").save()

    # Create access types

    accessTypes = ["Open", "Doorway", "Buttoned door", "Door", "Hatch", "Floor cover", "Drawer", \
        "Seat hatch", "Under bunk hatch", "Backrest cushion", "Seat cushion", "Passerelle"]
    for at_name in accessTypes:
       at = AccessType(None, at_name)
       if not at.save() :
           print("Errors: ", at.errors)

    shoreRegion = Region.search("Shore")[0]
    print(shoreRegion.__str__())

    shore = Space(None, "Shore")
    if not shore.save():
        print("Errors: ", shore.errors)

    r2 = R2(None, shore.id, shoreRegion.id)
    if not r2.save():
        print("Errors: ", r2.errors)
   
    transomRegion = Region.search("Transom")[0]
    print(transomRegion.__str__())

    swimDeck = Space(None, "Swim deck")
    if not swimDeck.save():
        print("Errors: ", swimDeck.errors)

    r2 = R2(None, swimDeck.id, transomRegion.id)
    if not r2.save():
        print("Errors: ", r2.errors)

    # shore to swimdeck access

    passerelle = AccessType.search("Passerelle")[0] 

    # passerelleAccess = R1(None, shore.id, swimDeck.id, passable=True)
    passerelleAccess = Access(None, shore.id, swimDeck.id, passable=True)
    if not passerelleAccess.save():
        print("Errors: ", passerelleAccess.errors)

    r3 = R3(None, passerelle.id, passerelleAccess.id)
    if not r3.save():
        print("Errors: ", r3.errors)
   
      
