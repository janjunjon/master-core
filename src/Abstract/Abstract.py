from pathlib import Path

class Abstract:
    root = Path(__file__).resolve().parent.parent.parent
    parent = root.parent
    def __init__(self) -> None:
        self.root_path = self.__class__.root
        self.parent_path = self.__class__.parent