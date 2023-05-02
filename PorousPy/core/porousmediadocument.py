import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime

from .seeding import Seeding
from .author import Author
from .camera import Camera
from .measurement import Measurement
from .freeflow import FreeFlow
from .recording import Recording
from .laser import Laser
from .triggering import Triggering
from .model import Model
from .device import Device
from .hardware import Hardware
from .processstep import ProcessStep


@forge_signature
class PorousMediaDocument(sdRDM.DataModel):

    """This is a container for general information about the dataset. Please describe your dataset in detail here."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("porousmediadocumentINDEX"),
        xml="@id",
    )

    grant_information: str = Field(
        ...,
        description="Hello",
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
        multiple=True,
        description="Persons who worked on the dataset",
        default_factory=ListPlus,
    )

    subjects: List[str] = Field(
        multiple=True,
        description="Research subjects covered by the dataset",
        default_factory=ListPlus,
    )

    model: Optional[Model] = Field(
        default=None,
        description="Porous media model investigated in this dataset",
    )

    keywords: List[str] = Field(
        multiple=True,
        description=(
            "Descriptive keywords to describe the datase (examples:PIV, time-resolved,"
            " time-averaged)"
        ),
        default_factory=ListPlus,
    )

    devices: List[Hardware] = Field(
        description="Devices used in this experiment",
        multiple=True,
        default_factory=ListPlus,
    )

    free_flow: Optional[FreeFlow] = Field(
        default=None,
        description="Free flow of the measurement",
    )

    measurements: List[Measurement] = Field(
        description="Contains all measurements done in this experiment",
        default_factory=ListPlus,
        multiple=True,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="217170c9b861fd33ddc40de1715b3fedae23bbe6"
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
        This method adds an object of type 'Author' to attribute authors

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name of the author.
            affiliation (): Organisation the author is affiliated with.
            email (): Contact e-mail adress of the author.
            phone (): Contact phone number of the author. Defaults to None
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

    def add_to_devices(
        self,
        seeding: Seeding,
        camera: List[Camera] = ListPlus(),
        laser: List[Laser] = ListPlus(),
        optics: List[Device] = ListPlus(),
        triggering: Optional[Triggering] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Hardware' to attribute devices

        Args:
            id (str): Unique identifier of the 'Hardware' object. Defaults to 'None'.
            seeding (): Description of the used seeding device and seeding material.
            camera (): Description of the used camera system. Defaults to ListPlus()
            laser (): Description of the used laser system. Defaults to ListPlus()
            optics (): Description of the used optical devices (laserarm, lenses, beamsplitter, sheet optics, ...). Defaults to ListPlus()
            triggering (): Description of the used triggering devices. Defaults to None
        """

        params = {
            "seeding": seeding,
            "camera": camera,
            "laser": laser,
            "optics": optics,
            "triggering": triggering,
        }

        if id is not None:
            params["id"] = id

        self.devices.append(Hardware(**params))

    def add_to_measurements(
        self,
        name: str,
        recordings: List[Recording] = ListPlus(),
        processing_steps: List[ProcessStep] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Measurement' to attribute measurements

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            name (): Name of the experiment.
            recordings (): Recordings that have been done in the course of the experiment. Defaults to ListPlus()
            processing_steps (): Processed video data of the flow measurement. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "recordings": recordings,
            "processing_steps": processing_steps,
        }

        if id is not None:
            params["id"] = id

        self.measurements.append(Measurement(**params))
