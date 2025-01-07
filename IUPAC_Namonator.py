import Exceptions_of_IUPAC as eoi
import FormulaValidator as fv

class Namonator:
    def __init__(self):
        self.formula = input("Enter Formula : ")
        self.fv1 = fv.FormulaValidator(self.formula)
        self.elementsList = []
        self.elementsDict = {}
        self.setFormula()
        
    #Generate the IUPAC Name
    def generateName(self):
        pass
    
    def setFormula(self):
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
            if(element in self.elementsDict):
                self.elementsDict[element] += 1
            else:
                self.elementsDict[element] = 1
            self.display_element_data()
    #Display data of elements of Given Formula
    def display_element_data(self):
        print("Elements : ",self.elementsList)
        print("Elements Dict : ", self.elementsDict)
n = Namonator()