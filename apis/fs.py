"""
Filesystem API
"""

import flask

class FileSystemAPI (object):

    _app : flask.Flask
    _active_api_list : set[str]
    _root_path : str

    def __init__ (self, app : flask.Flask = flask.Flask(__name__), active_api_list : set[str] = {}, root_path = './filesystem_data') -> None:

        self._app = app
        self._active_api_list = active_api_list
        self._root_path = root_path

    def set_routes (self) -> None:

        @self._app.route('/fs')
        def fs () -> (str, int):
            
            return 'Filesystem API is running', 200

        @self._app.route('/fs/access/<path:item_path>', methods = ['GET', 'POST', 'PUT'])
        def fs_access (item_path : str) -> (str, int):

            if '..' in item_path: return '`..` is not allowed in path.', 400
            if not item_path: return 'No path given', 400

            item_path = self._root_path + '/' + item_path

            open_method : str = ''

            for method in ['r', 'w', 'a']:
                if method in flask.request.args: open_method = method + '+'

            if open_method == '': return 'No file operation specified.', 400
            
            try:

                with open(item_path, open_method, encoding = flask.request.args.get('encoding', 'utf-8')) as file:

                    code : int = 200
                
                    if 'w' in flask.request.args or 'a' in flask.request.args:
                        file.write(flask.request.data.decode())
                        code = 201

                    if 'r' in flask.request.args: return file.read(), code
                    else: return 'File operated sucessfully.', code

            except FileNotFoundError: return 'The file could not be found', 404

            except IOError: return 'The file could not be opened', 400

        self._active_api_list.append('fs')
