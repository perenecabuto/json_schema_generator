# -*- coding: utf-8 -*

from urllib2 import urlopen

from jsonschema import validate

from generator import SchemaGenerator

import json


url = 'http://api2.g1.be.qa01.globoi.com/loterias/megasena/concursos'

json_data = urlopen(url).read()
generator = SchemaGenerator.from_json(json_data)
json_schema_data = json.dumps(generator.to_dict(), indent=4)


with open('gotten_json.json', 'w') as json_file:
    json_file.write(json_data)

#with open('gotten_json_schema.json', 'w') as json_schema_file:
    #json_schema_file.write(json_schema_data)


json_object = json.load(open('gotten_json.json'))
json_schema_object = json.load(open('gotten_json_schema.json'))

validation_result = "Valido"

try:
    validate(json_object, json_schema_object)

except Exception, e:
    validation_result = "Inválido: \n\t%s" % str(e)

print validation_result
