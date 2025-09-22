from typing import Annotated, List, Literal, Optional, TypeAlias, Union

from pydantic import AfterValidator, PositiveInt
from pydantic_xml import BaseXmlModel, attr, element

from ._types import StringFloatVec3, StringFloatVec9


class MaterialAxisVector(BaseXmlModel, validate_assignment=True, extra="forbid"):
    type: Literal["vector"] = attr(default="vector", frozen=True)
    a: StringFloatVec3 = element(default="1.0,0.0,0.0")
    d: StringFloatVec3 = element(default="0.0,1.0,0.0")


class FiberVector(BaseXmlModel, validate_assignment=True, extra="forbid"):
    type: Literal["vector"] = attr(default="vector", frozen=True)
    text: StringFloatVec3 = "1.0,0.0,0.0"


class MaterialParameter(BaseXmlModel, validate_assignment=True, extra="forbid"):
    type: Optional[Literal["map", "math"]] = attr(default=None)
    text: str | int | float


class DynamicMaterialParameter(BaseXmlModel, validate_assignment=True, extra="forbid"):
    type: Optional[Literal["map", "math"]] = attr(default=None)
    lc: int = attr(default=1, ge=1)
    text: str | int | float = 1.0


# Material Paramter Validators
def mat_is_positive_float(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text <= 0.0:
            raise ValueError(f"{parameter.text=} must be greater than 0.0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_non_negative_float(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text < 0.0:
            raise ValueError(f"{parameter.text=} must be greater than or equal to 0.0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_gte_one_float(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text < 1.0:
            raise ValueError(f"{parameter.text=} must be greater than or equal to 1.0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_gt_one_float(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text <= 1.0:
            raise ValueError(f"{parameter.text=} must be greater than 1.0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_gte_two_float(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text < 2.0:
            raise ValueError(f"{parameter.text=} must be greater than or equal to 2.0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_lte_onethird_gte_zero(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text < 0.0 or parameter.text > 1.0 / 3.0:
            raise ValueError(f"{parameter.text=} must be in domain [0.0, 1./3.]")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_lte_90_gte_0(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float | int):
        if parameter.text < 0.0 or parameter.text > 90.0:
            raise ValueError(f"{parameter.text=} must be in domain [0.0, 90.0]")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_positive_int(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float):
        raise ValueError(f"{parameter.text=} must be type(int)")
    elif isinstance(parameter.text, int):
        if parameter.text < 1:
            raise ValueError(f"{parameter.text=} must be greater than 0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_positive_int_mult10(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif isinstance(parameter.text, float):
        raise ValueError(f"{parameter.text=} must be type(int)")
    elif isinstance(parameter.text, int):
        if parameter.text % 10 != 0 and parameter.text > 0:
            raise ValueError(f"{parameter.text=} must be a multiple of 10 and greater than 0")
        return parameter
    else:
        raise ValueError(f"{parameter.text=} of type(str) but {parameter.type=} when it must be 'map' or 'math'")


def mat_is_string_float_vec3(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif parameter.text is StringFloatVec3:
        return parameter
    else:
        raise ValueError(f"{parameter.text=} must be of type(StringFloatVec3)")


def mat_is_string_float_vec9(parameter: MaterialParameter) -> MaterialParameter:
    if parameter.type == "map" or parameter.type == "math":
        if not isinstance(parameter.text, str):
            raise ValueError(
                f"MaterialParameter {parameter.type=}, which requires parameter.text to be of type(str), but {parameter.text=}."
            )
        return parameter
    elif parameter.text is StringFloatVec9:
        return parameter
    else:
        raise ValueError(f"{parameter.text=} must be of type(StringFloatVec9)")


MatPositiveFloat: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_positive_float)]
MatNonNegativeFloat: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_non_negative_float)]
MatGTEOneFloat: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_gte_one_float)]
MatGTOneFloat: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_gt_one_float)]
MatGTETwoFloat: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_gte_two_float)]
MatLTE_OneThird_GTE_Zero: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_lte_onethird_gte_zero)]
MatLTE_90_GTE_0: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_lte_90_gte_0)]
MatPositiveInt: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_positive_int)]
MatPositiveIntMult10: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_positive_int_mult10)]
MatStringFloatVec3: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_string_float_vec3)]
MatStringFloatVec9: TypeAlias = Annotated[MaterialParameter, AfterValidator(mat_is_string_float_vec9)]


class SolidBoundMolecule(BaseXmlModel, tag="solid_bound", extra="forbid"):
    sbm: int = attr(default=1)
    rho0: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    rhomin: MatPositiveFloat = element(default=MaterialParameter(text=0.1))
    rhomax: MatPositiveFloat = element(default=MaterialParameter(text=5.0))


class ArrudaBoyce(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Arruda-Boyce unconstrained")
    type: Literal["Arruda-Boyce unconstrained"] = attr(default="Arruda-Boyce unconstrained", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    N: MatPositiveInt = element(default=MaterialParameter(text=5))
    n_term: int = element(default=3, ge=3, le=30)
    kappa: MatPositiveFloat = element(default=MaterialParameter(text=1.0))


class CarterHayes(BaseXmlModel, tag="solid", extra="forbid"):
    name: str = attr(default="Carter-Hayes")
    type: Literal["Carter-Hayes"] = attr(default="Carter-Hayes", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E0: MatPositiveFloat = element(default=MaterialParameter(text=10000.0))
    rho0: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    gamma: MatPositiveFloat = element(default=MaterialParameter(text=2.0))
    v: MatNonNegativeFloat = element(default=MaterialParameter(text=0.3))
    sbm: MatPositiveInt = element(default=MaterialParameter(text=1))


class CellGrowth(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Cell Growth")
    type: Literal["cell growth"] = attr(default="cell growth", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    phir: MatPositiveFloat = element(default=DynamicMaterialParameter(text=10000.0))
    cr: MatPositiveFloat = element(default=DynamicMaterialParameter(text=1.0))
    ce: MatPositiveFloat = element(default=MaterialParameter(text=300.0))


class CubicCLE(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="cubic CLE")
    type: Literal["cubic CLE"] = attr(default="cubic CLE", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    lp1: MatPositiveFloat = element(default=MaterialParameter(text=13.01))
    lm1: MatPositiveFloat = element(default=MaterialParameter(text=0.49))
    l2: MatPositiveFloat = element(default=MaterialParameter(text=0.66))
    mu: MatPositiveFloat = element(default=MaterialParameter(text=0.16))


class CoupledMooneyRivlin(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="coupled Mooney-Rivlin")
    type: Literal["coupled Mooney-Rivlin"] = attr(default="coupled Mooney-Rivlin", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    c2: MatNonNegativeFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=100.0))


class CoupledVerondaWestmann(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="coupled Veronda-Westmann")
    type: Literal["coupled Veronda-Westmann"] = attr(default="coupled Veronda-Westmann", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    c2: MatNonNegativeFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=100.0))


class DonnanEquilibrium(BaseXmlModel, tag="solid", extra="forbid"):
    type: Literal["Donnan equilibrium"] = attr(default="Donnan equilibrium", frozen=True)
    phiw0: MatPositiveFloat = element(default=MaterialParameter(text=0.8))
    cF0: MatPositiveFloat = element(default=DynamicMaterialParameter(text=1.0))
    bosm: MatPositiveFloat = element(default=MaterialParameter(text=0.8))


class EllipsoidalFiberDistribution(BaseXmlModel, tag="solid", extra="forbid"):
    type: Literal["ellipsoidal fiber distribution"] = attr(default="ellipsoidal fiber distribution", frozen=True)
    ksi: StringFloatVec3 = element(default="10,12,15")
    beta: StringFloatVec3 = element(default="2.5,3,3")


class EllipsoidalFiberDistributionNeoHookean(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="EFD neo-Hookean")
    type: Literal["EFD neo-Hookean"] = attr(default="EFD neo-Hookean", frozen=True)
    id: int = attr(ge=1)
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatPositiveFloat = element(default=MaterialParameter(text=0.3))
    beta: StringFloatVec3 = element(default="2.5,3.0,3.0")
    ksi: StringFloatVec3 = element(default="1.0,1.0,1.0")


class EllipsoidalFiberDistributionDonnanEquilibrium(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="EFD Donnan equilibrium")
    type: Literal["EFD Donnan equilibrium"] = attr(default="EFD Donnan equilibrium", frozen=True)
    id: int = attr(ge=1)
    phiw0: MatPositiveFloat = element(default=MaterialParameter(text=0.8))
    cF0: DynamicMaterialParameter = element(default=DynamicMaterialParameter(text=0.3))
    bosm: MaterialParameter = element(default=MaterialParameter(text=300))
    beta: StringFloatVec3 = element(default="2.5,3.0,3.0")
    ksi: StringFloatVec3 = element(default="1.0,1.0,1.0")


class FungOrthotropicCompressible(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Fung-ortho-compressible")
    type: Literal["Fung-ortho-compressible"] = attr(default="Fung-ortho-compressible", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E1: MatPositiveFloat = element(default=MaterialParameter(text=124.0))
    E2: MatPositiveFloat = element(default=MaterialParameter(text=124.0))
    E3: MatPositiveFloat = element(default=MaterialParameter(text=36.0))
    G12: MatPositiveFloat = element(default=MaterialParameter(text=67.0))
    G23: MatPositiveFloat = element(default=MaterialParameter(text=40.0))
    G31: MatPositiveFloat = element(default=MaterialParameter(text=40.0))
    v12: MatPositiveFloat = element(default=MaterialParameter(text=0.075))
    v23: MatPositiveFloat = element(default=MaterialParameter(text=0.87))
    v31: MatPositiveFloat = element(default=MaterialParameter(text=0.26))
    c: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=120.0))


class GentCompressible(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="compressible Gent")
    type: Literal["compressible Gent"] = attr(default="compressible Gent", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    G: MatPositiveFloat = element(default=MaterialParameter(text=3.14))
    Jm: MatPositiveFloat = element(default=MaterialParameter(text=1.5))
    K: MatPositiveFloat = element(default=MaterialParameter(text=1e5))


class HolmesMow(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Holmes-Mow")
    type: Literal["Holmes-Mow"] = attr(default="Holmes-Mow", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatPositiveFloat = element(default=MaterialParameter(text=0.35))
    beta: MatPositiveFloat = element(default=MaterialParameter(text=0.25))


class HolzapfelGasserOgdenUnconstrained(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="HGO unconstrained")
    type: Literal["HGO unconstrained"] = attr(default="HGO unconstrained", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c: MatPositiveFloat = element(default=MaterialParameter(text=7.64))
    k1: MatPositiveFloat = element(default=MaterialParameter(text=996.6))
    k2: MatPositiveFloat = element(default=MaterialParameter(text=524.6))
    gamma: MatLTE_90_GTE_0 = element(default=MaterialParameter(text=49.98))
    kappa: MatLTE_OneThird_GTE_Zero = element(default=MaterialParameter(text=0.226))
    k: MatPositiveFloat = element(default=MaterialParameter(text=7.64e3))
    mat_axis: Optional[MaterialAxisVector] = element(default=None)
    fiber: Optional[FiberVector] = element(default=None)


class IsotropicElastic(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="isotropic elastic")
    type: Literal["isotropic elastic"] = attr(default="isotropic elastic", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatNonNegativeFloat = element(default=MaterialParameter(text=0.3))


class IsotropicHencky(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="isotropic Hencky")
    type: Literal["isotropic Hencky"] = attr(default="isotropic Hencky", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1000.0))
    v: MatPositiveFloat = element(default=MaterialParameter(text=0.45))


class KinematicGrowth(BaseXmlModel, tag="material", extra="forbid"):
    elastic: str = element()
    growth: Literal["volume", "growth", "area growth", "fiber growth"] = element(default="volume")


class LargePoissonRatioLigament(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="PRLig")
    type: Literal["PRLig"] = attr(default="PRLig", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=90.0))
    c2: MatPositiveFloat = element(default=MaterialParameter(text=160.0))
    mu: MatPositiveFloat = element(default=MaterialParameter(text=0.025))
    v0: MatPositiveFloat = element(default=MaterialParameter(text=5.85))
    m: MatPositiveFloat = element(default=MaterialParameter(text=100.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=1.55))


class NaturalNeoHookean(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="natural neo-Hookean")
    type: Literal["natural neo-Hookean"] = attr(default="natural neo-Hookean", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatNonNegativeFloat = element(default=MaterialParameter(text=0.3))


class NeoHookean(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="neo-Hookean")
    type: Literal["neo-Hookean"] = attr(default="neo-Hookean", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatNonNegativeFloat = element(default=MaterialParameter(text=0.3))


class OrthotropicElastic(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="orthotropic elastic")
    type: Literal["orthotropic elastic"] = attr(default="orthotropic elastic", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E1: MatPositiveFloat = element(default=MaterialParameter(text=13.4))
    E2: MatPositiveFloat = element(default=MaterialParameter(text=14.1))
    E3: MatPositiveFloat = element(default=MaterialParameter(text=22.9))
    v12: MatNonNegativeFloat = element(default=MaterialParameter(text=0.42))
    v23: MatNonNegativeFloat = element(default=MaterialParameter(text=0.23))
    v31: MatNonNegativeFloat = element(default=MaterialParameter(text=0.38))
    G12: MatPositiveFloat = element(default=MaterialParameter(text=4.6))
    G23: MatPositiveFloat = element(default=MaterialParameter(text=6.2))
    G31: MatPositiveFloat = element(default=MaterialParameter(text=5.8))
    mat_axis: Optional[MaterialAxisVector] = element(default=None)


class OrthotropicCLE(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="orthotropic CLE")
    type: Literal["orthotropic CLE"] = attr(default="orthotropic CLE", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    lp11: MatPositiveFloat = element(default=MaterialParameter(text=13.01))
    lp22: MatPositiveFloat = element(default=MaterialParameter(text=13.01))
    lp33: MatPositiveFloat = element(default=MaterialParameter(text=13.01))
    lm11: MatPositiveFloat = element(default=MaterialParameter(text=0.49))
    lm22: MatPositiveFloat = element(default=MaterialParameter(text=0.49))
    lm33: MatPositiveFloat = element(default=MaterialParameter(text=0.49))
    l12: MatPositiveFloat = element(default=MaterialParameter(text=0.66))
    l23: MatPositiveFloat = element(default=MaterialParameter(text=0.66))
    l31: MatPositiveFloat = element(default=MaterialParameter(text=0.66))
    mu1: MatPositiveFloat = element(default=MaterialParameter(text=0.16))
    mu2: MatPositiveFloat = element(default=MaterialParameter(text=0.16))
    mu3: MatPositiveFloat = element(default=MaterialParameter(text=0.16))


class OsmoticVirialPressure(BaseXmlModel, tag="solid", extra="forbid"):
    name: str = attr(default="osmotic virial expansion")
    id: int = attr(ge=1)
    type: Literal["osmotic virial expansion"] = attr(default="osmotic virial expansion", frozen=True)
    phiw0: MaterialParameter = element(default=MaterialParameter(text=0.8))
    cr: DynamicMaterialParameter = element(default=DynamicMaterialParameter(text=100.0))
    c1: MaterialParameter = element(default=MaterialParameter(text=2.436e-6))
    c2: MaterialParameter = element(default=MaterialParameter(text=0.0))
    c3: MaterialParameter = element(default=MaterialParameter(text=0.0))


class PorousNeoHookean(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="porous neo-Hookean")
    type: Literal["porous neo-Hookean"] = attr(default="porous neo-Hookean", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    phi0: MatPositiveFloat = element(default=MaterialParameter(text=0.5))


class TransIsoMooneyRivlin(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="coupled trans-iso Mooney-Rivlin")
    type: Literal["coupled trans-iso Mooney-Rivlin"] = attr(default="coupled trans-iso Mooney-Rivlin", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c2: MatNonNegativeFloat = element(default=MaterialParameter(text=0.1))
    c3: MatNonNegativeFloat = element(default=MaterialParameter(text=0.0))
    c4: MatPositiveFloat = element(default=MaterialParameter(text=43.0))
    c5: MatPositiveFloat = element(default=MaterialParameter(text=3.0))
    lam_max: MatGTOneFloat = element(default=MaterialParameter(text=1.05))
    k: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    fiber: Optional[FiberVector] = element(default=None)


class UnconstrainedOgden(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Ogden")
    type: Literal["Ogden unconstrained"] = attr(default="Ogden unconstrained", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    m1: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    m2: Optional[MatPositiveFloat] = element(default=None)
    c2: Optional[MatPositiveFloat] = element(default=None)
    m3: Optional[MatPositiveFloat] = element(default=None)
    c3: Optional[MatPositiveFloat] = element(default=None)
    m4: Optional[MatPositiveFloat] = element(default=None)
    c4: Optional[MatPositiveFloat] = element(default=None)
    m5: Optional[MatPositiveFloat] = element(default=None)
    c5: Optional[MatPositiveFloat] = element(default=None)
    m6: Optional[MatPositiveFloat] = element(default=None)
    c6: Optional[MatPositiveFloat] = element(default=None)


UnconstrainedMaterials: TypeAlias = Union[
    ArrudaBoyce,
    CoupledMooneyRivlin,
    CoupledVerondaWestmann,
    CubicCLE,
    EllipsoidalFiberDistributionNeoHookean,
    FungOrthotropicCompressible,
    GentCompressible,
    HolmesMow,
    HolzapfelGasserOgdenUnconstrained,
    IsotropicElastic,
    IsotropicHencky,
    LargePoissonRatioLigament,
    NaturalNeoHookean,
    NeoHookean,
    PorousNeoHookean,
    OrthotropicElastic,
    OrthotropicCLE,
    TransIsoMooneyRivlin,
    UnconstrainedOgden,
]

EvolvingUnconstrainedMaterials: TypeAlias = Union[
    EllipsoidalFiberDistributionDonnanEquilibrium, CellGrowth, OsmoticVirialPressure
]


class MooneyRivlin(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Mooney-Rivlin")
    type: Literal["Mooney-Rivlin"] = attr(default="Mooney-Rivlin", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    c2: MatNonNegativeFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=1000.0))


class UncoupledHolmesMow(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Uncoupled-Holmes-Mow")
    type: Literal["uncoupled Holmes-Mow"] = attr(default="uncoupled Holmes-Mow", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    mu: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    beta: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=100.0))


class Ogden(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Ogden")
    type: Literal["Ogden"] = attr(default="Ogden", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    k: MatPositiveFloat = element(default=MaterialParameter(text=100.0))
    m1: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c1: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    m2: Optional[MatPositiveFloat] = element(default=None)
    c2: Optional[MatPositiveFloat] = element(default=None)
    m3: Optional[MatPositiveFloat] = element(default=None)
    c3: Optional[MatPositiveFloat] = element(default=None)
    m4: Optional[MatPositiveFloat] = element(default=None)
    c4: Optional[MatPositiveFloat] = element(default=None)
    m5: Optional[MatPositiveFloat] = element(default=None)
    c5: Optional[MatPositiveFloat] = element(default=None)
    m6: Optional[MatPositiveFloat] = element(default=None)
    c6: Optional[MatPositiveFloat] = element(default=None)


class HolzapfelGasserOgden(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="Holzapfel-Gasser-Ogden")
    type: Literal["Holzapfel-Gasser-Ogden"] = attr(default="Holzapfel-Gasser-Ogden", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    c: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    k1: MatPositiveFloat = element(default=MaterialParameter(text=10.0))
    k2: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    gamma: MatLTE_90_GTE_0 = element(default=MaterialParameter(text=45.0))
    kappa: MatLTE_OneThird_GTE_Zero = element(default=MaterialParameter(text=0.1))
    k: MatPositiveFloat = element(default=MaterialParameter(text=100.0))
    mat_axis: Optional[MaterialAxisVector] = element(default=None)
    fiber: Optional[FiberVector] = element(default=None)


UncoupledMaterials: TypeAlias = Union[MooneyRivlin, Ogden, HolzapfelGasserOgden]


class RigidBody(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="rigid body")
    type: Literal["rigid body"] = attr(default="rigid body", frozen=True)
    id: int = attr(ge=1)
    density: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    center_of_mass: Optional[StringFloatVec3] = element(default=None)
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    v: MatNonNegativeFloat = element(default=MaterialParameter(text=0.3))


# Unconstrained Fibers
class FiberExponentialPower(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-exp-pow", frozen=True)
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=5.0))
    alpha: MatNonNegativeFloat = element(default=MaterialParameter(text=20.0))
    beta: MatGTETwoFloat = element(default=MaterialParameter(text=2.0))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.0))
    fiber: Optional[FiberVector] = element(default=None)


class FiberNeoHookean(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-NH", frozen=True)
    mu: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    fiber: Optional[FiberVector] = element(default=None)


class FiberNaturalNeoHookean(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-natural-NH", frozen=True)
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    lam0: MatGTEOneFloat = element(default=MaterialParameter(text=1.0))
    fiber: Optional[FiberVector] = element(default=None)


class FiberToeLinear(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-pow-linear", frozen=True)
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    beta: MatGTETwoFloat = element(default=MaterialParameter(text=2.0))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.01))
    fiber: Optional[FiberVector] = element(default=None)


class FiberExponentialPowerLinear(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-exp-pow-linear", frozen=True)
    E: MatPositiveFloat = element(default=MaterialParameter(text=1080.0))
    alpha: MatNonNegativeFloat = element(default=MaterialParameter(text=1400.0))
    beta: MatGTETwoFloat = element(default=MaterialParameter(text=2.73))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.01))
    fiber: Optional[FiberVector] = element(default=None)


class FiberExponentialLinear(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-exp-linear", frozen=True)
    c3: MatNonNegativeFloat = element(default=MaterialParameter(text=0.0))
    c4: MatPositiveFloat = element(default=MaterialParameter(text=43.0))
    c5: MatPositiveFloat = element(default=MaterialParameter(text=3.0))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.05), tag="lambda")
    fiber: Optional[FiberVector] = element(default=None)


class FiberEntropyChain(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-entropy-chain", frozen=True)
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    N: MatGTOneFloat = element(default=MaterialParameter(text=2.0))
    n_term: MatPositiveInt = element(default=MaterialParameter(text=2))
    fiber: Optional[FiberVector] = element(default=None)


FiberModel: TypeAlias = Union[
    FiberNeoHookean,
    FiberNaturalNeoHookean,
    FiberToeLinear,
    FiberEntropyChain,
    FiberExponentialPower,
    FiberExponentialLinear,
    FiberEntropyChain,
]


# Uncoupled Fibers
class FiberExponentialPowerUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-exp-pow-uncoupled")
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=5.0))
    alpha: MatNonNegativeFloat = element(default=MaterialParameter(text=20.0))
    beta: MatGTETwoFloat = element(default=MaterialParameter(text=3.0))
    fiber: Optional[FiberVector] = element(default=None)


class FiberKiousisUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-Kiousis-uncoupled")
    d1: MatPositiveFloat = element(default=MaterialParameter(text=500.0))
    d2: MatGTOneFloat = element(default=MaterialParameter(text=2.25))
    n: MatNonNegativeFloat = element(default=MaterialParameter(text=3))
    fiber: Optional[FiberVector] = element(default=None)


class FiberToeLinearUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="fiber-pow-linear-uncoupled", frozen=True)
    E: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    beta: MatGTETwoFloat = element(default=MaterialParameter(text=2.0))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.01))
    fiber: Optional[FiberVector] = element(default=None)


class FiberExponentialLinearUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="uncoupled fiber-exp-linear", frozen=True)
    c3: MatNonNegativeFloat = element(default=MaterialParameter(text=0.0))
    c4: MatPositiveFloat = element(default=MaterialParameter(text=43.0))
    c5: MatPositiveFloat = element(default=MaterialParameter(text=3.0))
    lam0: MatGTOneFloat = element(default=MaterialParameter(text=1.05), tag="lambda")
    fiber: Optional[FiberVector] = element(default=None)


class FiberEntropyChainUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: str = attr(default="uncoupled fiber-entropy-chain", frozen=True)
    ksi: MatPositiveFloat = element(default=MaterialParameter(text=1.0))
    N: MatGTOneFloat = element(default=MaterialParameter(text=2.0))
    n_term: MatPositiveInt = element(default=MaterialParameter(text=2))
    fiber: Optional[FiberVector] = element(default=None)


FiberModelUC: TypeAlias = Union[
    FiberToeLinearUC,
    FiberKiousisUC,
    FiberExponentialPowerUC,
    FiberExponentialLinearUC,
    FiberEntropyChainUC,
]


# Continuous Fiber Distribution Functions
class CFDSpherical(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["spherical"] = attr(default="spherical", frozen=True)


class CFDEllipsoidal(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["ellipsoidal"] = attr(default="ellipsoidal", frozen=True)
    spa: MatStringFloatVec3 = element(default=MaterialParameter(text="1.0,1.0,1.0"))


class CFDVonMises3d(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["von-Mises-3d"] = attr(default="von-Mises-3d")
    b: MatNonNegativeFloat = element(default=MaterialParameter(text=0.5))


class CFDCircular(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["circular"] = attr(default="circular")


class CFDElliptical(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["elliptical"] = attr(default="elliptical", frozen=True)
    spa1: MatNonNegativeFloat = element(default=MaterialParameter(text=1.0))
    spa2: MatNonNegativeFloat = element(default=MaterialParameter(text=1.0))


class CFDVonMises2d(BaseXmlModel, tag="distribution", extra="forbid"):
    type: Literal["von-Mises-2d"] = attr(default="von-Mises-2d")
    b: MatNonNegativeFloat = element(default=MaterialParameter(text=0.5))


CFDistributionModel: TypeAlias = Union[CFDCircular, CFDSpherical, CFDVonMises3d, CFDVonMises2d, CFDEllipsoidal]


# Continous Fiber Distribution Function Integration Schema
class GaussKronrodTrapezoidalIntegration(BaseXmlModel, tag="scheme", extra="forbid"):
    type: Literal["fibers-3d-gkt"] = attr(default="fibers-3d-gkt", frozen=True)
    nph: Literal[7, 11, 15, 19, 23, 27] = element(default=7)
    nth: PositiveInt = element(default=31)


class FiniteElementIntegration(BaseXmlModel, tag="scheme", extra="forbid"):
    type: Literal["fibers-3d-fei"] = attr(default="fibers-3d-fei", frozen=True)
    resolution: Literal[
        20,
        34,
        60,
        74,
        196,
        210,
        396,
        410,
        596,
        610,
        796,
        810,
        996,
        1010,
        1196,
        1210,
        1396,
        1410,
        1596,
        1610,
        1796,
    ] = element(default=1610)


class TrapezoidalRuleIntegration(BaseXmlModel, tag="scheme", extra="forbid"):
    type: Literal["fibers-2d-trapezoidal"] = attr(default="fibers-2d-trapezoidal", frozen=True)
    nth: PositiveInt = element(default=31)


IntegrationScheme: TypeAlias = Union[GaussKronrodTrapezoidalIntegration, FiniteElementIntegration, TrapezoidalRuleIntegration]


class ContinuousFiberDistribution(BaseXmlModel, tag="solid", extra="forbid"):
    type: Literal["continuous fiber distribution"] = attr(default="continuous fiber distribution", frozen=True)
    fibers: FiberModel = element(default=FiberNaturalNeoHookean(), tag="fibers")
    distribution: CFDistributionModel = element(default=CFDSpherical())
    scheme: IntegrationScheme = element(default=GaussKronrodTrapezoidalIntegration())
    mat_axis: Optional[MaterialAxisVector] = element(default=None)


class ContinuousFiberDistributionUC(BaseXmlModel, tag="solid", extra="forbid"):
    type: Literal["continuous fiber distribution uncoupled"] = attr(
        default="continuous fiber distribution uncoupled", frozen=True
    )
    fibers: FiberModelUC = element(default=FiberToeLinearUC(), tag="fibers")
    distribution: CFDistributionModel = element(default=CFDSpherical())
    scheme: IntegrationScheme = element(default=GaussKronrodTrapezoidalIntegration())
    mat_axis: Optional[MaterialAxisVector] = element(default=None)


# Solid Mixture
class SolidMixture(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="solid mixture")
    type: Literal["solid mixture"] = attr(default="solid mixture", frozen=True)
    id: int = attr(ge=1)
    solid_list: list[UnconstrainedMaterials | FiberModel | ContinuousFiberDistribution | EvolvingUnconstrainedMaterials] = (
        element(tag="solid", default=[])
    )

    def add_solid(
        self, new_solid: UnconstrainedMaterials | FiberModel | ContinuousFiberDistribution | EvolvingUnconstrainedMaterials
    ):
        self.solid_list.append(new_solid)


# Uncoupled Solid Mixture
class SolidMixtureUC(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="solid mixture")
    type: Literal["solid mixture"] = attr(default="uncoupled solid mixture", frozen=True)
    id: int = attr(ge=1)
    solid_list: list[UncoupledMaterials | FiberModelUC | ContinuousFiberDistributionUC] = element(tag="solid", default=[])

    def add_solid(self, new_solid: UncoupledMaterials | FiberModelUC | ContinuousFiberDistributionUC):
        self.solid_list.append(new_solid)


# Prestrain
class InSituStretch(BaseXmlModel, tag="stretch", extra="forbid"):
    lc: int = attr(ge=1)
    type: Optional[Literal["map", "math"]] = attr(default=None)
    text: str | float


class PrestrainInSituStretch(BaseXmlModel, tag="prestrain", extra="forbid"):
    type: Literal["in-situ stretch"] = attr(default="in-situ stretch", frozen=True)
    stretch: InSituStretch = element()
    ischoric: Literal[0, 1] = element(default=1)


class PrestrainRamp(BaseXmlModel, tag="ramp", extra="forbid"):
    lc: int = attr(ge=1)
    text: float = 1.0


class PrestrainGradient(BaseXmlModel, tag="prestrain", extra="forbid"):
    type: Literal["prestrain gradient"] = attr(default="prestrain gradient", frozen=True)
    ramp: PrestrainRamp = element()
    F0: MatStringFloatVec9 = element(default=MaterialParameter(text="1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0"))


class PrestrainElastic(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="prestrain elastic")
    type: Literal["prestrain elastic"] = attr(default="prestrain elastic", frozen=True)
    id: int = attr(ge=1)
    elastic: UnconstrainedMaterials | SolidMixture = element(default=TransIsoMooneyRivlin(id=1))
    prestrain: PrestrainInSituStretch | PrestrainGradient = element()


class PrestrainElasticUC(BaseXmlModel, tag="material", extra="forbid"):
    name: str = attr(default="prestrain elastic")
    type: Literal["prestrain elastic"] = attr(default="prestrain elastic", frozen=True)
    id: int = attr(ge=1)
    elastic: UncoupledMaterials | SolidMixtureUC = element(default=TransIsoMooneyRivlin(id=1))
    prestrain: PrestrainInSituStretch | PrestrainGradient = element()


def tension_only_nonlinear_spring(slack: float, e0: float, k: float) -> str:
    """
    Blankevoort 1991 ligament model

    :param slack: engineering strain representing amount of slack (will not produce force until slack strain is reached)
    :param e0: engineering strain where fibers are fully straigtened (start of linear region)
    :param k: elastic modulus of linear region

    :return: A string expression of fiber force equation compatible with FEBio math interpreter
    """

    toe_region = f"H(x - {slack:.5f}) * ({0.5 / e0 * k:.5f} * (x - {slack:.5f}) ^ 2) * (1.0 - H(x -{slack + e0:.5f}))"
    linear_region = f"H(x - {slack + e0:.5f}) * {k:.5f} * (x - {slack} - {e0 / 2.0:.5f})"

    return " + ".join([toe_region, linear_region])


MaterialType = Union[UnconstrainedMaterials, EvolvingUnconstrainedMaterials, UncoupledMaterials, RigidBody, SolidMixture]


class Material(BaseXmlModel, validate_assignment=True):
    all_materials: List[MaterialType] = element(tag="material", default=[])

    def add_material(self, material: MaterialType):
        material.id = len(self.all_materials) + 1
        self.all_materials.append(material)
