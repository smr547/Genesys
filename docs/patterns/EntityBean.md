# Bean Pattern
The coding pattern used in the Contact Entity Bean ([see contact app Contact Bean](https://github.com/bigskysoftware/contact-app/blob/master/contacts_model.py)) is interesting
## Definition
1. Entity bean implemented as a top level class (no superclass)
## Constructor
1. All fields default to None in constructor
1. Id field is listed as first parameter with trailing underscore suggesting it’s value should not be set
## Error and validation handling
1. In constructor, self.errors = {} initialises an empty dictionary intended to take per property error messages
1. validate() method sets error values and returns false if errors exist
1. Note that self.errors in not re-initialised so errors might persist despite correction (bug?)
## Persistence
1. Implemented using class dictionary variable db
1. db dictionary loaded with call to class method load_db() which reads json file contacts_file (bug?)
1. and constructs a Contacts object from each entry in the list 
1. which is then stored in the db dictionary keyed by id
1. A Contact is retrieved from the db dictionary by the find() class method which also initialised the error property to an empty dictionary (bug?)
1. The Contacts database is persisted the save_db() class method which serialises each Contact to the contacts.json file
## Search
1. Implemented by class method search(cls, text)
1. Returns a list of Contacts which has “text” string in any of the fields
## Bean operations
1. Created via constructor (but not yet included in db database)
1. Retrieved via class method find()
1. Updated via instance method update()
1. Deleted via instance method delete()
1. Call to instance method save()required to validate the object, allocate a new id and save to the db database
1. save() method also saves the database to disk via a call to Contact.save_db()


