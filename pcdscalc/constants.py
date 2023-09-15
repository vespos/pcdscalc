""""Module to hold constants."""
import numpy as np

# wavelength/energy = 12398.4 (A) / E(eV)
WAVELENGTH_TO_ENERGY_LAMBDA = 12398.4


# Material density in g/cm^3
density = {
    "H": 0.00008988,
    "He": 0.0001785,
    "Li": 0.543,
    "Be": 1.85,
    "B": 2.34,
    "C": 3.5,
    "N": 0.0012506,
    "O": 0.001429,
    "F": 0.001696,
    "Ne": 0.0008999,
    "Na": 0.971,
    "Mg": 1.738,
    "Al": 2.698,
    "Si": 2.3296,
    "P": 1.82,
    "S": 2.067,
    "Cl": 0.003214,
    "Ar": 0.0017837,
    "K": 0.862,
    "Ca": 1.54,
    "Sc": 2.989,
    "Ti": 4.54,
    "V": 6.11,
    "Cr": 7.15,
    "Mn": 7.44,
    "Fe": 7.874,
    "Co": 8.86,
    "Ni": 8.912,
    "Cu": 8.96,
    "Zn": 7.134,
    "Ga": 5.907,
    "Ge": 5.323,
    "As": 5.776,
    "Se": 4.809,
    "Br": 3.122,
    "Kr": 0.003733,
    "Rb": 1.532,
    "Sr": 2.64,
    "Y": 4.469,
    "Zr": 6.506,
    "Nb": 8.57,
    "Mo": 10.22,
    "Tc": 11.5,
    "Ru": 12.37,
    "Rh": 12.41,
    "Pd": 12.02,
    "Ag": 10.501,
    "Cd": 8.69,
    "In": 7.31,
    "Sn": 7.287,
    "Sb": 6.685,
    "Te": 6.232,
    "I": 4.93,
    "Xe": 0.005887,
    "Cs": 1.873,
    "Ba": 3.594,
    "La": 6.145,
    "Ce": 6.77,
    "Pr": 6.773,
    "Nd": 7.007,
    "Pm": 7.26,
    "Sm": 7.52,
    "Eu": 5.243,
    "Gd": 7.895,
    "Tb": 8.229,
    "Dy": 8.55,
    "Ho": 8.795,
    "Er": 9.066,
    "Tm": 9.321,
    "Yb": 6.965,
    "Lu": 9.84,
    "Hf": 13.31,
    "Ta": 16.654,
    "W": 19.25,
    "WC": 15.8,
    "Re": 21.02,
    "Os": 22.61,
    "Ir": 22.56,
    "Pt": 21.46,
    "Au": 19.282,
    "Hg": 13.5336,
    "Tl": 11.85,
    "Pb": 11.342,
    "Bi": 9.807,
    "Po": 9.32,
    "At": 7,
    "Rn": 0.00973,
    "Fr": 1.87,
    "Ra": 5.5,
    "Ac": 10.07,
    "Th": 11.72,
    "Pa": 15.37,
    "U": 18.95,
    "Np": 20.45,
    "Pu": 19.84,
    "H2O": 1.0,
    "B4C": 2.52,
    "SiC": 3.217,
    "SiO2": 2.2,
    "Al2O3": 3.97,
    "ZnSe": 5.42,
    "ZnTe": 6.34,
    "CdS": 6.749,
    "CdSe": 7.01,
    "CdTe": 7.47,
    "BN": 3.49,
    "GaSb": 5.619,
    "GaAs": 5.316,
    "GaMnAs": 5.316,
    "GaP": 4.13,
    "InP": 4.787,
    "InAs": 5.66,
    "InSb": 5.775,
    "TaC": 13.9,
    "TiB2": 4.52,
    "YAG": 4.55,
    "CuBe": 8.96,
    "ZnO": 5.606,
    "SiC2": 3.217,
    "AlN": 3.3,
    "Si3N4": 3.44,
    "CaF2": 3.18,
    "LiF": 2.635,
    "KF": 2.48,
    "PbF2": 8.24,
    "SrF2": 4.24,
    "KBr": 2.75,
    "ZrO2": 5.6,
    "Gd3Ga5O12": 7.08,
    "CaSiO5": 2.4,
    "LaMnO3": 5.7,
    "LaAlO3": 6.52,
    "La0.7Sr0.3MnO3": 6.17,
    "La0.5Ca0.5MnO3": 6.3,
    "Fe.68Cr.2Ni.1Mn.02": 8.03,
    "CaSO4H4O2": 2.32,
    "C10H8O4": 1.4,
    "C22H10N2O5": 1.43,
    "C3H6O": 0.79,
    "C5H8O2": 1.19,
    "C2F4": 2.2,
    "C7H8": 0.867,
    "Y3Al5O12": 4.56,
    "CHN.3O7.6": 1.06,
    "C1.5H0.3O4.3N0.4PCa2.2": 1.92,
    ("Be0.9983O0.0003Al0.0001Ca0.0002C0.0003Cr0.000035Co0.000005Cu0.00005Fe0."
     "0003Pb0.000005Mg0.00006Mn0.00003Mo0.00001Ni0.0002Si0.0001Ag0.000005Ti0."
     "00001Zn0.0001"): 1.85,
    ("Be.994O.004Al.0005B.000003Cd.0000002Ca.0001C.0006Cr.0001Co.00001Cu."
     "0001Fe.0008Pb.00002Li.000003Mg.00049Mn.0001Mo.00002Ni.0002N.0003Si."
     "0004Ag.00001"): 1.85,
}


# Chemical Formula Aliases
chemical_name_to_formula = {
    "Air": "N1.562O.42C.0003Ar.0094",
    "air": "N1.562O.42C.0003Ar.0094",
    "C*": "C",
    "mylar": "C10H8O4",
    "Mylar": "C10H8O4",
    "polyimide": "C22H10N2O5",
    "Polyimide": "C22H10N2O5",
    "kapton": "C22H10N2O5",
    "Kapton": "C22H10N2O5",
    "304SS": "Fe.68Cr.2Ni.1Mn.02",
    "Acetone": "C3H6O",
    "acetone": "C3H6O",
    "PMMA": "C5H8O2",
    "Teflon": "C2F4",
    "teflon": "C2F4",
    "Toluene": "C7H8",
    "toluene": "C7H8",
    "FS": "SiO2",
    "GGG": "Gd3Ga5O12",
    "quartz": "SiO2",
    "Quartz": "SiO2",
    "Silica": "SiO2",
    "silica": "SiO2",
    "water": "H2O",
    "Water": "H2O",
    "Calcite": "CaCO3",
    "calcite": "CaCO3",
    "YAG": "Y3Al5O12",
    "yag": "Y3Al5O12",
    "Sapphire": "Al2O3",
    "sapphire": "Al2O3",
    "Blood": "CHN.3O7.6",
    "LMSO": "La0.7Sr0.3MnO3",
    "blood": "CHN.3O7.6",
    "Bone": "C1.5H0.3O4.3N0.4PCa2.2",
    "bone": "C1.5H0.3O4.3N0.4PCa2.2",
    "IF1": ("Be0.9983O0.0003Al0.0001Ca0.0002C0.0003Cr0.000035Co0.000005Cu0."
            "00005Fe0.0003Pb0.000005Mg0.00006Mn0.00003Mo0.00001Ni0.0002Si0."
            "0001Ag0.000005Ti0.00001Zn0.0001"),
    "PF60": ("Be.994O.004Al.0005B.000003Cd.0000002Ca.0001C.0006Cr.0001Co."
             "00001Cu.0001Fe.0008Pb.00002Li.000003Mg.00049Mn.0001Mo.00002Ni."
             "0002N.0003Si.0004Ag.00001"),
}

# Atomic Number
element_z = {
    'H' : 1,
    'He': 2,
    'Li': 3,
    'Be': 4,
    'B': 5,
    'C': 6,
    'N': 7,
    'O': 8,
    'F': 9,
    'Ne': 10,
    'Na': 11,
    'Mg': 12,
    'Al': 13,
    'Si': 14,
    'P': 15,
    'S': 16,
    'Cl': 17,
    'Ar': 18,
    'K': 19,
    'Ca': 20,
    'Sc': 21,
    'Ti': 22,
    'V': 23,
    'Cr': 24,
    'Mn': 25,
    'Fe': 26,
    'Co': 27,
    'Ni': 28,
    'Cu': 29,
    'Zn': 30,
    'Ga': 31,
    'Ge': 32,
    'As': 33,
    'Se': 34,
    'Br': 35,
    'Kr': 36,
    'Rb': 37,
    'Sr': 38,
    'Y': 39,
    'Zr': 40,
    'Nb': 41,
    'Mo': 42,
    'Tc': 43,
    'Ru': 44,
    'Rh': 45,
    'Pd': 46,
    'Ag': 47,
    'Cd': 48,
    'In': 49,
    'Sn': 50,
    'Sb': 51,
    'Te': 52,
    'I': 53,
    'Xe': 54,
    'Cs': 55,
    'Ba': 56,
    'La': 57,
    'Ce': 58,
    'Pr': 59,
    'Nd': 60,
    'Pm': 61,
    'Sm': 62,
    'Eu': 63,
    'Gd': 64,
    'Tb': 65,
    'Dy': 66,
    'Ho': 67,
    'Er': 68,
    'Tm': 69,
    'Yb': 70,
    'Lu': 71,
    'Hf': 72,
    'Ta': 73,
    'W': 74,
    'Re': 75,
    'Os': 76,
    'Ir': 77,
    'Pt': 78,
    'Au': 79,
    'Hg': 80,
    'Tl': 81,
    'Pb': 82,
    'Bi': 83,
    'Po': 84,
    'At': 85,
    'Rn': 86,
    'Fr': 87,
    'Ra': 88,
    'Ac': 89,
    'Th': 90,
    'Pa': 91,
    'U': 92,
    'Np': 93,
    'Pu': 94
}

# Atomic Weight, unit are amu
atomic_mass = {
    'H' : 1.00794,
    'He': 4.002602,
    'Li': 6.941,
    'Be': 9.012182,
    'B': 10.811,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.9994,
    'F': 18.9984032,
    'Ne': 20.1797,
    'Na': 22.98976928,
    'Mg': 24.3050,
    'Al': 26.9815386,
    'Si': 28.0855,
    'P': 30.973762,
    'S': 32.065,
    'Cl': 35.453,
    'Ar': 39.948,
    'K': 39.0983,
    'Ca': 40.078,
    'Sc': 44.955912,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938045,
    'Fe': 55.845,
    'Co': 58.933195,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.64,
    'As': 74.92160,
    'Se': 78.96,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.90585,
    'Zr': 91.224,
    'Nb': 92.90638,
    'Mo': 95.96,
    'Tc': 98,
    'Ru': 101.07,
    'Rh': 102.90550,
    'Pd': 106.42,
    'Ag': 107.8682,
    'Cd': 112.411,
    'In': 114.818,
    'Sn': 118.710,
    'Sb': 121.760,
    'Te': 127.60,
    'I': 126.9044,
    'Xe': 131.293,
    'Cs': 132.9054519,
    'Ba': 137.327,
    'La': 138.90547,
    'Ce': 140.116,
    'Pr': 140.90765,
    'Nd': 144.242,
    'Pm': 145,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.92535,
    'Dy': 162.500,
    'Ho': 164.93032,
    'Er': 167.259,
    'Tm': 168.93421,
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
    'Hg': 200.59,
    'Tl': 204.3833,
    'Pb': 207.2,
    'Bi': 208.9804,
    'Po': 210,
    'At': 210,
    'Rn': 222,
    'Fr': 223,
    'Ra': 226,
    'Ac': 227,
    'Th': 232.03806,
    'Pa': 231.03588,
    'U': 238.02891,
    'Np': 237,
    'Pu': 244
}

# Crystal Lattice parameters (a, b, c, alpha, beta, gamma)
# a,b,c in angstroms
# alpha, beta, gamma in degrees
lattice_parameters = {
    "H": (3.75, 3.75, 6.12, 90, 90, 120),
    "He": (3.57, 3.57, 5.83, 90, 90, 120),
    "Li": (3.491, 3.491, 3.491, 90, 90, 90),
    "Be": (2.2866, 2.2866, 3.5833, 90, 90, 120),
    "B": (5.06, 5.06, 5.06, 58.06, 58.06, 58.06),
    "C": (3.567, 3.567, 3.567, 90, 90, 90),
    "N": (5.66, 5.66, 5.66, 90, 90, 90),
    "Ne": (4.66, 4.66, 4.66, 90, 90, 90),
    "Na": (4.225, 4.225, 4.225, 90, 90, 90),
    "Mg": (3.21, 3.21, 5.21, 90, 90, 120),
    "Al": (4.05, 4.05, 4.05, 90, 90, 90),
    "Si": (5.4310205, 5.4310205, 5.4310205, 90, 90, 90),
    "Ar": (5.31, 5.31, 5.31, 90, 90, 90),
    "K": (5.225, 5.225, 5.225, 90, 90, 90),
    "Ca": (5.58, 5.58, 5.58, 90, 90, 90),
    "Sc": (3.31, 3.31, 5.27, 90, 90, 120),
    "Ti": (2.95, 2.95, 4.68, 90, 90, 120),
    "V": (3.03, 3.03, 3.03, 90, 90, 90),
    "Cr": (2.88, 2.88, 2.88, 90, 90, 90),
    "Fe": (2.87, 2.87, 2.87, 90, 90, 90),
    "Co": (2.51, 2.51, 4.07, 90, 90, 120),
    "Ni": (3.52, 3.52, 3.52, 90, 90, 90),
    "Cu": (3.61, 3.61, 3.61, 90, 90, 90),
    "Zn": (2.66, 2.66, 4.95, 90, 90, 120),
    "Ge": (5.658, 5.658, 5.658, 90, 90, 90),
    "As": (4.1018, 4.1018, 4.1018, 54.554, 54.554, 54.554),
    "Kr": (5.64, 5.64, 5.64, 90, 90, 90),
    "Rb": (5.585, 5.585, 5.585, 90, 90, 90),
    "Sr": (6.08, 6.08, 6.08, 90, 90, 90),
    "Y": (3.65, 3.65, 5.73, 90, 90, 120),
    "Zr": (3.23, 3.23, 5.15, 90, 90, 120),
    "Nb": (3.3, 3.3, 3.3, 90, 90, 90),
    "Mo": (3.15, 3.15, 3.15, 90, 90, 90),
    "Tc": (2.74, 2.74, 4.4, 90, 90, 120),
    "Ru": (2.71, 2.71, 4.28, 90, 90, 120),
    "Rh": (3.8, 3.8, 3.8, 90, 90, 90),
    "Pd": (3.89, 3.89, 3.89, 90, 90, 90),
    "Ag": (4.09, 4.09, 4.09, 90, 90, 90),
    "Cd": (2.98, 2.98, 5.62, 90, 90, 120),
    "In": (3.25, 3.25, 4.95, 90, 90, 90),
    "Sn": (6.49, 6.49, 6.49, 90, 90, 90),
    "Sb": (4.4898, 4.4898, 4.4898, 57.233, 57.233, 57.233),
    "Xe": (6.13, 6.13, 6.13, 90, 90, 90),
    "Cs": (6.045, 6.045, 6.045, 90, 90, 90),
    "Ba": (5.02, 5.02, 5.02, 90, 90, 90),
    "Ce": (5.16, 5.16, 5.16, 90, 90, 90),
    "Eu": (4.58, 4.58, 4.58, 90, 90, 90),
    "Gd": (3.63, 3.63, 5.78, 90, 90, 120),
    "Tb": (3.6, 3.6, 5.7, 90, 90, 120),
    "Dy": (3.59, 3.59, 5.65, 90, 90, 120),
    "Ho": (3.58, 3.58, 5.62, 90, 90, 120),
    "Er": (3.56, 3.56, 5.59, 90, 90, 120),
    "Tm": (3.54, 3.54, 5.56, 90, 90, 120),
    "Yb": (5.45, 5.45, 5.45, 90, 90, 90),
    "Lu": (3.5, 3.5, 5.55, 90, 90, 120),
    "Hf": (3.19, 3.19, 5.05, 90, 90, 120),
    "Ta": (3.3, 3.3, 3.3, 90, 90, 90),
    "W": (3.16, 3.16, 3.16, 90, 90, 90),
    "Re": (2.76, 2.76, 4.46, 90, 90, 120),
    "Os": (2.74, 2.74, 4.32, 90, 90, 120),
    "Ir": (3.84, 3.84, 3.84, 90, 90, 90),
    "Pt": (3.92, 3.92, 3.92, 90, 90, 90),
    "Au": (4.08, 4.08, 4.08, 90, 90, 90),
    "Tl": (3.46, 3.46, 5.52, 90, 90, 120),
    "Pb": (4.95, 4.95, 4.95, 90, 90, 90),
    "Bi": (4.7236, 4.7236, 4.7236, 57.35, 57.35, 57.35),
    "Po": (3.34, 3.34, 3.34, 90, 90, 90),
    "Ac": (5.31, 5.31, 5.31, 90, 90, 90),
    "Th": (5.08, 5.08, 5.08, 90, 90, 90),
    "Pa": (3.92, 3.92, 3.24, 90, 90, 90),
    "ZnSe": (5.6676, 5.6676, 5.6676, 90, 90, 90),
    "ZnTe": (6.101, 6.101, 6.101, 90, 90, 90),
    "CdS": (5.832, 5.832, 5.832, 90, 90, 90),
    "CdSe": (6.05, 6.05, 6.05, 90, 90, 90),
    "CdTe": (6.477, 6.477, 6.477, 90, 90, 90),
    "BN": (3.615, 3.615, 3.615, 90, 90, 90),
    "GaSb": (6.0954, 6.0954, 6.0954, 90, 90, 90),
    "GaAs": (5.65315, 5.65315, 5.65315, 90, 90, 90),
    "GaMnAs": (5.65, 5.65, 5.65, 90, 90, 90),
    "GaP": (5.4505, 5.4505, 5.4505, 90, 90, 90),
    "InP": (5.86875, 5.86875, 5.86875, 90, 90, 90),
    "InAs": (6.05838, 6.05838, 6.05838, 90, 90, 90),
    "InSb": (6.47877, 6.47877, 6.47877, 90, 90, 90),
    "LaMnO3": (5.531, 5.602, 7.742, 90, 90, 90),
    "LaAlO3": (5.377, 5.377, 5.377, 60.13, 60.13, 60.13),
    "La0.7Sr0.3MnO3": (5.4738, 5.4738, 5.4738, 60.45, 60.45, 60.45),
    "Gd3Ga5O12": (12.383, 12.383, 12.383, 90, 90, 90),
}


# Crytal Lattice type
# cubic = cubic
# bcc = body centered cubic
# fcc = face centered cubic
# diamond = diamond
# hcp = hexaganol closed packed
# hex = hexagonal
# rhomb = rhombohedral
# zinc = zinc blende
lattice_type = {
    'H' : 'hcp',
    'He': 'hcp',
    'Li': 'bcc',
    'Be': 'hcp',
    'B': 'rhomb',
    'C': 'diamond',
    'N': 'cubic',
    'Ne': 'fcc',
    'Na': 'bcc',
    'Mg': 'hcp',
    'Al': 'fcc',
    'Si': 'diamond',
    'Ar': 'fcc',
    'K': 'bcc',
    'Ca': 'fcc',
    'Sc': 'hcp',
    'Ti': 'hcp',
    'V': 'bcc',
    'Cr': 'bcc',
    'Mn': 'cubic',
    'Fe': 'bcc',
    'Co': 'hcp',
    'Ni': 'fcc',
    'Cu': 'fcc',
    'Zn': 'hcp',
    'Ge': 'diamond',
    'As': 'rhomb',
    'Se': 'hex',
    'Kr': 'fcc',
    'Rb': 'bcc',
    'Sr': 'fcc',
    'Y': 'hcp',
    'Zr': 'hcp',
    'Nb': 'bcc',
    'Mo': 'bcc',
    'Tc': 'hcp',
    'Ru': 'hcp',
    'Rh': 'fcc',
    'Pd': 'fcc',
    'Ag': 'fcc',
    'Cd': 'hcp',
    'In': 'tetr',
    'Sn': 'diamond',
    'Sb': 'rhomb',
    'Te': 'hex',
    'Xe': 'fcc',
    'Cs': 'bcc',
    'Ba': 'bcc',
    'La': 'hex',
    'Ce': 'fcc',
    'Pr': 'hex',
    'Nd': 'hex',
    'Eu': 'bcc',
    'Gd': 'hcp',
    'Tb': 'hcp',
    'Dy': 'hcp',
    'Ho': 'hcp',
    'Er': 'hcp',
    'Tm': 'hcp',
    'Yb': 'fcc',
    'Lu': 'hcp',
    'Hf': 'hcp',
    'Ta': 'bcc',
    'W': 'bcc',
    'Re': 'hcp',
    'Os': 'fcc',
    'Ir': 'fcc',
    'Pt': 'fcc',
    'Au': 'fcc',
    'Hg': 'rhomb',
    'Tl': 'hcp',
    'Pb': 'fcc',
    'Bi': 'rhomb',
    'Po': 'cubic',
    'Ac': 'fcc',
    'Th': 'fcc',
    'Pa': 'tetr',
    'ZnSe': 'zinc',
    'ZnTe': 'zinc',
    'CdS': 'zinc',
    'CdSe': 'zinc',
    'CdTe': 'zinc',
    'BN': 'zinc',
    'GaSb': 'zinc',
    'GaAs': 'zinc',
    'GaMnAs': 'zinc',
    'GaP': 'zinc',
    'Gd3Ga5O12': 'cubic',
    'InP': 'zinc',
    'InAs': 'zinc',
    'InSb': 'zinc',
    'LaMnO3': 'ortho',
    'LaAlO3': 'rhomb',
    'LaAlO3': 'rhomb',
    'La0.7Sr0.3MnO3': 'rhomb',
    'GGG': 'cubic'
}

# define units and constants
units = {
    "fm": 1e15,
    "pm": 1e12,
    "ang": 1e10,
    "nm": 1e9,
    "um": 1e6,
    "mm": 1e3,
    "cm": 1e2,
    "km": 1e-3,
    "kHz": 1e-3,
    "MHz": 1e-6,
    "GHz": 1e-9,
    "THz": 1e-12,
    "PHz": 1e-15,
    "inch": 39.370079,
    "mile": 0.000621,
    "ft": 3.28084,
    "yard": 1.093613,
    "mil": 39.370079 * 1000,
    "barn": 1e28,
    "fs": 1e15,
    "ps": 1e12,
    "ns": 1e9,
    "us": 1e6,
    "ms": 1e3,
    "min": 1 / 60.0,
    "hour": 1 / 3600.0,
    "day": 1 / (3600 * 24.0),
    "mdeg": 1e3,
    "udeg": 1e6,
    "ndeg": 1e9,
    "rad": np.pi / 180,
    "mrad": np.pi / 180 * 1e3,
    "urad": np.pi / 180 * 1e6,
    "nrad": np.pi / 180 * 1e9,
    "asec": 3600,
    "amin": 60,
    "g": 1e3,
    "eV": 6.2415e18,
    "erg": 1e7,
    "cal": 0.239,
    "mJ": 1e3,
    "uJ": 1e6,
    "nJ": 1e9,
    "pJ": 1e9,
    "Torr": 7.5006e-3,
}


# Constants in MKS units
#    NA : Avagadro Constant
#  eRad : Classical electron radius
#     e : electron charge in Coulombs
#     c : speed of light in m
#     h : Plank constant in Js
#  hbar : reduced Plank constant in Js
# emass : electron mass in kg
# pmass : proton mass in kg
#     k : Boltzman constant in J/K
#    mu : Permeability of free space in N/A^2
#    eo : Permittivity of free space in F/m
#   S-B : Stefan-Boltzmann constant
const = {
    'NA': 6.02212e23,
    'eRad': 2.81794e-15,
    'e': 1.602176e-19,
    'c': 2.99792458e8,
    'h': 6.62606896e-34,
    'hbar': 1.054571628e-34,
    'emass': 9.10938215e-31,
    'pmass': 1.672621637e-27,
    'k': 1.3806504e-23,
    'mu': 12.566370614e-7,
    'eo': 8.854187817e-12,
    'S-B': 5.670373e-8,
}
