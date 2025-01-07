import Exceptions_of_IUPAC as eoi
class FormulaValidator:
    def __init__(self, formula):
        self.formula = formula
        self.elementsList = []  # List to store elements and counts
        self.validElements = ["C", "H", "O", "N", "S", "P", "Cl", "Br", "F", "I", "Ar"]
        self.valency = {"C": 4, "H": 1, "O": 2, "N": 3, "S": 2, "P": 3, "Cl": 1, "Br": 1, "F": 1, "I": 1, "Ar": 0}
        try:
            
            
            self.parseFormula()
            if self.checkValidity():
                print("The formula is valid and bonds are correctly bonded.")
                
            else:
                raise eoi.IncorrectFormulaError("The formula is Incorrect,Please check the your formula")
        except eoi.IncorrectFormulaError as e:
            print(e)
    def parseFormula(self):
        f = self.formula
        element = ""
        count = ""
        for i in range(len(f)):
            if f[i].isupper():  # Start of a new element
                if element:  # Save the previous element and its count
                    self.elementsList.append((element, int(count) if count else 1))
                element = f[i]
                count = ""
            elif f[i].islower():  # Continuation of the element symbol
                element += f[i]
            elif f[i].isdigit():  # Count of the current element
                count += f[i]
        if element:  # Add the last element
            self.elementsList.append((element, int(count) if count else 1))

    def checkValidity(self):
        # Ensure all elements are valid
        try:
            for element, count in self.elementsList:
                if element not in self.validElements:
                    raise eoi.InvalidElementError("Invalid element Error of "+element+" "+str(count))
            # Check bonds for each element based on valency
            totalBonds = 0
            for element, count in self.elementsList:
                if element in self.valency:
                    totalBonds += count * self.valency[element]
                else:
                    raise eoi.IncorrectBondsError("Incorrect bond count Error : "+ str(totalBonds))
                # Simplistic check: total bonds should be even (basic rule for stability)
                return totalBonds % 2 == 0
        except eoi.InvalidElementError as e:
            print(e)
            return False
        except eoi.IncorrectBondsError as e: 
            print(e)
            return False