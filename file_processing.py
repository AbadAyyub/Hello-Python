from pathlib import Path


path = Path("ecommerce")
path.mkdir("")

#print(path.glob("*.py"))

for file in path.glob("*.py"):
    print(file)



