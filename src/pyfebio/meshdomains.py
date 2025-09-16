from typing import Literal, Optional

from pydantic_xml import BaseXmlModel, attr, element


class SolidDomain(BaseXmlModel, validate_assignment=True):
    name: str = attr(default="SolidPart")
    type: Optional[
        Literal[
            "elastic-solid",
            "three-field-solid",
            "rigid-solid",
            "udg-hex",
            "sri-solid",
            "remodelling-solid",
            "ut4-solid",
        ]
    ] = attr(default=None)
    elem_type: Optional[
        Literal["HEX8G6", "TET4G4", "TET10G4", "TET10GL11", "TET15G8", "TET15G11"]
    ] = attr(default=None)
    mat: str = attr(default="material")
    alpha: Optional[float] = element(default=None)
    iso_stab: Optional[Literal[0, 1]] = element(default=None)


class ShellDomain(BaseXmlModel, validate_assignment=True):
    name: str = attr(default="ShellPart")
    type: Literal[
        "elastic-shell",
        "three-field-shell",
        "rigid-shell",
        "elastic-shell-old",
        "elastic-shell-eas",
        "elastic-shell-ans",
    ] = attr(default="elastic-shell")
    mat: str = attr(default="material")
    shell_thickness: float = element(default=0.01)


class MeshDomains(BaseXmlModel, validate_assignment=True):
    solid_domains: list[SolidDomain] = element(default=[], tag="SolidDomain")
    shell_domains: list[ShellDomain] = element(default=[], tag="ShellDomain")

    def add_solid_domain(self, new_solid_domain: SolidDomain):
        self.solid_domains.append(new_solid_domain)

    def add_shell_domain(self, new_shell_domain: ShellDomain):
        self.shell_domains.append(new_shell_domain)
