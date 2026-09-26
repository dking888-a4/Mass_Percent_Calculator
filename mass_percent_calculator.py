"""
Mass Percent Solution Calculator
CSCI 1511
Author: Daniel King
Date: September 25, 2026
Purpose: This program will calculate amount of a compound and a solvent needed
         to make a solution that is a known concentration based on the mass of
         of the compound and the mass of the solvent.
"""

def is_float(value:str) -> bool:
    """ Check if string can be converted to a floating point value. """
    # Code from https://www.geeksforgeeks.org/python/python-check-for-float-string/
    
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_solvent_data():
    """ Get solvent data (name and density) and return a dictionary contianing
    the data """
    
    solvent_dict : dictionary = {}

    name : str = input("Enter name of the solvent: ")
    density_str : str = input("Enter solvent density or specific gravity in g/mL: ")

    # validate density_str is a floating point value
    while not is_float(density_str):
        print("Invalid Input: value is not a numeric value")
        density_str : str = input("Enter solvent density or specific gravity in g/mL: ")
    
    density : float = float(density_str)

    solvent_dict['name'] = name
    solvent_dict['density'] = density

    return solvent_dict




def get_compound_data():
     """ Get compound data (name, density, concentration) and return a dictionary contianing the data """
#    print("to be implemented")

def compound_mass(solution_data):
    """ calculate solution based on known compound mass """
    print("to be implemented") 

def solvent_mass(solution_data):
    """ Calculate solution based on know solvent mass """
    print("to be implemented")

def compound_volume(solution_data):
    """ calculate solution based on known compound volume """
    print("to be implemented") 

def solvent_volume(solution_data):
    """ Calculate solution based on know solvent volumne """
    print("to be implemented")

def display_solution_data(solution_data):
    """ Display data to make solution. """

def display_menu():
    """ Display main menu. """

    print("\n1 -- Known Compound Mass")
    print("2 -- Known Compound Volume")
    print("3 -- Known Solvent Mass")
    print("4 -- Known Solvent Volume")
    print("q -- Exit Program\n")


def get_choice() -> str:
    """ Return user's menu selection """

    valid_choices = ['1', '2', '3', '4', 'q']

    answer : str = input("Selection: ")
    
    while answer.lower() not in valid_choices:
        answer = input("Invalid choice. Please enter [1, 2, 3, 4, or q]: ")

    return answer    

def get_solution_data(solution_input):
    """ Get data for compound, solvent, and solution concentration. """

def main():
    """ Main Program Logic """

    print("Mass Percent Solution Calculator\n")

    

