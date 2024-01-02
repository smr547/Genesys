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
from BeanSpec import BeanSpec

class RelationshipEnd:

    def __init__(self, beanSpec, clause="no clause specified", mandatory=False, multiple=False):
        self.beanSpec = beanSpec
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
        self.associationBean = associationBean
        end0._setRelationship(self)
        end1._setRelationship(self)
        end0.beanSpec._addRelation(self)
        end1.beanSpec._addRelation(self)
