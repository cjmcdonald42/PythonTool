"""
         package:  pythonTool.py
          author:  Charles J McDonald «cmcdonald@daviestech.org»
    date/version:  2026.11.26

    description:
        This is a handy tool for calulating the density of a material given it's mass and volume.
"""

"""
Welcome to the Density Calculator
Given the Mass and Volume of a material, I will calculate its Density
"""

print("")
mass = float(input("What is the mass of your sample in grams? "))
Volume = float(input("What is the measured volume of your sample in millilitres? "))
print("")

Density = mass / Volume
print(f"The Density is {Density} g/mL")
print("")