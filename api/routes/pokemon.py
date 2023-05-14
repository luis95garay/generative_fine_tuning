import uuid

from fastapi import BackgroundTasks, Path
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter
import numpy as np

from responses.response import Responses
from services.pokemon_service import PokemonService

router = APIRouter(prefix='/make_pokemon', tags=['make pokemon'])


@router.post('/')
async def upload(
    bg_task: BackgroundTasks,
    prompt: str,
    scale: float
):
    key = prompt, scale
    if (_uuid := PokemonService.is_processing(key)):
        return Responses.accepted(_uuid)
    _uuid = str(uuid.uuid4())
    bg_task.add_task(
        PokemonService.make_pokemon, prompt, scale,
        key, _uuid)
    return Responses.created(_uuid)


@router.get("/{id}")
def result(id: str = Path(...)):
    output = PokemonService.get_image_BytesIO(id)
    return StreamingResponse(output, media_type='image/jpeg')
