from pathlib import Path

class Site:
    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dst = Path(dest)