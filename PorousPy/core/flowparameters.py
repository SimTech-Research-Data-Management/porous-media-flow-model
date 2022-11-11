import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List


@forge_signature
class FlowParameters(sdRDM.DataModel):

    """This is a container for information about the flow parameters."""

    id: str = Field(
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

    flow_velocity: float = Field(
        ...,
        description="Value of the fluid flow velocity in m/s",
    )

    mass_flux: float = Field(
        ...,
        description=" Value of the fluid mass flux in kg/s",
    )

    reynolds_number: List[float] = Field(
        description="Value(s) of investigated Reynolds number(s)",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )
