from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class DisplayMessage(DataClassJsonMixin):
    row: int
    col: int
    text: str
