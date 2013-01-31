#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tests import test_types, test_generator

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_types)
suite.addTests(loader.loadTestsFromModule(test_generator))

unittest.TextTestRunner(verbosity=2).run(suite)
