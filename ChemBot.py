import discord
from discord.ext import commands
import re

# Set up intents for the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Initialize the bot with the specified command prefix and intents
bot = commands.Bot(command_prefix='/', intents=intents)

element_masses = {
    'H': 1.00784,
    'He': 4.0026,
    'Li': 6.939,
    'Be': 9.01218,
    'B': 10.806,
    'C': 12.011,
    'N': 14.0067,
    'O': 15.999,
    'F': 18.9984,
    'Ne': 20.179,
    'Na': 22.98977,
    'Mg': 24.305,
    'Al': 26.98154,
    'Si': 28.086,
    'P': 30.97376,
    'S': 32.064,
    'Cl': 35.453,
    'K': 39.098,
    'Ar': 39.948,
    'Ca': 40.078,
    'Sc': 44.95591,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.93804,
    'Fe': 55.845,
    'Co': 58.93319,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.92159,
    'Se': 78.971,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.90584,
    'Zr': 91.224,
    'Nb': 92.90637,
    'Mo': 95.95,
    'Tc': 98,
    'Ru': 101.07,
    'Rh': 102.90550,
    'Pd': 106.42,
    'Ag': 107.8682,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.710,
    'Sb': 121.760,
    'Te': 127.60,
    'I': 126.90447,
    'Xe': 131.293,
    'Cs': 132.90545,
    'Ba': 137.327,
    'La': 138.90547,
    'Ce': 140.116,
    'Pr': 140.90766,
    'Nd': 144.242,
    'Pm': 145,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.92535,
    'Dy': 162.500,
    'Ho': 164.93033,
    'Er': 167.259,
    'Tm': 168.93422,
    'Yb': 173.054,
    'Lu': 174.9668,
    'Hf': 178.49,
    'Ta': 180.94788,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.217,
    'Pt': 195.084,
    'Au': 196.966569,
    'Hg': 200.592,
    'Tl': 204.38,
    'Pb': 207.2,
    'Bi': 208.98040,
    'Th': 232.03806,
    'Pa': 231.03588,
    'U': 238.02891,
    'Np': 237,
    'Pu': 244,
    'Am': 243,
    'Cm': 247,
    'Bk': 247,
    'Cf': 251,
    'Es': 252,
    'Fm': 257,
    'Md': 258,
    'No': 259,
    'Lr': 266,
    'Rf': 267,
    'Db': 270,
    'Sg': 271,
    'Bh': 270,
    'Hs': 277,
    'Mt': 278,
    'Ds': 281,
    'Rg': 280,
    'Cn': 285,
    'Nh': 284,
    'Fl': 289,
    'Mc': 288,
    'Lv': 293,
    'Ts': 294,
    'Og': 294,
    # All Elements :)
}

# Parse the chemical formula and return a list of elements with their counts
def parse_formula(formula):
    # Regular expression pattern to match element symbols and their counts
    element_pattern = re.compile(r'([A-Z][a-z]?)(\d*)')
    # Find all elements and their counts in the formula
    elements = element_pattern.findall(formula)
    return elements

# Calculate the molar mass of a chemical formula represented by a list of elements
def calculate_molar_mass(elements):
    molar_mass = 0
    for element, count in elements:
        # If the element is valid, add its molar mass to the total
        if element in element_masses:
            molar_mass += element_masses[element] * (int(count) if count else 1)
        else:
            raise ValueError(f'Invalid element symbol: {element}')
    return molar_mass

# Event handler to print a message when the bot is connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command to calculate the molar mass of a given chemical formula
@bot.command(name='molmass', help='Calculates the molar mass of a given chemical formula.')
async def molmass(ctx, formula: str):
    try:
        # Parse the formula and calculate the molar mass
        elements = parse_formula(formula)
        molar_mass = calculate_molar_mass(elements)
        # Send the result to the user
        await ctx.send(f'The molar mass of {formula} is {molar_mass:.2f} g/mol.')
    except ValueError as e:
        # If there's an error, send an error message to the user
        await ctx.send(str(e))

# Start the bot using the token (Replace with your bot token)

bot.run("MTA5MTAzOTgyMTAxNjg1ODY1NA.G98pbL.47n6yQZvVYSuo3wf83fp2aQ0wfzywwrKR0XFPs")

