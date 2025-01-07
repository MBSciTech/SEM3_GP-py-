class IncorrectNameError(Exception):
    def __init__(self,msg):
        self.msg = msg
class IncorrectFormulaError(Exception):
    def __init__(self,msg):
        self.msg = msg

class InvalidElementError(Exception):
    def __init__(self,msg):
        self.msg = msg

class IncorrectBondsError(Exception):
    def __init__(self,msg):
        self.msg = msg
        