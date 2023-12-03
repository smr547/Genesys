#!/usr/bin/env python3
#
# Generate Python code for a simple Entity Bean in the Contacts application
#----------------------------------------
from BeanSpec import *


if __name__ == "__main__":

    fieldlist = [ \
        FieldSpec("id", FieldType.INT, True, True, True), \
        FieldSpec("first", FieldType.STRING, True, False), \
        FieldSpec("last", FieldType.STRING, True, False), \
        FieldSpec("phone", FieldType.STRING, True, True), \
        FieldSpec("email", FieldType.EMAIL, True, True) \
        ]

    bs = BeanSpec("Contact", fieldlist)
    print(bs.generate())
