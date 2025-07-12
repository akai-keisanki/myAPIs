import flask
import sys

class App (object):

    _app : flask.Flask

    def __init__ (self) -> None:

        self._app = flask.Flask(__name__);

    def set_routes (self) -> None:
        """
        App route setter
        """

        @self._app.route('/')
        def root () -> None:

            return 'The app is running.'

    def start_apis (self) -> None:

        ...
    
    def main (self) -> None:
        """
        App main function.

        Executes `set_routes`, `start_apis` and runs the application.
        """

        self.set_routes()

        self.start_apis()
        
        self._app.run(debug = sys.argv[-1] == 'debug')


if __name__ == '__main__': App().main()
