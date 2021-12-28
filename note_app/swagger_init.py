from flasgger import Swagger

def set_up_swagger(app):
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['specs'] = [{
        "endpoint": 'apispec_server',
        "route": "/apispec_1.json",
        "route_filter": lambda rule: True,
        "model_filter": lambda tag: True
    }] + swagger_config["specs"]
    swagger_config['swagger_ui_bundle_js'] = "/flasgger_static/swagger-ui-bundle.js"
    swagger_config['swagger_ui_standalone_preset_js'] = "/flasgger_static/swagger-ui-standalone-preset.js"
    swagger_config['jquery_js'] = "/flasgger_static/lib/jquery.min.js"
    swagger_config['swagger_ui_css'] = "/flasgger_static/swagger-ui.css"
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "my-note-app",
            "version": "1"
        },
        "basePath": "/my_note_space"
    }
    Swagger(app, template=swagger_template, config=swagger_config, parse=True)