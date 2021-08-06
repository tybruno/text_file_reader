from pathlib import Path
from typing import Union
from dataclasses import dataclass
from file_reader.file_readers import AbstractFileReader, FileReaderError


@dataclass
class TextFileReader(AbstractFileReader):
    def __call__(self, file: Union[str, Path]) -> str:
        path = Path(file)
        try:
            return path.read_text()
        except FileNotFoundError as error:
            raise FileReaderError from error
