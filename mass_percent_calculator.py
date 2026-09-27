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
        value_str : str = input(f"{prompt}")
    
    return float(value_str)


def get_data(component:str) -> dictionary:
    """ Get data for solute or solvent. """

    component_dict :dictionary = {}

    name : str = input(f"Enter name of the {component}: ")

    density = get_float(f"Enter {component} density or specific gravity in g/mL: ")
 
    component_dict['name'] = name
    component_dict['density'] = density
    
    stock_concentration : float = 0.0

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
    
    solvent_mass : float = get_float("Enter solvent mass in grams: ")

    solvent_vol : float = solvent_mass / solution_data[1]['density']

    solute_mass : float = solvent_mass*solution_data[2]/(100 - solution_data[2])

    solute_vol = solute_mass * 100 / solution_data[0]['concentration'] * (1 / solution_data[0]['density'])

    if solution_data[0]['concentration'] < 90:
        solvent_vol = solvent_vol - (solute_vol * solution_data[0]['density'] \
        * (100 - solution_data[0]['concentration']) / 100) 
    
    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt



def solute_volume(solution_data):
    """ calculate solution based on known solute volume """



def solvent_volume(solution_data) -> list:
    """ Calculate solution based on know solvent volumne """

    solvent_vol : float = get_float("Enter solvent volume in mL: ")

    solvent_mass : float = solvent_vol * solution_data[1]['density']

    solute_mass : float = solvent_mass*solution_data[2]/(100 - solution_data[2])

    solute_vol = solute_mass * 100 / solution_data[0]['concentration'] * (1 / solution_data[0]['density'])

    if solution_data[0]['concentration'] < 90:
        solvent_vol = solvent_vol - (solute_vol * solution_data[0]['density'] \
        * (100 - solution_data[0]['concentration']) / 100) 
    
    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt


def display_solution_calculations(solution_data: list, solution_amt: list):
    """ Display data to make solution. """
    print(f"Amounts needed to make {solution_data[2]} percent (by mass) {solution_data[0]['name']}")

    for i in range(0, 4):
        if i < 2:
            if i == 0:
                print(f"Solute Mass: {solution_amt[i]} grams")
            else:
                print(f"Solute Volume: {solution_amt[i]} mL")
        else:
            if i == 2:
                print(f"Solvent Mass: {solution_amt[i]} grams")
            else:
                print(f"Solvent Volume: {solution_amt[i]} mL")                    


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

    
    while True:
        display_menu()
        selection : str = get_choice()
        if selection.lower() == 'q':
            break
        
        solution_components: list = get_solution_data()

        # for item in solution_components:
        #     print(item)
        solution_amounts: list = []
        choice: int = int(selection)

        if choice == 1:
            solution_amounts = solute_mass(solution_components)
        elif choice == 2:
            solution_amounts = solute_volume(solution_components)
        elif choice == 3:
            solution_amounts = solvent_mass(solution_components)
        else:
            solution_amounts = solvent_volume(solution_components)

        display_solution_calculations(solution_components, solution_amounts)
    
    print("Exiting Program.")
        
        
main()



    

