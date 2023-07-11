import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .camera import Camera
from .seeding import Seeding
from .device import Device
from .triggering import Triggering
from .laser import Laser


@forge_signature
class Hardware(sdRDM.DataModel):

    """This is a container for general information about the hardware which was used to capture the PIV data."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("hardwareINDEX"),
        xml="@id",
    )

    camera: List[Camera] = Field(
        multiple=True,
        description="Description of the used camera system",
        default_factory=ListPlus,
    )

    laser: List[Laser] = Field(
        multiple=True,
        description="Description of the used laser system",
        default_factory=ListPlus,
    )

    seeding: Seeding = Field(
        ...,
        description="Description of the used seeding device and seeding material",
    )

    optics: List[Device] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Description of the used optical devices (laserarm, lenses, beamsplitter,"
            " sheet optics, ...)"
        ),
    )

    triggering: Optional[Triggering] = Field(
        default=None,
        description="Description of the used triggering devices",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7663b173df67fd6098a9e76ea7a354fcf151c549"
    )

    def add_to_camera(
        self,
        lens: Optional[str] = None,
        sensor: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Camera' to attribute camera

        Args:
            id (str): Unique identifier of the 'Camera' object. Defaults to 'None'.
            lens (): Name of the camera lens. Defaults to None
            sensor (): Description of the camera sensor. Defaults to None
        """

        params = {
            "lens": lens,
            "sensor": sensor,
        }

        if id is not None:
            params["id"] = id

        self.camera.append(Camera(**params))

    def add_to_laser(
        self,
        wavelength: float,
        type: Optional[str] = None,
        power: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Laser' to attribute laser

        Args:
            id (str): Unique identifier of the 'Laser' object. Defaults to 'None'.
            wavelength (): Value of the used wavelength.
            type (): Pulsed or continous wave laser?. Defaults to None
            power (): value of the laser power. Defaults to None
        """

        params = {
            "wavelength": wavelength,
            "type": type,
            "power": power,
        }

        if id is not None:
            params["id"] = id

        self.laser.append(Laser(**params))

    def add_to_optics(
        self, manufacturer: str, model: str, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Device' to attribute optics

        Args:
            id (str): Unique identifier of the 'Device' object. Defaults to 'None'.
            manufacturer (): Name of the device's manufacturer.
            model (): Name of the device's model.
        """

        params = {
            "manufacturer": manufacturer,
            "model": model,
        }

        if id is not None:
            params["id"] = id

        self.optics.append(Device(**params))
