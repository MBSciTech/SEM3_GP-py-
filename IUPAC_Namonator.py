import Exceptions_of_IUPAC as eoi
import FormulaValidator as fv

class Namonator:
    def __init__(self):
        self.formula = input("Enter Formula : ")
        self.fv1 = fv.FormulaValidator(self.formula)
        self.elementsList = []
        self.elementsDict = {}
        self.setFormula()
        name = self.generateName()
        print(self.name)
        
    #Generate the IUPAC Name
    def generateName(self):
        hydrocarbonNames = {
            1: "Methane",
            2: "Ethane",
            3: "Propane",
            4: "Butane",
            5: "Pentane",
            6: "Hexane",
            7: "Heptane",
            8: "Octane",
            9: "Nonane",
            10: "Decane",
        }
        name = ""
        f = self.formula
        if(self.containsCH(self.elementsDict)):
            n = self.elementsDict["C"]#Count of Carbon
            if(self.elementsDict["H"]==(2*n+2)):
                #It is Alken
                name+=hydrocarbonNames[self.elementsDict["C"]]
            elif(self.elementsDict["H"]==(2*n)):
                bondIndex = 0
                #It is Alkene
                name+=hydrocarbonNames[self.elementsDict["C"]][:3]+"-"+"-en"
            elif(self.elementsDict["H"]==(2*n-2)):
                #It is Alkyne
                name+=hydrocarbonNames[self.elementsDict["C"]][:3]+"-"+"-yne"
            return name  
        
        
        
        
        
        
        
        
    def containsCH(self,d):
        for i in d.keys():
            if(i not in ["C","H"]):
                return False
        return True
        
    def setFormula(self):
        f = self.formula
        element = ""
        count = ""

        # Clear previous lists and dictionaries to avoid duplicate data
        

        for i in range(len(f)):
            if f[i].isupper():  # Start of a new element
                if element:  # Save the previous element and its count
                    count = int(count) if count else 1
                    self.elementsList.append((element, count))
                    if element in self.elementsDict:
                        self.elementsDict[element] += count
                    else:
                        self.elementsDict[element] = count
                element = f[i]
                count = ""
            elif f[i].islower():  # Continuation of the element symbol
                element += f[i]
            elif f[i].isdigit():  # Count of the current element
                count += f[i]

        # Add the last element after the loop ends
        if element:
            count = int(count) if count else 1
            self.elementsList.append((element, count))
            if element in self.elementsDict:
                self.elementsDict[element] += count
            else:
                self.elementsDict[element] = count

        # Display element data
        self.display_element_data()
        
        
    #Display data of elements of Given Formula
    def display_element_data(self):
        print("Elements : ",self.elementsList)
        print("Elements Dict : ", self.elementsDict)
n = Namonator()
