#!/usr/bin/env python3
#
# Generate Python code BoatLayout entity Beans
#
# This script capture the Class Diagram information for the BoatLayout Domain. This 
# includes:
#
#     Main classes
#     Relationships 
#     Association classes
#  
# Python code is then generated for each class. An association class is
# then generated to implement each relationship -- regardless of whether the
# relationship is expressed as an Association Class or not
#----------------------------------------

from Domain import Domain
from BeanSpec import *
from RelationSpec import AssociationBean, RelationshipEnd, Relationship


if __name__ == "__main__":

#-----------------------------------------------------------------
#  Capture Class diagram information
#-----------------------------------------------------------------

# Region 

    entityName = "Region"
    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("name", FieldType.STRING, True, True)
        ]

    regionBean = BeanSpec(entityName, fieldlist)

# AccessType 

    entityName = "AccessType"
    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("name", FieldType.STRING, True, False)
        ]

    accessTypeBean = BeanSpec(entityName, fieldlist)

# Space 

    entityName = "Space"
    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("name", type=FieldType.STRING, notNull=True, unique=True) \
#        FieldSpec("regionId", FieldType.STRING, True, True)    # don't specify this, R2 access will be implemented by generated  getRegion() instance method
        ]

    spaceBean = BeanSpec(entityName, fieldlist)

# Access
    entityName = "Access"
    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
#        FieldSpec("accessType", FieldType.STRING, True, False), \   # don't specify this, R3 specifies it ... generate getAccessType() instance method
        FieldSpec("passable", FieldType.BOOLEAN, True, False)
        ]
    accessBean = BeanSpec(entityName, fieldlist)

# Relationship R1
    end0 = RelationshipEnd(spaceBean, "has access to", False, True)
    end1 = RelationshipEnd(spaceBean, "is accessed from", False, True)
    r1 = Relationship("R1", end0, end1, accessBean) 

# Relationship R2
    end0 = RelationshipEnd(spaceBean, "groups together", False, True)
    end1 = RelationshipEnd(regionBean, "is part of", True, False)
    r2 = Relationship("R2", end0, end1, None) 

# Relationship R3
    end0 = RelationshipEnd(accessTypeBean, "is specified by", False, True)
    end1 = RelationshipEnd(accessBean, "is part of", True, False)
    r3 = Relationship("R3", end0, end1, None) 


#-----------------------------------------------------------------
#  End of Class diagram information
#-----------------------------------------------------------------


# Generate bean code

    domain = Domain(name="Boat Layout Domain", \
            classes=[regionBean, accessTypeBean, spaceBean], \
            relationships=[r1, r2, r3])

    print(domain)
    domain.generateCode()

