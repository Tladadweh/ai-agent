from functions.run_python_file import run_python_file


print("Test 1: main.py without args")
print(run_python_file("calculator", "main.py"))

print("\nTest 2: main.py with args")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\nTest 3: tests.py")
print(run_python_file("calculator", "tests.py"))

print("\nTest 4: outside working directory")
print(run_python_file("calculator", "../main.py"))

print("\nTest 5: nonexistent file")
print(run_python_file("calculator", "nonexistent.py"))

print("\nTest 6: non-Python file")
print(run_python_file("calculator", "lorem.txt"))
