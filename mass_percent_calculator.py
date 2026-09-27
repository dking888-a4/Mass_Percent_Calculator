"""
Mass Percent Solution Calculator
CSCI 1511
Author: Daniel King
Date: September 25, 2026
Purpose: This program will calculate amount of a compound and a solvent needed
         to make a solution that is a known concentration based on the mass of
         of the compound and the mass of the solvent.
"""

# Mass percent is defined as the mass of the solute divided by the mass of the
# solution (solute mass + solvent mass)


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

    # Get name and density of the solute or solvent
    name : str = input(f"Enter name of the {component}: ")

    density = get_float(f"Enter {component} density or specific gravity in g/mL: ")
 
    component_dict['name'] = name
    component_dict['density'] = density
    
    # Get concentration of the solute if it is a liquid
    stock_concentration : float = 100.0

    if component.lower() == "solute":
        solid_solute: str = input("Is the solute a solid compound? (y/n) ")
        if solid_solute.lower() == "y":
            solid = True
        else:
            solid = False

            stock_concentration = get_float("Enter the stock solution concentration as a percent: ")

        component_dict['concentration'] = stock_concentration
        component_dict['solid'] = solid
    
    return component_dict



def solute_mass(solution_data):
    """ calculate solution based on known solute mass """
    
    solute_mass: float = get_float("Enter mass of solute in grams: ") # mass of solute stock reagent

    solute_vol: float = solute_mass / solution_data[0]['density']

    # calculate mass of the solute in the stock reagent
    solute_mass_adj: float = solute_mass * solution_data[0]['concentration'] / 100 
    
    solvent_mass: float = (100 - solution_data[2]) * solute_mass_adj / solution_data[2]

    if solution_data[0]['concentration'] < 90:
        # Adjust solvent mass to account for additional solvent in the solute stock reagent.
        solvent_mass = solvent_mass - (solute_mass_adj - solute-mass)
    
    solvent_vol: float = solvent_mass / solution_data[1]['density']

    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt
  


def solvent_mass(solution_data):
    """ Calculate solution based on know solvent mass """
    
    solvent_mass : float = get_float("Enter solvent mass in grams: ") # mass of solvent

    solvent_vol : float = solvent_mass / solution_data[1]['density'] 

    # calcuate mass of solute needed for the solution
    solute_mass : float = solvent_mass*solution_data[2]/(100 - solution_data[2])

    # calculate volume of stock reagent needed for calcuated solute mass
    solute_vol = solute_mass * 100 / solution_data[0]['concentration'] * (1 / solution_data[0]['density'])

    if solution_data[0]['concentration'] < 90:
        # Adjust solvent volume and solvent mass to account for additional 
        # solvent in the solute stock reagent.

        solvent_vol = solvent_vol - (solute_vol * solution_data[0]['density'] \
        * (100 - solution_data[0]['concentration']) / 100) 

        solvent_mass = solvent_vol * solution_data[1]['density']
    
    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt



def solute_volume(solution_data):
    """ calculate solution based on known solute volume """
    
    solute_vol: float = get_float("Enter volume of solute in mL: ") # volumne of solute stock reagent

    # Calcuate mass of solute present in the given volume of solute stock reagent
    solute_mass: float = solute_vol * solution_data[0]['density'] * solution_data[0]['concentration'] / 100

    # Calculate mass of the solvent for the given amount of solute
    solvent_mass: float = (100 - solution_data[2]) * solute_mass / solution_data[2]

    if solution_data[0]['concentration'] < 90:
        # Adjust solvent mass to account for additional solvent in the solute stock reagent.
        solvent_mass = solvent_mass - (solute_vol * solution_data[0]['density'] \
        * (100 - solution_data[0]['concentration']) / 100)
    
    solvent_vol: float = solvent_mass / solution_data[1]['density']

    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt



def solvent_volume(solution_data) -> list:
    """ Calculate solution based on know solvent volumne """

    solvent_vol : float = get_float("Enter solvent volume in mL: ") # volumet of solvent

    solvent_mass : float = solvent_vol * solution_data[1]['density']

    # calcuate mass of solute needed for the solution
    solute_mass : float = solvent_mass*solution_data[2]/(100 - solution_data[2])

    # calculate volume of stock reagent needed for calcuated solute mass
    solute_vol = solute_mass * 100 / solution_data[0]['concentration'] * (1 / solution_data[0]['density'])

    if solution_data[0]['concentration'] < 90:
        # Adjust solvent volume and mass 4to account for additional solvent in the solute stock reagent.
        solvent_vol = solvent_vol - (solute_vol * solution_data[0]['density'] \
        * (100 - solution_data[0]['concentration']) / 100) 
        
        solvent_mass : float = solvent_vol * solution_data[1]['density']

    solution_amt : list = [solute_mass, solute_vol, solvent_mass, solvent_vol]

    return solution_amt



def display_solution_calculations(solution_data: list, solution_amt: list):
    """ Display data to make solution. """

    solute_name :str = solution_data[0]['name']
    solvent_nmae :str = solution_data[1]['name']

    print(f"\nAmounts needed to make {solution_data[2]} percent (by mass) {solute_name}\n")

    for index in range(0, 4):
        if index < 2:
            if index == 0:
                print(f"{solute_name} Mass: {solution_amt[index]:.2f} grams")
            else:
                print(f"{solute_name} Volume: {solution_amt[index]:.2f} mL")
        else:
            if index == 2:
                print(f"{solvent_nmae} Mass: {solution_amt[index]:.2f} grams")
            else:
                print(f"{solvent_nmae} Volume: {solution_amt[index]:.2f} mL")                    

4

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
    return [solute_dict, solvent_dict, solution_concentration]

    

def main():
    """ Main Program Logic """

    print("Mass Percent Solution Calculator\n")

    
    while True:
        display_menu()
        selection : str = get_choice()
        if selection.lower() == 'q':
            break
        
        solution_components: list = get_solution_data()

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



    

