import os
import sys


def resolve_root():
    root_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)))
    sys.path.append(root_path)


if __name__ == '__main__':
    resolve_root()
