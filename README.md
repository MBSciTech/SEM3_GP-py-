# SEM3_GP-py- | IUPAC Name Generator

An intelligent **IUPAC Name Generator for Organic and Inorganic Chemistry** written in Python. This project is part of the FSCP-1 Semester 3 curriculum and provides automated chemical nomenclature based on molecular formulas.

---

## 🎯 Project Overview

This application takes a chemical formula as input, validates its correctness, and generates the corresponding IUPAC name. Currently, it supports **hydrocarbons** (alkanes, alkenes, and alkynes) and is designed to be expanded for inorganic compounds and other organic molecules.

### Key Features:
- ✅ **Formula Validation** - Validates chemical formulas and checks bonding integrity
- ✅ **Element Parsing** - Extracts elements and their counts from chemical formulas
- ✅ **IUPAC Nomenclature** - Generates proper IUPAC names for supported compounds
- ✅ **Error Handling** - Comprehensive exception handling for invalid inputs
- ✅ **Extensible Architecture** - Modular design for adding new compound types

---

## 🏗️ Project Architecture

The project is organized into three main modules:

### Module 1: **Exceptions_of_IUPAC.py**
Defines custom exception classes for error handling:

```python
- IncorrectNameError      # Raised when generated name is invalid
- IncorrectFormulaError   # Raised when formula structure is incorrect
- InvalidElementError     # Raised when an unknown element is detected
- IncorrectBondsError     # Raised when valency/bonding rules are violated
```

**Status:** ✅ Complete (v1.0)

---

### Module 2: **FormulaValidator.py**
Validates chemical formulas and checks molecular stability:

**Key Methods:**
- `__init__(formula)` - Initializes validator and performs validation
- `parseFormula()` - Parses formula string into elements and counts
- `checkValidity()` - Validates elements and checks total bond count

**Supported Elements:** C, H, O, N, S, P, Cl, Br, F, I, Ar

**Valency Rules Implemented:**
- Carbon (C): 4 bonds
- Hydrogen (H): 1 bond
- Oxygen (O): 2 bonds
- Nitrogen (N): 3 bonds
- And others as per periodic table

**Validation Logic:**
- Verifies all elements are from the supported list
- Checks that total bond count is even (basic stability criterion)
- Raises appropriate exceptions for invalid formulas

**Status:** ✅ Complete (v1.0)

---

### Module 3: **IUPAC_Namonator.py**
Generates IUPAC names for valid chemical formulas:

**Key Methods:**
- `__init__()` - Initializes the namonator with user input
- `setFormula()` - Parses and stores formula data in list and dictionary
- `display_element_data()` - Displays parsed element information
- `generateName()` - Generates IUPAC name based on formula composition
- `containsCH()` - Checks if compound contains only Carbon and Hydrogen

**Current Capabilities:**
Generates IUPAC names for hydrocarbons based on carbon chain length:

| Carbon Count | Alkan (CₙH₂ₙ₊₂) | Alken (CₙH₂ₙ) | Alkyn (CₙH₂ₙ₋₂) |
|:---:|:---:|:---:|:---:|
| 1 | Methane | - | - |
| 2 | Ethane | Ethene | Ethyne |
| 3 | Propane | Propene | Propyne |
| 4 | Butane | Butene | Butyne |
| 5 | Pentane | Pentene | Pentyne |
| 6 | Hexane | Hexene | Hexyne |
| 7 | Heptane | Heptene | Heptyne |
| 8 | Octane | Octene | Octyne |
| 9 | Nonane | Nonene | Nonyne |
| 10 | Decane | Decene | Decyne |

**Status:** ✅ Core functionality complete (v1.0)

---

## 🚀 Usage

### Example 1: Alkane (Ethane)
```
Enter Formula : C2H6
Elements :  [('C', 2), ('H', 6)]
Elements Dict :  {'C': 2, 'H': 6}
Ethane
```

### Example 2: Alkene (Propene)
```
Enter Formula : C3H6
Elements :  [('C', 3), ('H', 6)]
Elements Dict :  {'C': 3, 'H': 6}
Pro-en
```

### Example 3: Alkyne (Butyne)
```
Enter Formula : C4H6
Elements :  [('C', 4), ('H', 6)]
Elements Dict :  {'C': 4, 'H': 6}
But-yne
```

### Example 4: Invalid Formula
```
Enter Formula : C2H7
The formula is Incorrect. Please check your formula.
```

---

## 📋 Supported Compounds (Current & Planned)

### ✅ Currently Supported:
- **Alkanes** - Single carbon bonds (CₙH₂ₙ₊₂)
- **Alkenes** - One double bond (CₙH₂ₙ)
- **Alkynes** - One triple bond (CₙH₂ₙ₋₂)

### 🔄 Planned Features:
- [ ] Functional groups (alcohols, aldehydes, ketones, carboxylic acids)
- [ ] Cyclic compounds
- [ ] Aromatic compounds (benzene derivatives)
- [ ] Inorganic compound nomenclature
- [ ] Stereoisomers and optical isomers
- [ ] Advanced substitution naming
- [ ] GUI interface for user interaction

---

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MBSciTech/SEM3_GP-py-.git
   cd SEM3_GP-py-
   ```

2. **Run the program:**
   ```bash
   python IUPAC_Namonator.py
   ```

3. **Enter a chemical formula** when prompted:
   ```
   Enter Formula : C6H12
   ```

---

## 📁 File Structure

```
SEM3_GP-py-/
├── Exceptions_of_IUPAC.py      # Custom exception definitions
├── FormulaValidator.py          # Formula validation logic
├── IUPAC_Namonator.py          # IUPAC naming engine
└── README.md                   # Project documentation
```

---

## 🧪 Testing

The project has been tested with various hydrocarbon formulas:

| Formula | Type | Expected Name |
|:---:|:---:|:---:|
| CH4 | Alkane | Methane |
| C2H6 | Alkane | Ethane |
| C3H8 | Alkane | Propane |
| C2H4 | Alkene | Eth-en |
| C3H6 | Alkene | Pro-en |
| C2H2 | Alkyne | Eth-yne |
| C4H6 | Alkyne | But-yne |
| C2H7 | Invalid | Error |

---

## 🎓 Learning Outcomes

This project teaches:
- ✅ Object-Oriented Programming (OOP) principles
- ✅ Exception handling and custom exceptions
- ✅ String parsing and data structure manipulation
- ✅ Chemistry nomenclature rules (IUPAC standards)
- ✅ Input validation and error management
- ✅ Modular code design and separation of concerns

---

## 📝 Version History

| Version | Date | Changes |
|:---:|:---:|:---|
| 1.0 | 07-01-2025 | Initial release with all basic modules |
| 1.1 | 08-01-2025 | Added `generateName()` and `containsCH()` methods |
| 1.2 | Current | Enhanced with full documentation |

---

## 🤝 Contributing

This is an educational project. Contributions, suggestions, and improvements are welcome!

To contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

---

## 📚 References

- [IUPAC Nomenclature Rules](https://www.iupacnaming.com/)
- [Organic Chemistry Basics](https://www.khanacademy.org/science/organic-chemistry)
- [Chemical Valency Rules](https://www.britannica.com/technology/valence)

---

## 📧 Contact

**Project Author:** MBSciTech  
**Repository:** [SEM3_GP-py-](https://github.com/MBSciTech/SEM3_GP-py-)

---

## 📄 License

This project is created for educational purposes as part of FSCP-1 Semester 3 curriculum.

---

**Last Updated:** June 3, 2026  
**Status:** Active Development ✨
