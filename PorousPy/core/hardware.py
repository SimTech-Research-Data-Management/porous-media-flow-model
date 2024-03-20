import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .triggering import Triggering
from .device import Device
from .laser import Laser
from .camera import Camera
from .seedingparameters import SeedingParameters
from .seeding import Seeding


@forge_signature
class Hardware(sdRDM.DataModel, search_mode="unordered"):
    """*The Hardware includes descriptions of the camera systems, laser systems, seeding devices and materials, optical devices, and triggering systems utilized during the experiment.*"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    camera: List[Camera] = element(
        description="Description of the used camera system.",
        default_factory=ListPlus,
        tag="camera",
        json_schema_extra=dict(multiple=True),
    )

    laser: List[Laser] = element(
        description="Description of the used laser system.",
        default_factory=ListPlus,
        tag="laser",
        json_schema_extra=dict(multiple=True),
    )

    seeding: List[Seeding] = element(
        description="Description of the used seeding device and seeding material.",
        default_factory=ListPlus,
        tag="seeding",
        json_schema_extra=dict(multiple=True),
    )

    optics: List[Device] = element(
        description=(
            "Description of the used optical devices (e.g. laserarms, lenses,"
            " beamsplitter, sheet optics, ...)."
        ),
        default_factory=ListPlus,
        tag="optics",
        json_schema_extra=dict(multiple=True),
    )

    triggering: List[Triggering] = element(
        description="Description of the used triggering devices.",
        default_factory=ListPlus,
        tag="triggering",
        json_schema_extra=dict(multiple=True),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="07eea00104b98a757878bf718d0cd3baf4ea52d5"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self

    def add_to_camera(
        self,
        manufacturer: str,
        lens: Optional[str] = None,
        sensor: Optional[str] = None,
        model: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Camera:
        """
        This method adds an object of type 'Camera' to attribute camera

        Args:
            id (str): Unique identifier of the 'Camera' object. Defaults to 'None'.
            manufacturer (): Name of the device's manufacturer..
            lens (): Name of the camera lens which were used.. Defaults to None
            sensor (): Description of the camera sensor which were used.. Defaults to None
            model (): Name of the device's model.. Defaults to None
        """
        params = {
            "manufacturer": manufacturer,
            "lens": lens,
            "sensor": sensor,
            "model": model,
        }
        if id is not None:
            params["id"] = id
        self.camera.append(Camera(**params))
        return self.camera[-1]

    def add_to_laser(
        self,
        wavelength: float,
        manufacturer: str,
        type: Optional[str] = None,
        power: Optional[float] = None,
        model: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Laser:
        """
        This method adds an object of type 'Laser' to attribute laser

        Args:
            id (str): Unique identifier of the 'Laser' object. Defaults to 'None'.
            wavelength (): Value of the used wavelength of the laser. \\[nm].
            manufacturer (): Name of the device's manufacturer..
            type (): Type of the used laser (e.g. pulsed or continuous wave laser, ...). Defaults to None
            power (): Value of the laser power. \\[W]. Defaults to None
            model (): Name of the device's model.. Defaults to None
        """
        params = {
            "wavelength": wavelength,
            "manufacturer": manufacturer,
            "type": type,
            "power": power,
            "model": model,
        }
        if id is not None:
            params["id"] = id
        self.laser.append(Laser(**params))
        return self.laser[-1]

    def add_to_seeding(
        self,
        particles: SeedingParameters,
        manufacturer: str,
        model: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Seeding:
        """
        This method adds an object of type 'Seeding' to attribute seeding

        Args:
            id (str): Unique identifier of the 'Seeding' object. Defaults to 'None'.
            particles (): Seeding parameters of the used seeding material during the experiment..
            manufacturer (): Name of the device's manufacturer..
            model (): Name of the device's model.. Defaults to None
        """
        params = {"particles": particles, "manufacturer": manufacturer, "model": model}
        if id is not None:
            params["id"] = id
        self.seeding.append(Seeding(**params))
        return self.seeding[-1]

    def add_to_optics(
        self, manufacturer: str, model: Optional[str] = None, id: Optional[str] = None
    ) -> Device:
        """
        This method adds an object of type 'Device' to attribute optics

        Args:
            id (str): Unique identifier of the 'Device' object. Defaults to 'None'.
            manufacturer (): Name of the device's manufacturer..
            model (): Name of the device's model.. Defaults to None
        """
        params = {"manufacturer": manufacturer, "model": model}
        if id is not None:
            params["id"] = id
        self.optics.append(Device(**params))
        return self.optics[-1]

    def add_to_triggering(
        self,
        recording_mode: str,
        manufacturer: str,
        model: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Triggering:
        """
        This method adds an object of type 'Triggering' to attribute triggering

        Args:
            id (str): Unique identifier of the 'Triggering' object. Defaults to 'None'.
            recording_mode (): Type of recording mode during the experiment (e.g. time-based, cyclic time-based, ...)..
            manufacturer (): Name of the device's manufacturer..
            model (): Name of the device's model.. Defaults to None
        """
        params = {
            "recording_mode": recording_mode,
            "manufacturer": manufacturer,
            "model": model,
        }
        if id is not None:
            params["id"] = id
        self.triggering.append(Triggering(**params))
        return self.triggering[-1]
