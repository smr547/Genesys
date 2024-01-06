import json
import jinja2

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

        # generate app.py

        templateLoader = jinja2.FileSystemLoader( searchpath="../templates" )
        templateEnv = jinja2.Environment( loader=templateLoader )
        TEMPLATE_FILE = "app_py.jinja"
        template = templateEnv.get_template( TEMPLATE_FILE )
        with open("./generated/app.py", "w") as outfile:

            # generate derived values used in template

            derived_values = {}

            # create the template context
            ctx = {}
            ctx.update(self.__dict__)
            ctx.update(derived_values)
      
            # generate the code using the template
            outfile.write(template.render(ctx))
