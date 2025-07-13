"""
Application
"""

import flask
import sys
import functools

import apis

class App (object):

    _app : flask.Flask
    _active_apis : set[str]

    def __init__ (self) -> None:
        """
        App setup and class initializer.
        """

        self._app = flask.Flask(__name__, template_folder = 'templates', static_folder = 'static');
        _active_apis = []

    def set_routes (self) -> None:
        """
        App route setter
        """

        @self._app.route('/')
        def root () -> (str, int):

            return 'The app is running.' + functools.reduce(lambda a, b : a + b, self._active_apis), 200

    def set_apis (self) -> None:
        """
        API set setter
        """

        apis.fs.FileSystemAPI(self._app, self._active_apis).set_routes()
            
    def main (self) -> None:
        """
        App main function.

        Executes `set_routes`, `start_apis` and runs the application.
        """

        self.set_routes()

        self.set_apis()
        
        self._app.run(debug = sys.argv[-1] == 'debug')


if __name__ == '__main__': App().main()
