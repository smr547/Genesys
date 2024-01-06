

class Domain(object):
    def __init__(self, name="My Application", classes=[], relationships=[]):
        self.name = name
        self.classes = classes
        self.relationships = relationships

    def __str__(self):
        return "Application: " + self.name + \
               " has " + str(len(self.classes)) + " domain classes" + \
               " and " + str(len(self.relationships)) + " relationships"


    def generateCode(self):

        for bean in self.classes:
            print(bean)
            bean.generate()

        for relationship in self.relationships:
            print(relationship)
            relationship.generate()
