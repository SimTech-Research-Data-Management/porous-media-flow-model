import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class FlowParameters(sdRDM.DataModel):
    """This is a container for information about the flow parameters."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("flowparametersINDEX"),
        xml="@id",
    )

    fluid: str = Field(
        ...,
        description="Name of the free flow fluid",
    )

    temperature: float = Field(
        ...,
        description="Value of the fluid temperature in K",
    )

    pressure: float = Field(
        ...,
        description="Value of the fluid pressure in bar",
    )

    density: float = Field(
        ...,
        description="Value of the fluid density in kg/m^3",
    )

    kinematic_viscosity: float = Field(
        ...,
        description="Value of the fluid kinematic viscosity in m^2/s",
    )

    dynamic_viscosity: float = Field(
        ...,
        description="Value of the dynamic fluid viscosity in mPas",
    )

    flow_velocity: float = Field(
        ...,
        description="Value of the fluid flow velocity in m/s",
    )

    mass_flux: float = Field(
        ...,
        description="Value of the fluid mass flux in kg/s",
    )

    reynolds_number: List[float] = Field(
        multiple=True,
        description="Value(s) of investigated Reynolds number(s)",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bcd0026275c43b975bd1ffb5d0a0a434786df0e4"
    )
