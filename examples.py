from models import Person

person = Person(name="Jerry Seinfeld", age=69)
print(person.__dict__)
print(f"Person {person.name} is {person.age}")

# >> {'name': 'Jerry Seinfeld', 'age': 69}
# >> Person Jerry Seinfeld is 69

person = Person()
person.name = "Julia Louis-Dreyfus"
person.age = 62
print(f"Person {person.name} is {person.age}")

# >> Person Julia Louis-Dreyfus is 62

data = {"name": "Jason Alexander", "age": 64, "character_name": "George Costanza"}
person = Person(**data)
print(f"Person {person.name} is {person.age}")

# >> Person Jason Alexander is 64

person = Person(name="Michael Richards", age=74, character_name="Cosmo Kramer")
print(person.__dict__)
print(f"Person {person.name} is {person.age}")

# >> {'name': 'Michael Richards', 'age': 74}
# >> Person Michael Richards is 74

try:
    person.age = "Invalid"
except ValueError as v_e:
    print(f"We got the error expected: {v_e}")

# >> We got the error expected: Integer data type expected. Invalid is not a valid integer.
