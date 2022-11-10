import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class SeedingParameters(sdRDM.DataModel):

    """This is a container for information regarding of the used seeding particles."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seedingparametersINDEX"),
        xml="@id",
    )
    material: str = Field(
        ...,
        description="Name of the seeding material",
    )

    type: str = Field(
        ...,
        description="Solid or liquid particles?",
    )

    density: float = Field(
        ...,
        description="Value of the seeding particle density in kg/m^3",
    )

    particle_size: float = Field(
        ...,
        description="Value or span of the seeding particle diameter in m",
    )

    kinematic_viscosity: Optional[float] = Field(
        description="Value of the seeding particle kinematic viscosity in m^2/s",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")
