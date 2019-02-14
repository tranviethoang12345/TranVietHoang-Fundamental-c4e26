inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"],
}
print("First", inventory, sep=("\n"))
print("")

inventory["pocket"] = ["seashell", "strange berry", "lint"]

inventory["backpack"].remove("dagger")

inventory["gold"] += 50

print("After", inventory, sep=("\n"))
