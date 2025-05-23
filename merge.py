import nbformat
from nbmerge import merge_notebooks

# Fusionner les 2 notebooks
merged = merge_notebooks([
    "Projet_Airbnb_Athanaël_Sautereau_Guillaume_Scheid.ipynb",
    "Project_Airbnb_Project_add_Sublet_Yoann_Xu_Guillaume.ipynb"
])

# Sauvegarder
with open("Fusion_Airbnb.ipynb", "w") as f:
    nbformat.write(merged, f)
