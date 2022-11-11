import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime
from pydantic import Field
from typing import List
from typing import Optional

from .author import Author
from .camera import Camera
from .device import Device
from .freeflow import FreeFlow
from .hardware import Hardware
from .laser import Laser
from .measurement import Measurement
from .model import Model
from .processstep import ProcessStep
from .recording import Recording
from .seeding import Seeding
from .triggering import Triggering


@forge_signature
class Root(sdRDM.DataModel):

    """This is a container for general information about the dataset. Please describe your dataset in detail here.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("rootINDEX"),
        xml="@id",
    )
    description: str = Field(
        ...,
        description="Describes the content of the dataset",
    )

    name: str = Field(
        ...,
        description="Descriptive name of the dataset / ID",
    )

    date: datetime = Field(
        ...,
        description="Date/time when the dataset was created",
    )

    authors: List[Author] = Field(
        description="Persons who worked on the dataset",
        default_factory=ListPlus,
    )

    subjects: List[str] = Field(
        description="Research subjects covered by the dataset",
        default_factory=ListPlus,
    )

    model: Optional[Model] = Field(
        description="Porous media model investigated in this dataset",
        default=None,
    )

    keywords: List[str] = Field(
        description=(
            "Descriptive keywords to describe the datase (examples:PIV, time-resolved,"
            " time-averaged)"
        ),
        default_factory=ListPlus,
    )

    devices: List[Hardware] = Field(
        description="Devices used in this experiment",
        default_factory=ListPlus,
    )

    free_flow: Optional[FreeFlow] = Field(
        description="Free flow of the measurement",
        default=None,
    )

    measurements: List[Measurement] = Field(
        description="Contains all measurements done in this experiment",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )

    def add_to_authors(
        self,
        name: str,
        affiliation: str,
        email: str,
        phone: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (str): Full name of the author.
            affiliation (str): Organisation the author is affiliated with.
            email (str): Contact e-mail adress of the author.
            phone (Optional[int]): Contact phone number of the author. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
            "phone": phone,
        }

        if id is not None:
            params["id"] = id

        authors = [Author(**params)]

        self.authors = self.authors + authors

    def add_to_devices(
        self,
        camera: List[Camera],
        laser: List[Laser],
        seeding: Seeding,
        optics: List[Device],
        triggering: Optional[Triggering] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Hardware' to the attribute 'devices'.

        Args:
            id (str): Unique identifier of the 'Hardware' object. Defaults to 'None'.
            camera (List[Camera]): Description of the used camera system.
            laser (List[Laser]): Description of the used laser system.
            seeding (Seeding): Description of the used seeding device and seeding material.
            optics (List[Device]): Description of the used optical devices (laserarm, lenses, beamsplitter, sheet optics, ..).
            triggering (Optional[Triggering]): Description of the used triggering devices. Defaults to None
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

        devices = [Hardware(**params)]

        self.devices = self.devices + devices

    def add_to_measurements(
        self,
        name: str,
        recordings: List[Recording],
        processing_steps: List[ProcessStep],
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Measurement' to the attribute 'measurements'.

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            name (str): Name of the experiment.
            recordings (List[Recording]): Recordings that have been done in the course of the experiment.
            processing_steps (List[ProcessStep]): Processed video data of the flow measurement.
        """

        params = {
            "name": name,
            "recordings": recordings,
            "processing_steps": processing_steps,
        }

        if id is not None:
            params["id"] = id

        measurements = [Measurement(**params)]

        self.measurements = self.measurements + measurements
