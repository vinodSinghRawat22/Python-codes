# 18. Create a dictionary and iterate over its keys and values.

special_forces = {
    "India": "NSG",
    "USA": "Navy SEALs",
    "UK": "SAS",
    "Russia": "Spetsnaz"
}

for key, value in special_forces.items() :
    print(f"-- Special force {value} is from {key}. ")