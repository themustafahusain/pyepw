'''
Created on Oct 30, 2014

@author: rene
'''
import string


def normalize_field_name(internal_name):
    name = internal_name.strip().replace('/', ' or ').lower()
    name = name.replace(' ', '_')
    name = name.replace('(', '')
    name = name.replace(')', '')
    return name


def normalize_object_name(internal_name):
    name = internal_name.replace('/', ' or ').strip()
    name = string.capwords(name)
    name = name.replace(' ', '')
    return name


def normalize_object_var_name(internal_name):
    name = internal_name.strip().replace('/', ' or ').lower()
    name = name.replace(' ', '_')
    name = name.replace('(', '')
    name = name.replace(')', '')
    return name

# 
# def value2pyconv(self, vtype):
# 
#     if vtype == 'alpha':
#         return "str"
#     if vtype == 'integer':
#         return "int"
#     if vtype == 'real':
#         return "float"
#     return "str"


class DataObject:

    def __init__(self, internal_name=None):
        self.internal_name = internal_name
        self.class_name = normalize_object_name(self.internal_name)
        self.var_name = normalize_object_var_name(internal_name)
        self.fields = []


class DataField(object):

    def __init__(self, internal_name, ftype):

        self.attributes = {}
        self.internal_name = internal_name
        self.field_name = normalize_field_name(internal_name)
        self.is_list = False
        self.ftype = ftype

    def value2py(self, value, ftype):
        if ftype == 'alpha':
            return str(value)
        if ftype == 'integer':
            return str(int(value))
        if ftype == 'real':
            return str(float(value))
        return value

    def add_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def conv_vals(self):
        # Update type if not other specified
        if not "type" in self.attributes:
            if self.ftype == "A":
                self.attributes["type"] = "alpha"
            elif self.ftype == "N":
                self.attributes["type"] = "real"

        # Convert some values to python representation
        for attribute_name in self.attributes:
            if attribute_name in ["default",
                             "minimum",
                             "minimum>",
                             "maximum",
                             "maximum<",
                             "missing"]:
                value = self.attributes[attribute_name]
                self.attributes[attribute_name] = self.value2py(value,
                                                                self.attributes["type"])


class ListField(DataField):

    def __init__(self, internal_name):
        super(ListField, self).__init__(internal_name, "list")
        self.is_list = True
        self.object_name = normalize_object_name(internal_name)
        self.field_name = normalize_field_name(internal_name)