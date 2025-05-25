import psutil
import os
from matplotlib import mathtext, font_manager
import matplotlib as mpl

current_dir = os.getcwd()
current_dir = current_dir.replace("C:\\", "/")
current_dir = current_dir.replace("\\", "/")

mpl.rcParams['savefig.transparent'] = True

#texFont = font_manager.FontProperties(size=30, fname="./OpenSans-Medium.ttf")
texFont = font_manager.FontProperties(size=40, family='serif', math_fontfamily='cm')

valeur = r"Compléter avec un autre coefficient binomial : $ \binom{n}{n-k}=\ldots\,?$"
mathtext.math_to_image(valeur, "output.png", prop=texFont, dpi=300, format='png' , color="white")
