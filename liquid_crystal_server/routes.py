from typing import Dict

from aiohttp.web import Request, Response, RouteTableDef
from aiojobs.aiohttp import atomic
from liquid_crystal import LiquidCrystalDriver

from liquid_crystal_server.defs import DisplayMessage

routes = RouteTableDef()

lcd = LiquidCrystalDriver('/dev/i2c-1', 0x27)


@atomic
@routes.post('/api/v1/display')
async def display_text(request: Request) -> Response:
    try:
        message: Dict[str, any] = await request.json()
        display_message = DisplayMessage.from_dict(message)
        lcd.display_at_position(display_message.text, display_message.row, display_message.col)
        return Response(status=204)
    except Exception as error:
        return Response(status=400, text=f'Failed to display text: {error}')
