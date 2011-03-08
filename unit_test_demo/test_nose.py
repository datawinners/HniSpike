from nose.tools import *

def testEquals():
    assert 1==1

class A:
    def __init__(self):
        pass
    
    def raise_error(self,arg):
        raise KeyError

class TestNose:
    
    @classmethod
    def setup_class(klass):
        pass
    
    @classmethod
    def teardown_class(klass):
        pass
    
    def setup(self):
        print "setUp"
        self.a = A()
    
    def teardown(self):
        print "teardown"
        self.a = None
    
    def test_asserts(self):
        assert_equal(1+1,2)
        assert_not_equal(2,3)
        assert_raises(KeyError,self.a.raise_error,"function argument")
    
    @raises(KeyError)
    def test_raises_error(self):
        self.a.raise_error("")
   
    
    
    
    
