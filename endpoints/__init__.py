from sanic import Blueprint
import endpoints.v1.endpoints as v1


def add_blueprints(app):
    # TODO: automate looking up versions...
    print("added blueprints")
    blueprint_v1 = Blueprint("v1", url_prefix="/v1")
    blueprint_v1.add_route(v1.get_replays, "/<game>/replays", methods=["GET"])
    blueprint_v1.add_route(v1.get_replay, "/<game>/replay/<name>", methods=["GET"])
    blueprint_v1.add_route(v1.parse_replay, "/<game>/replay/parse", methods=["POST"])
    blueprint_v1.add_route(v1.accept_replay, "/<game>/replay/analyze", methods=["POST"])
    app.blueprint(blueprint_v1, url_prefix="/v1")


__all__ = [add_blueprints]
