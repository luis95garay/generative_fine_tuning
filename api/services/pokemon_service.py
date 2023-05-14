import io
from typing import Optional
from PIL import Image

from exceptions.pokemon import (NotProcessingException,
                                          StillProcessingException)
from .model import PokemonPipeline

PROCESSING = {}
RESULT: dict[str, Image.Image] = {}


class PokemonService:
    @staticmethod
    def make_pokemon(
        prompt: str,
        scale: float,
        key: tuple,
        uuid: str,
    ):
        pipe = PokemonPipeline()
        PROCESSING[key] = uuid
        RESULT[uuid] = Image.fromarray(pipe(prompt, scale))

    @staticmethod
    def is_processing(key: tuple) -> Optional[str]:
        return PROCESSING.get(key)

    @staticmethod
    def get_image_BytesIO(pid: str) -> io.BytesIO:

        if pid not in PROCESSING.values():
            raise NotProcessingException()
        output = io.BytesIO()
        try:
            RESULT[pid].save(output, format='JPEG')
        except KeyError:
            raise StillProcessingException()
        output.seek(0)
        return output
