
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device
from .seedingparameters import SeedingParameters


@forge_signature
class Seeding(Device):
    """The Seeding describes the material of the seeding particles, the type of them as well as their density, particle size, and kinematic viscosity."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seedingINDEX"),
        xml="@id",
    )

    particles: SeedingParameters = Field(
        ...,
        description="Seeding parameters of the used seeding material",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
