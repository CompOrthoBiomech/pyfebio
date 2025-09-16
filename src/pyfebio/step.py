from typing import List, Optional

from pydantic_xml import BaseXmlModel, attr, element

from .boundary import Boundary
from .constraints import Constraints
from .contact import Contact
from .control import Control
from .initial import Initial
from .loads import Loads
from .rigid import Rigid


class StepEntry(BaseXmlModel, validate_assignment=True):
    id: int = attr()
    name: str = attr(default="Step")
    control: Optional[Control] = element(default=None, tag="Control")
    initial: Optional[Initial] = element(default=None, tag="Initial")
    boundary: Optional[Boundary] = element(default=None, tag="Boundary")
    loads: Optional[Loads] = element(default=None, tag="Loads")
    constraints: Optional[Constraints] = element(default=None, tag="Constraints")
    contact: Optional[Contact] = element(default=None, tag="Contact")
    rigid: Optional[Rigid] = element(default=None, tag="Rigid")


class Step(BaseXmlModel, validate_assignment=True):
    all_steps: List[StepEntry] = element(default=[], tag="step")

    def add_step(self, new_step: StepEntry):
        self.all_steps.append(new_step)
