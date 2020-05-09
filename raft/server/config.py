import argparse
import os
import json


parser = argparse.ArgumentParser(description=('Zatt. An implementation of '
                                              'the Raft algorithm for '
                                              'distributed consensus'))
parser.add_argument('-c', '--config', dest='path_conf',
                    help='Config file path. Default: raft.persist/config')
parser.add_argument('-s', '--storage', help=('Path for the persistent state'
                    ' directory. Default: raft.persist'))
parser.add_argument('-a', '--address', help=('This node address. Default: '
                    '127.0.0.1'))
parser.add_argument('-p', '--port', help='This node port. Default: 5254',
                    type=int)
parser.add_argument('--remote-address', action='append', default=[],
                    help='Remote node address')
parser.add_argument('--remote-port', action='append', default=[], type=int,
                    help='Remote node port')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')


class Config:
    """Collect and merge CLI and file based config.
    This class is a singleton based on the Borg pattern."""
    __shared_state = {}

    def __new__(cls, *p, **k):
        if '_instance' not in cls.__dict__:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, config={}):
        if config is None:
            self.__dict__ = {}
        elif config:
            self.__dict__ = config
        else:
            self.__dict__ = self._get()

    def _get(self):
        default = {'debug': False, 'address': ['127.0.0.1', 5254],
                   'cluster': set(), 'storage': 'raft.persist'}

        environ = {k[5:].lower(): v for (k, v) in os.environ.items()
                   if k.startswith('ZATT_')}
        if {'address', 'port'}.issubset(environ):
            environ['address'] = (environ['address'], int(environ['port']))
            del environ['port']
        if {'remote_address', 'remote_port'}.issubset(environ):
            environ['cluster'] = {(a, int(p)) for (a, p) in
                                  zip(environ['remote_address'].split(','),
                                      environ['remote_port'].split(','))}
            del environ['remote_address']
            del environ['remote_port']

        config = default.copy()
        config.update(environ)

        cmdline = parser.parse_args().__dict__

        if 'path_conf' not in config:
            config['path_conf'] = os.path.join(config['storage'], 'conf')
        path_conf = cmdline['path_conf'] if cmdline['path_conf']\
            else config['path_conf']

        if os.path.isfile(path_conf):
            with open(path_conf, 'r') as f:
                config.update(json.loads(f.read()))

        config['cluster'] = {(a, int(p)) for (a, p) in config['cluster']}

        if cmdline['address']:
            config['address'][0] = cmdline['address']
        if cmdline['port']:
            config['address'][1] = cmdline['port']
        # cmdline['address'] = (cmdline['address'], cmdline['port'])\
            # if cmdline['address'] else None
        del cmdline['port']
        del cmdline['address']

        if cmdline['remote_address'] and cmdline['remote_port']:
            config['cluster'].add(*zip(cmdline['remote_address'],
                                       cmdline['remote_port']))
        del cmdline['remote_address']
        del cmdline['remote_port']

        for k, v in cmdline.items():
            if v is not None:
                config[k] = v

        config['address'] = tuple(config['address'])
        config['cluster'].add(config['address'])
        if type(config['debug']) is str:
            config['debug'] = True if config['debug'] == 'true' else False
        return config

config = Config(None)
