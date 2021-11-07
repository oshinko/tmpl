import argparse
import pathlib
import re

from . import __name__ as MODULE_NAME

pacakge_data_dir = pathlib.Path(__file__).parent / 'data'


def istext(data):
    # ref: https://stackoverflow.com/a/7392391
    TEXT_CHARS = \
        bytes({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
    if isinstance(data, str):
        data = data.encode('utf8')
    return not bool(data.translate(None, TEXT_CHARS))


def create(ctx):
    ctx.output_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(pacakge_data_dir.glob('**/*')):
        dist = ctx.output_dir / path.relative_to(pacakge_data_dir)
        if path.is_dir():
            dist.mkdir(parents=True, exist_ok=True)
            continue
        data = path.read_bytes()
        if istext(data):
            for k, v in vars(ctx).items():
                var = k.encode('utf8')
                val = str(v).encode('utf8')
                pattern = br'\(\$\s+VAR+\s+\$\)'.replace(b'VAR', var)
                data = re.sub(pattern, val, data)
        dist.write_bytes(data)


parser = argparse.ArgumentParser('python -m ' + MODULE_NAME)
subparsers = parser.add_subparsers(dest='method', required=True)
subparser = subparsers.add_parser('create')
subparser.add_argument('--title', default='Your App')
subparser.add_argument('output_dir', metavar='output-dir', nargs='?',
                       type=pathlib.Path, default='.')
subparser.set_defaults(action=create)
args = parser.parse_args()
args.action(args)
