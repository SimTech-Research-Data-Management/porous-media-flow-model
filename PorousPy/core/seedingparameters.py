import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SeedingParameters(sdRDM.DataModel):
    """The Seeding Parameters contains crucial information about the seeding material used in the experiment.
    It includes details such as the material name, particle type, density, particle size and the kinematic viscosity of the seeding particles.
    These parameters provide valuable insights into the characteristics of the seeding material and its influence on the fluid flow behavior within the experimental setup.
    """

    id: Optional[str] = Field(
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
        default=None,
        description="Value of the seeding particle kinematic viscosity in m^2/s",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
