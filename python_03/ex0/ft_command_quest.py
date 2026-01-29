import sys

print("=== Command Quest ===")
args: list = sys.argv

if len(args) == 1:
    print("No arguments proivided!")
    print("Program name:", args[0])
else:
    print("Program name:", args[0])
    print("Arguments received:", len(args) - 1)
    for i, arg in enumerate(args[1:], 1):
        print(f"Argument {i}: {arg}")
    
print("Total arguments:", len(args))
