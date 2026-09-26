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
        
def get_float(prompt:str) -> float:
    """ get data that is a floating point value """

    value_str : str = input(f"{prompt}")

    # validate density_str is a floating point value
    while not is_float(value_str):
        print("Invalid Input: value is not a numeric value")
        density_str : str = input(f"{prompt}")
    
    density : float = float(density_str)


def get_data(component:str) -> dictionary:
    """ Get data for solute or solvent. """

    component_dict :dictionary = {}

    name : str = input(f"Enter name of the {component}: ")

    density = get_float(f"Enter {component} density or specific gravity in g/mL: ")
 
    component_dict['name'] = name
    component_dict['density'] = density

    if component.lower() == "solute":
        solid_solute: str = input("Is the solute a solid compound? (y/n) ")
        if solid_solute.lower() == "y":
            solid = True
            stock_concentration = 100
        else:
            solid = False

            stock_concentration = get_float("Enter the stock solution concentration as a percent: ")

    component_dict['concentration'] = stock_concentration
    component_dict['solid'] = solid
    return component_dict


def solute_mass(solution_data):
    """ calculate solution based on known solute mass """
    print("to be implemented") 


def solvent_mass(solution_data):
    """ Calculate solution based on know solvent mass """
    print("to be implemented")


def solute_volume(solution_data):
    """ calculate solution based on known solute volume """
    print("to be implemented") 


def solvent_volume(solution_data):
    """ Calculate solution based on know solvent volumne """
    print("to be implemented")


def display_solution_data(solution_data):
    """ Display data to make solution. """


def display_menu():
    """ Display main menu. """

    print("\n1 -- Known Solute Mass")
    print("2 -- Known Solute Volume")
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

def get_solution_data() -> list:
    """ Get data for solute, solvent, and solution concentration. """

    # list: solute dictionary, solvent dictionary, and solution concentration in percent (float)

    solution_list : list = []
    solution_concentration = get_float("Enter the desired solution concentration as a percent: ")

    solute_dict : dictionary = get_data("solute")
    solvent_dict : dictionary = get_data("solvent")
    
    # create list and return it
    solution_list.append(solute_dict)
    solution_list.append(solvent_dict)
    solution_list.append(solution_concentration)

    return solution_list

    
def main():
    """ Main Program Logic """

    print("Mass Percent Solution Calculator\n")

    done: bool = False
    
    while not done:
        display_menu()
        selection : str = get_choice()
        if selection.lower() == 'q':
            done = True
        else:
            solution_components: list = get_solution_data()

        for item in solution_components:
            print solution_components[item]
        
main()



    

