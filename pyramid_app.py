from pyramid.config import Configurator
from pyramid.response import Response


def root(request):
    return Response(
        """
                    <body><h1>
                        Hello, World!
                    </h1></body>
                    """
    )


config = Configurator()

config.add_route("hello", "/")
config.add_view(root, route_name="hello")
app = config.make_wsgi_app()
