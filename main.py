from src.__init__ import create_app
from src.support.config import Config
from waitress import serve

app = create_app()
config = Config()

if __name__ == '__main__':
    host = config.HOST
    port = config.PORT
    debug = config.DEBUG

    if config.DEBUG:
        # run application in debug mode
        app.run(
            host=host, debug=debug, port=port, use_reloader=debug
        )
    else:
        # run application in production
        serve(app, host=config.HOST, port=config.PORT)
