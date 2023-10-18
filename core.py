class BaseModel:
    __attr_map__ = None

    def __init_subclass__(cls, **kwargs):
        """
        This gets called when Python is defining subclasses of BaseModel.
        If you needed to register anything with the BaseModel, you could do it here.
        """
        super().__init_subclass__()
        cls.__attr_map__ = {
            k: v for k, v in cls.__dict__.items() if isinstance(v, Property)
        }

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__attr_map__.keys():
                setattr(self, key, value)


class Property:
    """
    This implements Python's descriptor protocol.
    """

    def __init__(self, data_type, property_name=None, default=None):
        if isinstance(data_type, type):
            data_type = data_type()
        self._data_type = data_type
        self._property_name = property_name
        self._default = default

    def __set_name__(self, owner, name):
        """
        This method is called during class creation. When the class (owner) is defined,
        it makes a callback to this function. The class attribute (name) is stored in the
        __dict__ attribute of the object it's attached to using the same name from the
        descriptor itself.
        """
        self.name = name

    def __get__(self, obj, obj_type=None):
        """
        This method is called when the attribute (assigned to self.name) is accessed with
        dot notation on the object (obj). The MRO will first check __dict__ for the key named
        after the attribute you are looking for. If that fails, then you will get the result
        returned from the __get__ method of this descriptor named after the attribute you are
        looking for. The obj is Nnoe if the attribute is referenced on the class. The class
        should return the BaseProperty itself (self) when the class attribute is referenced.
        """
        if obj is None:
            return self
        return obj.__dict__.get(self.name, self._default)

    def __set__(self, obj, value):
        """
        This method is called when the attribute (stored in self.name) is assigned a value
        with dot notation on the object (obj). The MRO will first check the object's __dict__
        for the key named after the attribute you are looking for. If that fails, MRO will then
        use this method to set the attribute.
        """
        value = self._data_type.validate(value)
        obj.__dict__[self.name] = value

    @property
    def data_type(self):
        self._data_type

    @property
    def default(self):
        return self._default


class BaseDataType:
    def validate(self, value):
        """
        Verifies the object attributes are of the correct data type according to the definition on the
        object. Validation occurs in the object when the attribute is set by dot notation (in the descriptor's
        __set__ method) or setattr function.
        """
        return value


class StringDataType(BaseDataType):
    def validate(self, value):
        if value is not None:
            if isinstance(value, str):
                return value
            elif isinstance(value, (int, float)):
                return str(value)
            else:
                raise ValueError(
                    f"String data type expected. {value} is not a valid string."
                )


class IntegerDataType(BaseDataType):
    def validate(self, value):
        if value is not None:
            try:
                return int(value)
            except ValueError:
                raise ValueError(
                    f"Integer data type expected. {value} is not a valid integer."
                ) from None
