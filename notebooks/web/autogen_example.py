# filename: autogen_example.py

# This is a template for a Python script that uses AutoGen to generate code.
# AutoGen uses templates defined in a separate file, so this script will
# load a template and use it to generate code.

from autogen import AutoGen

# Create an instance of AutoGen
ag = AutoGen()

# Define a template for a function that squares a number
template = """
def square_{i}():
    return {i} * {i}
"""

# Use the template to generate functions for squaring numbers from 1 to 10
for i in range(1, 11):
    ag.add(template.format(i=i))

# Write the generated code to a file
with open('generated_code.py', 'w') as f:
    f.write(ag.generate())