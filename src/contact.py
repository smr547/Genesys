import json
from operator import attrgetter
import time
from threading import Thread
from random import random


# ========================================================
# Contact Model
# ========================================================
PAGE_SIZE = 100

class Contact:
    # mock contacts database
    db = {}
    
    # Constructor

    def __init__(self, id=None, first=None, last=None, phone=None, email=None):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.errors = {}

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    # Update

    def update(self, id, first, last, phone, email):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def save(self):
        # perform validation

        if not self.validate():
            return False    # refuse to save if invalid

        # auto ID generation -- currently mandatory for all Beans
  

        if self.id is None:
            if len(Contact.db) == 0:
                max_id = 0
            else:
                max_id = max(instance.id for instance in Contact.db.values())
            self.id = max_id + 1
            Contact.db[self.id] = self
  
  
  
  
  
        Contact.save_db()           # commit database to permanent store
        return True                    # indicate successful save

    # delete a Contact
    def delete(self):
        del Contact.db[self.id]     # remove from in memory database
        Contact.save_db()           # commit database to permanent store

    
    @classmethod
    def count(cls):
        time.sleep(2)
        return len(cls.db)

    @classmethod
    def all(cls, page=1):
        page = int(page)
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def load_db(cls):
        with open('contact.json', 'r') as contact_file:
            contacts = json.load(contact_file)
            cls.db.clear()
            for object in contacts:
                c = Contact(object['id'], object['first'], object['last'], object['phone'], object['email'])
                cls.db[c.id] = c

    @staticmethod
    def save_db():
        out_arr = [instance.__dict__ for instance in Contact.db.values()]
        with open("contact.json", "w") as f:
            json.dump(out_arr, f, indent=2)

    @classmethod
    def find(cls, id_):
        id_ = int(id_)
        c = cls.db.get(id_)
        if c is not None:
            c.errors = {}

        return c

    def validate(self):
    
        # Non null constraints
  
  
        if not self.first:
            self.errors['first'] = "first Required"
  
  
        if not self.last:
            self.errors['last'] = "last Required"
  
  
        if not self.phone:
            self.errors['phone'] = "phone Required"
  
  
        if not self.email:
            self.errors['email'] = "email Required"
  

         # Unique constraints
  
  
  
  
        existing_phone = next(filter(lambda c: c.phone == self.phone, Contact.db.values()), None)
        if existing_phone:
            self.errors['phone'] = "phone Must Be Unique"
  
  
        existing_email = next(filter(lambda c: c.email == self.email, Contact.db.values()), None)
        if existing_email:
            self.errors['email'] = "email Must Be Unique"
  


         
        return len(self.errors) == 0
