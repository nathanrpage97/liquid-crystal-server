import aiohttp_cors
from aiohttp.web import Application, run_app

from liquid_crystal_server.routes import routes
app = Application()

# allow all cross origin sources to access the server
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
        allow_methods='*'
    )
})
app.add_routes(routes)
for route in list(app.router.routes()):
    cors.add(route)


def start_server(host: str = '0.0.0.0', port: int = 80):
    run_app(app, host=host, port=port, handle_signals=False)
