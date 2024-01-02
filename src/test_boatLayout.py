#!/usr/bin/env python3

import json
# import Space, Access, AccessType, Region
from Space import * 
from Region import * 
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

    r = Region.search("Shore")[0]
    print(r.__str__())

    s = Space(None, "Shore")
    if not s.save():
        print("Errors: ", s.errors)

    r2 = R2(None, s.id, r.id)
    if not r2.save():
        print("Errors: ", r2.errors)
   
