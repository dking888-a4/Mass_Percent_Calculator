# Slide 1

## Project 1 -- Mass Percent Solution Calculator

### Daniel King

# Slide 2

## Purpose

This program is a calculator for specific type of concentration unit known as mass or weight
percent. 

Mass percent solutions are defined as the mass of the solute (what is being dissolved) divided by the mass of the solution [the mass of the solute plus the mass of the solvent (what the solute is dissolved in)]. 

These calculations are not difficult but they involve a bit of algebra. They can get somewhat involved if there are stock solutions involved. 

Some time ago, I created a spreadsheet to do these calculations, although sometimes I still do them by hand. 

Since the basic equation has two unknown masses, one of them must be given either as a fixed mass or volume.


# Slide 3

## What went right

- Having the design document from Activity 2. 
- ideas for input and basic logic flow


# Slide 3

## Improvement

- More comprehensive input validation
    - negative numbers
    - percents greater than 100

- Spliiting the program into multiple files

- Simplifying the calcuations

# Slide 4

## Risk and Change Management

Refactoring some the code into separate functions

- Floating point number validation of strings
- A function to get data for the solute and the solvent. This code was to be in the main function, but is very similar, so I moved it to a separate function.


# Slide 5

## Actionable Advice

- Have a detailed design document.
- Start Earlier
- Think of different approaches.



# Other Thoughts

## Challenges

- The complexity of the calculations when using stock solutions such as 50% Hydrogen Peroxide. There is the concentration of the stock solution, the density, accounting for additional solvent in the stock solution, the density of the solvent, and the concentration of the desired solution. For me, this was a lot to keep track of in the program. Since I had the spreadsheet, I can check the results of the program.

- Even though I had a rough idea of how I wanted to approach this, I ended  with several helper functions as I realized I was repeating myself unneccessarily (DRY) particularly with validating floating point number inputs. 

- The issue with git push to an existing github repo. I finally fixed this be installing a different distribution of Linux. That issue seems to be resolved now.


## Future Work

- Write this as an Object Oriented Program.

- Expand it to do calcutions for other solution concenration units such as Molarity, Molality, and normal percent.

- Have it accept input from a file and write resuls to a file.

## Sample Data
Known Solvent Volume
Solution Concentration: 6 %
Solute Name: Hydrogen Peroxide
Solute Density: 1.1 
Solid: n
Solute Concentration 50
Solvent Name: Water
Solvent Density: 1.00
Solvent Volume: 900 mL

Solute Mass: 57.45 g
Solute Volume: 104.45 mL
Solvent Mass 842.55 g
Solvent Volume: 842.55 mL


Known Solvent Mass
Solution Concentration: 6 %
Solute Name: Hydrogen Peroxide
Solute Density: 1.1
Solid: n
Solute Concentration 50
Solvent Name: Water
Solvent Density: 1.00
Solvent mass: 485 g

Solute Mass: 30.96 g
Solute Volume: 56.29 mL
Solvent Mass 454.04 g
Solvent Volume: 454.04 mL


Known Solute Mass
Solution Concentration: 5 %
Solute Name: Adipoyl Chloride
Solute Density: 1.26
Solid: n
Solute Concentration 100
Solvent Name: Cyclohexane
Solvent Density: 0.779
Solute mass: 100 g

Solute Mass: 100.00 g
Solute Volume: 79.37 mL
Solvent Mass 1900 g
Solvent Volume: 2439.024 mL


Known Solute Volume
Solution Concentration: 5 %
Solute Name: Adipoyl Chloride
Solute Density: 1.26
Solid: n
Solute Concentration 100
Solvent Name: Cyclohexane
Solvent Density: 0.779
Solute Volume: 100 mL

Solute Mass: 126.00 g
Solute Volume: 100.00 mL
Solvent Mass 2394 g
Solvent Volume: 3073.17 mL