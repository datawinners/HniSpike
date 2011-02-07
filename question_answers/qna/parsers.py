import re

class ParserBase():
    def __init__(self, regex_pattern):
        self.__regex_pattern = regex_pattern
        self.__regex = re.compile(self.__regex_pattern)

    def matches(self, ruleValue):
        searchResult = self.__regex.search(ruleValue)
        return [] if searchResult == None else list(searchResult.groups())

class NumericParser(ParserBase):
    def __init__(self):
        ParserBase.__init__(self, "^(\d+)$")

    def validateFor(self,ruleValue,value,):
        return True if self.matches(str(value)) else False
                
class RangeParser(ParserBase):
    def __init__(self, data_type):
        ParserBase.__init__(self, "^(\d+[.]?\d*)-(\d+[.]?\d*)$")
        self.data_type = data_type

    def validateFor(self, ruleValue, value):
        match=self.matches(ruleValue)
        if not match: return  False
        return self.data_type(match[0])<= self.data_type(value)<= self.data_type(match[1])

class MinRangeParser(RangeParser):
    def validateFor(self, ruleValue, value):
        match=self.matches(ruleValue)
        if not match: return  False
        return self.data_type(match[0])<= self.data_type(value)

class MaxRangeParser(RangeParser):
    def validateFor(self, ruleValue, value):
        match=self.matches(ruleValue)
        if not match: return  False
        return self.data_type(match[1])>= self.data_type(value)

        
class ParserFactory():
    def __init__(self, datatype=int):
        self._parser = dict({"0":NumericParser(),
                             "0-0":RangeParser(datatype),
                             "x-0":MinRangeParser(datatype),
                             "0-x":MaxRangeParser(datatype)
                             })

    def get_parser(self, rule_pattern):
        return self._parser[rule_pattern]


