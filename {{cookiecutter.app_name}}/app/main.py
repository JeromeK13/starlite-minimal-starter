from starlite import Starlite, get


@get(path="/healthcheck")
def health_check() -> str:
    return "healthy"


app = Starlite(
    route_handlers=[health_check],
    openapi_config=OpenAPIConfig(
        title="{{cookiecutter.app_name}}",
        version="{{cookiecutter.version}}",
        description="{{cookiecutter.description}}",
        license="{{cookiecutter.license}}",
    ),
)
