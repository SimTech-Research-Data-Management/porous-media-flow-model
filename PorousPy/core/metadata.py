import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from datetime import datetime as Datetime
from .processstep import ProcessStep
from .calibration import Calibration
from .measurement import Measurement
from .freeflow import FreeFlow
from .author import Author
from .device import Device
from .triggering import Triggering
from .camera import Camera
from .laser import Laser
from .model import Model
from .seeding import Seeding
from .hardware import Hardware
from .recording import Recording


@forge_signature
class Metadata(sdRDM.DataModel, search_mode="unordered"):
    """*The Metadata summarizes key information about the following dataset. It includes a description of the dataset's content, a descriptive name or ID of the dataset, and the date of creation. It also lists the contributors, highlights the research areas which are covered and specifies the specific porous media model investigated. Descriptive keywords help categorize the dataset and the the hardware used in the experiment is also stored. Free flow conditions of the turbulent air flow are also stored. The Metadata provides detailed information about the measurements conducted in the experiment.*"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    description: str = element(
        description=(
            "Summary of the content and background of the dataset described in 3-5"
            " sentences."
        ),
        tag="description",
        json_schema_extra=dict(),
    )

    ID: str = element(
        description="Descriptive name of the dataset or ID of the dataset.",
        tag="ID",
        json_schema_extra=dict(),
    )

    date: Datetime = element(
        description="Date & time when the dataset was created.",
        tag="date",
        json_schema_extra=dict(),
    )

    authors: List[Author] = element(
        description="Persons who worked on the dataset.",
        default_factory=ListPlus,
        tag="authors",
        json_schema_extra=dict(multiple=True),
    )

    subjects: List[str] = element(
        description="Research subjects covered by the dataset.",
        default_factory=ListPlus,
        tag="subjects",
        json_schema_extra=dict(multiple=True),
    )

    model: Optional[Model] = element(
        description="Define the actual model which was investigated with the dataset.",
        default=None,
        tag="model",
        json_schema_extra=dict(),
    )

    keywords: List[str] = element(
        description="Descriptive keywords to describe the dataset.",
        default_factory=ListPlus,
        tag="keywords",
        json_schema_extra=dict(multiple=True),
    )

    devices: List[Hardware] = element(
        description="Experimental devices used in the dataset.",
        default_factory=ListPlus,
        tag="devices",
        json_schema_extra=dict(multiple=True),
    )

    free_flow: Optional[FreeFlow] = element(
        description="Free flow conditions during the experiment",
        default=None,
        tag="free_flow",
        json_schema_extra=dict(),
    )

    measurements: List[Measurement] = element(
        description=(
            "Contains all measurements & recordings which were conducted during the"
            " experiment"
        ),
        default_factory=ListPlus,
        tag="measurements",
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

    def add_to_authors(
        self,
        name: str,
        affiliation: str,
        email: str,
        phone: Optional[int] = None,
        id: Optional[str] = None,
    ) -> Author:
        """
        This method adds an object of type 'Author' to attribute authors

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name of the author or the experimenter..
            affiliation (): Organisation to which the author belongs..
            email (): E-Mail adress of the author..
            phone (): Phone number of the author.. Defaults to None
        """
        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
            "phone": phone,
        }
        if id is not None:
            params["id"] = id
        self.authors.append(Author(**params))
        return self.authors[-1]

    def add_to_devices(
        self,
        camera: List[Camera] = ListPlus(),
        laser: List[Laser] = ListPlus(),
        seeding: List[Seeding] = ListPlus(),
        optics: List[Device] = ListPlus(),
        triggering: List[Triggering] = ListPlus(),
        id: Optional[str] = None,
    ) -> Hardware:
        """
        This method adds an object of type 'Hardware' to attribute devices

        Args:
            id (str): Unique identifier of the 'Hardware' object. Defaults to 'None'.
            camera (): Description of the used camera system.. Defaults to ListPlus()
            laser (): Description of the used laser system.. Defaults to ListPlus()
            seeding (): Description of the used seeding device and seeding material.. Defaults to ListPlus()
            optics (): Description of the used optical devices (e.g. laserarms, lenses, beamsplitter, sheet optics, ...).. Defaults to ListPlus()
            triggering (): Description of the used triggering devices.. Defaults to ListPlus()
        """
        params = {
            "camera": camera,
            "laser": laser,
            "seeding": seeding,
            "optics": optics,
            "triggering": triggering,
        }
        if id is not None:
            params["id"] = id
        self.devices.append(Hardware(**params))
        return self.devices[-1]

    def add_to_measurements(
        self,
        name: str,
        calibration: List[Calibration] = ListPlus(),
        recordings: List[Recording] = ListPlus(),
        processing_steps: List[ProcessStep] = ListPlus(),
        id: Optional[str] = None,
    ) -> Measurement:
        """
        This method adds an object of type 'Measurement' to attribute measurements

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            name (): Name of the experiment.It should contain all relevant information about the experiment..
            calibration (): Calibration that has been done before the actual experiment.. Defaults to ListPlus()
            recordings (): Recordings that have been done in the course of the experiment.. Defaults to ListPlus()
            processing_steps (): Processing steps and processed video data of the experiment. Defaults to ListPlus()
        """
        params = {
            "name": name,
            "calibration": calibration,
            "recordings": recordings,
            "processing_steps": processing_steps,
        }
        if id is not None:
            params["id"] = id
        self.measurements.append(Measurement(**params))
        return self.measurements[-1]
