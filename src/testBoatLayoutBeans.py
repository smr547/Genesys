#!/usr/bin/env python3
#
# Generate Python code BoatLayout entity Bean
#----------------------------------------
from BeanSpec import *
from RelationSpec import AssociationBean, RelationshipEnd, Relationship


if __name__ == "__main__":

# Region 

    entityName = "Region"
    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("name", FieldType.STRING, True, False)
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
        FieldSpec("name", FieldType.STRING, True, False), \
        FieldSpec("regionId", FieldType.STRING, True, True)
        ]

    spaceBean = BeanSpec(entityName, fieldlist)


# Relationship R2
    end0 = RelationshipEnd(spaceBean, "groups together", False, True)
    end1 = RelationshipEnd(regionBean, "is part of", True, False)
    r2 = Relationship("R2", end0, end1, None) 



# Generate code

    for bean in [regionBean, accessTypeBean, spaceBean]:
        with open(bean.name +".py", "w") as outfile:
            print(bean)
            outfile.write(bean.generate())

