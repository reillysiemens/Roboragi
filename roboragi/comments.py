from enum import Enum, auto
from typing import Generator


class Tag(Enum):
    ANIME = auto()
    MANGA = auto()
    LIGHT_NOVEL = auto()
    VISUAL_NOVEL = auto()


class Request:
    def __init__(self, tag: Tag, body: str, expanded: bool = False) -> None:
        self.tag = tag
        self.body = body
        self.expanded = expanded


def parse(comment: str) -> Generator[Request, None, None]:
    return []
