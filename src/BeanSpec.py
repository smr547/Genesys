#!/usr/bin/env python3
#
# Specification of a Bean class
# 
# An Entity Bean is a class which represents a single Entity in an objedt Model. These are 
# key element in the "M" part of MVC
#
# Instances of this class are inputs to the code generation process.
#
# At present this is a very simple Bean class implementing very few properties. It is hope
# that the BeanSpecification class will evolve to support a full object-relational model.
# 
# Current capabilities:
#
# 1. Named entity
# 2. List of properties (fields)
# 3. Each field has name, type and boolean states (nullable, unique, autoId, searchable) 
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
        self.relations = set(())

    def _addRelation(self, relation):
        self.relations.add(relation)

    def __str__(self):
        # return json.dumps(self.__dict__, ensure_ascii=False, default=vars)
        s =  "{name: \"" + self.name + "\", fields: ["
        for f in self.fields:
            s += f.__str__()
        s += "], relations: {"
        for r in self.relations:
            s += r.id + ", "
        s += "]}"
        return s
    
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
