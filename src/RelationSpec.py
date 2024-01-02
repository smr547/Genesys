#!/usr/bin/env python3
# Specification of relationship involving two Entity Beans (potentially of the same type)
#
# A Relationship 
#
# 1. is identified by it's R number (e.g. R1, R2, R3)
# 2. has two ends 
# 3. Optionally has an AssociationBean (providing additional information about the relationship instance)
#
#------------------------------------

from enum import Enum
from BeanSpec import BeanSpec, FieldSpec, FieldType

def toCamel(aString):
    return aString[0:1].lower() + aString[1:]

class RelationshipEnd:

    def __init__(self, beanSpec, clause="no clause specified", mandatory=False, multiple=False):
        self.beanSpec = beanSpec  # the Entity at this end of the relationship
        self.clause = clause
        self.mandatory = mandatory
        self.multiple = multiple
        self.relationship = None
        
    def _setRelationship(self, relationship):
        self.relationship = relationship

class AssociationBean(BeanSpec):

    def __init__(self, relationship, name, fields=[]):
        self.relationship = relationship
        super(AssociationBean, self).__init__(name, fields)

class Relationship:

    def __init__(self, id, end0, end1, associationBean=None):
        self.id = id
        self.end0 = end0
        self.end1 = end1
        if end0.multiple and end1.multiple and associationBean is None:
            raise ValueError("AssociationBean required for " + id)
        self.associationBean = associationBean
        end0._setRelationship(self)
        end1._setRelationship(self)
        end0.beanSpec._addRelation(self)
        end1.beanSpec._addRelation(self)

    def isReflexive(self):
        return self.end0.beanSpec.name == self.end1.beanSpec.name


    def generate(self):

        # synthesise a Bean from a Relationship

        fs = []
        fs.append(FieldSpec(name="id", type=FieldType.INT, notNull=True, unique=True, autoId=True, searchable=True))
        if self.isReflexive():
            fs.append(FieldSpec(name=toCamel(self.end0.beanSpec.name)+"_0_id", type=FieldType.INT, notNull=True, unique=False, autoId=False, searchable=False))
            fs.append(FieldSpec(name=toCamel(self.end1.beanSpec.name)+"_1_id", type=FieldType.INT, notNull=True, unique=False, autoId=False, searchable=False))
        else:
            fs.append(FieldSpec(name=toCamel(self.end0.beanSpec.name)+"_id", type=FieldType.INT, notNull=True, unique=False, autoId=False, searchable=False))
            fs.append(FieldSpec(name=toCamel(self.end1.beanSpec.name)+"_id", type=FieldType.INT, notNull=True, unique=False, autoId=False, searchable=False))
        if self.associationBean is not None:
            for spec in self.associationBean.fields:
                if spec.name != "id":
                    fs.append(spec)
        bean = BeanSpec(self.id, fs)
        bean.generate()
