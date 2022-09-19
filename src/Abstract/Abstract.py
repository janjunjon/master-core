import os

class Abstract:
    def __init__(self) -> None:
        self.root_path = os.path.abspath('../')
        self.localdir = os.path.abspath('../../')