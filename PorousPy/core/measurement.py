import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from pydantic import validator
from typing import List
from typing import Optional
from typing import Union

from .processstep import ProcessStep
from .recording import Recording
from .software import Software
from .video import Video


@forge_signature
class Measurement(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Name of the experiment",
    )

    recording: Optional[Recording] = Field(
        description="Recordings that have been done in the course of the experiment",
        default=None,
    )

    model: Union[str, "Model", None] = Field(
        description="ID of the model that has been used",
        default=None,
    )

    raw_video: Optional[Video] = Field(
        description="Raw video data of the flow measurement",
        default=None,
    )

    processing_steps: List[ProcessStep] = Field(
        description="Processed video data of the flow measurement",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    def add_to_processing_steps(
        self,
        name: str,
        processed_video: Video,
        software: Software,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ProcessStep' to the attribute 'processing_steps'.

        Args:
            id (str): Unique identifier of the 'ProcessStep' object. Defaults to 'None'.
            name (str): Name of the processing step.
            processed_video (Video): Resulting video from the processing.
            software (Software): Software that has been used to perform the processing step.
        """

        params = {
            "name": name,
            "processed_video": processed_video,
            "software": software,
        }

        if id is not None:
            params["id"] = id

        processing_steps = [ProcessStep(**params)]

        self.processing_steps = self.processing_steps + processing_steps

    @validator("model", pre=True)
    def get_model_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .model import Model

        if not isinstance(value, (Model, str)):
            raise TypeError(
                f"Expected 'Model' or 'str' got '{type(value).__name__}' instead."
            )
        elif isinstance(value, Model):
            return value.id
        elif isinstance(value, str):
            return value
