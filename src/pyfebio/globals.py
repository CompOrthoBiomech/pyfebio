from pydantic_xml import BaseXmlModel, element


class Constants(BaseXmlModel, validate_assignment=True):
    T: float = element(default=0)
    P: float = element(default=0)
    R: float = element(default=8.31446)
    Fc: float = element(default=96485.3)


class Globals(BaseXmlModel, validate_assignment=True):
    constants: Constants = element(default=Constants(), tag="Constants")
