# Object Mapper Example

This is an example of how to build a simple object mapper like you might use to create an ORM.
It uses the `__init_subclass__` object creation hook that was added by [PEP 487](https://peps.python.org/pep-0487/)
in Python 3.6 and the [descriptor protocol](https://docs.python.org/3/howto/descriptor.html#id12).

I used a similar but more robust implementation of this object mapper to create a object-to-graph mapper for the AWS Neptune graph database.

- `core.py` is the logic for the mapper.
- `models.py` defines an example `Person` class that implements the object mapper.
- `examples.py` provides some examples of using the `Person` model and object mapper logic.