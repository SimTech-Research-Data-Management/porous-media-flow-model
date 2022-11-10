import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .camera import Camera
from .device import Device
from .laser import Laser
from .seeding import Seeding
from .triggering import Triggering


@forge_signature
class Hardware(sdRDM.DataModel):

    """This is a container for general information about the hardware which was used to capture the PIV data.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("hardwareINDEX"),
        xml="@id",
    )
    optics: List[Device] = Field(
        description=(
            "Description of the used optical devices (laserarm, lenses, beamsplitter,"
            " sheet optics, ...)"
        ),
        default_factory=ListPlus,
    )

    camera: List[Camera] = Field(
        description="Description of the used camera system",
        default_factory=ListPlus,
    )

    laser: List[Laser] = Field(
        description="Description of the used laser system",
        default_factory=ListPlus,
    )

    seeding: Seeding = Field(
        description="Description of the used seeding device and seeding material",
        default=None,
    )

    triggering: Optional[Triggering] = Field(
        description="Description of the used triggering devices",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="53d30eba563d0bc6bcf3db15575fa61d02387eb0"
    )

    def add_to_camera(
        self,
        manufacturer: str,
        model: str,
        lens: Optional[str] = None,
        sensor: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Camera' to the attribute 'camera'.

        Args:
            id (str): Unique identifier of the 'Camera' object. Defaults to 'None'.
            manufacturer (str): Name of the device's manufacturer.
            model (str): Name of the device's model.
            lens (Optional[str]): Name of the camera lens. Defaults to None
            sensor (Optional[str]): Description of the camera sensor. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "model": model,
            "lens": lens,
            "sensor": sensor,
        }

        if id is not None:
            params["id"] = id

        camera = [Camera(**params)]

        self.camera = self.camera + camera

    def add_to_laser(
        self,
        manufacturer: str,
        model: str,
        wavelength: float,
        type: Optional[str] = None,
        power: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Laser' to the attribute 'laser'.

        Args:
            id (str): Unique identifier of the 'Laser' object. Defaults to 'None'.
            manufacturer (str): Name of the device's manufacturer.
            model (str): Name of the device's model.
            wavelength (float): Value of the used wavelength.
            type (Optional[str]): Pulsed or continous wave laser?. Defaults to None
            power (Optional[float]): value of the laser power. Defaults to None
        """

        params = {
            "manufacturer": manufacturer,
            "model": model,
            "wavelength": wavelength,
            "type": type,
            "power": power,
        }

        if id is not None:
            params["id"] = id

        laser = [Laser(**params)]

        self.laser = self.laser + laser

    def add_to_optics(
        self, manufacturer: str, model: str, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Device' to the attribute 'optics'.

        Args:
            id (str): Unique identifier of the 'Device' object. Defaults to 'None'.
            manufacturer (str): Name of the device's manufacturer.
            model (str): Name of the device's model.
        """

        params = {
            "manufacturer": manufacturer,
            "model": model,
        }

        if id is not None:
            params["id"] = id

        optics = [Device(**params)]

        self.optics = self.optics + optics
