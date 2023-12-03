#!/usr/bin/env python3
#
# Specification of for a Bean class
#
#------------------------------------

from enum import Enum
import json
import jinja2

class FieldType(str, Enum):
    INT: str = "int"
    STRING: str = "string"
    FLOAT: str = "float"
    EMAIL: str = "email"

class FieldSpec:

    def __init__(self, name=None, type=None, notNull=False, unique=False, autoId=False, searchable=True):
        self.name = name
        self.type = type
        self.notNull = notNull
        self.unique = unique
        self.autoId = autoId
        self.searchable = searchable

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class BeanSpec:

    def __init__(self, name=None, fields = []):
        self.name = name
        self.fields = fields

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False, default=vars)
    
    def lowerName(self):
        return lower(self.name)

    def nameTempVar(self):
        return self.lowerName[0:1]


    def generate(self):
        templateLoader = jinja2.FileSystemLoader( searchpath="../templates" )
        templateEnv = jinja2.Environment( loader=templateLoader )
        TEMPLATE_FILE = "python_bean.jinja"
        template = templateEnv.get_template( TEMPLATE_FILE )
        return template.render( self.__dict__ )
        


if __name__ == "__main__":

    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("first", FieldType.STRING, True, False), \
        FieldSpec("last", FieldType.STRING, True, False), \
        FieldSpec("phone", FieldType.STRING, True, True), \
        FieldSpec("email", FieldType.EMAIL, True, True) \
        ]

    bs = BeanSpec("Contact", fieldlist)
#    print(bs)
    print(bs.generate())

