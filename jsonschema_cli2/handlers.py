import os
import pathlib

from jsonschema_cli2.load import load_file


def handle_file_uri(schema_path: pathlib.Path):
    def resolver(uri: str):
        if os.path.isdir(schema_path):
            path_to_ref_schema = schema_path

        if os.path.isfile(schema_path):
            path_to_ref_schema = schema_path.parent

        file_path = pathlib.Path(path_to_ref_schema).joinpath(pathlib.Path(uri)).absolute()

        return load_file(str(file_path))

    return resolver
