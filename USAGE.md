# Json Schema Generator


## Usage:

### To record

    $ json_schema_generator.py record http://somewhere.com/any.json file.json_schema

It creates file.json_schema file containing the generated json schema


### To validate

    $ json_schema_generator.py validate http://somewhere.com/any.json file.json_schema

It validates if the json validates with file.json_schema


### To create automatic test

    $ json_schema_generator.py homologate http://somewhere.com/immutable.json immutable

It should **create (or replace)**
a fixture file called **json_schemas/immutable.json_schema**
and a test file called **test_immutable_jsonschema.py**
in the current dir.

If you want to create it in another path use **--path /wanted/path/dir/**

