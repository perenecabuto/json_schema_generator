#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pkgutil
import tests

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for importer, modname, ispkg in pkgutil.iter_modules(tests.__path__):
    mod = __import__('tests.%s' % modname, globals(), locals(), ['*'], -1)
    suite.addTests(loader.loadTestsFromModule(mod))

unittest.TextTestRunner(verbosity=2).run(suite)
