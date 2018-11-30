#!/usr/bin/python
# -*- coding: utf-8 -*-
from thumbor.context import ServerParameters
from thumbor.server import *

def main(argv):
    start_thumbor()

def start_thumbor():
    """
    Runs thumbor server with the specified arguments.
    """
    try:
        server_parameters = ServerParameters(
            port=8888,
            ip='0.0.0.0',
            config_path=None,
            keyfile=False,
            log_level=log_level,
            app_class='thumbor.app.ThumborServiceApp',
            use_environment=True)
        global config
        # SO-SIH-167 - 08/08/2018 - Allowing environment variable
        # Passing environment variable flag to server parameters
        config = get_config(thumbor_config_path, server_parameters.use_environment)
        configure_log(config, server_parameters.log_level)
        importer = get_importer(config)
        os.environ["PATH"] += os.pathsep + '/var/task'
        validate_config(config, server_parameters)
        with get_context(server_parameters, config, importer) as thumbor_context:
            application = get_application(thumbor_context)
            run_server(application, thumbor_context)
            tornado.ioloop.IOLoop.instance().start()
            logging.info(
                        'thumbor running at %s:%d' %
                        (thumbor_context.server.ip, thumbor_context.server.port)
                        )
            return config
    except RuntimeError as error:
        if str(error) != "IOLoop is already running":
            logging.error('start_thumbor RuntimeError: %s' % (error))
            stop_thumbor()
    except Exception as error:
        stop_thumbor()
        logging.error('start_thumbor error: %s' % (error))
        logging.error('start_thumbor trace: %s' % traceback.format_exc())

def start_server():
    t = threading.Thread(target=start_thumbor)
    t.daemon = True
    t.start()
    return t



if __name__ == "__main__":
   main(sys.argv[1:])

