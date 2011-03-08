import sys
import os
from nose.tools import *
from formservice.models import Dictionary

class test_dictionary:

    def test_name_should_be_in_dict(self):
        d = Dictionary()

        assert d.validate("name")

    def test_address_should_not_be_in_dict(self):
        d = Dictionary()

        assert d.validate("address") == False




