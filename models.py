import core


class Person(core.BaseModel):
    name = core.Property(core.StringDataType)
    age = core.Property(core.IntegerDataType)
