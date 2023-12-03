import json
from operator import attrgetter
import time
from threading import Thread
from random import random
from contact import Contact


if __name__ == "__main__":

    print("It works")

    Contact.load_db()
    c = Contact(None, "Steven", "Ring", "+6147495268", "smr@soutshsky.com.au")
    c.save()
