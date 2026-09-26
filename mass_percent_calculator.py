"""
Mass Percent Solution Calculator
CSCI 1511
Author: Daniel King
Date: September 25, 2026
Purpose: This program will calculate amount of a compound and a solvent needed
         to make a solution that is a known concentration based on the mass of
         of the compound and the mass of the solvent.
"""

def get_solvent_data():
    """ Get solvent data (name and density) and return a dictionary contianing
    the data """
    print("to be implemented")

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

    

