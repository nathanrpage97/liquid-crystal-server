from aiohttp.web import Request, Response, RouteTableDef, json_response

from aiojobs.aiohttp import atomic


routes = RouteTableDef()


@atomic
@routes.get('/api/v1/')
async def display_text(request: Request) -> Response:
    try:
        body = 2
