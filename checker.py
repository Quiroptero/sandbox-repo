import os
import json
from pathlib import Path

try:
    import fire
except ImportError:
    os.system(f"pip install fire")
    import fire

def read_file(filepath) -> str:
    with open(filepath, "r") as file:
        return file.read()


class Main:

    def __init__(self):
        pass


    @classmethod
    def json_checker(
            cls,
            filepath: str,
            at_least_one: bool = False,
    ):
        if os.path.isdir(filepath):
            reduce = any if at_least_one else all
            return reduce([
                cls.json_checker(
                    filepath=str(file),
                )
                for file in [f for f in sorted(Path(filepath).glob("**/*")) if f.is_file()]
            ])
        content = read_file(filepath=filepath)
        try:
            obj = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"[JSON Specification Check Failed] File: {filepath}. Cause of error: {e}")
            raise e
        return True


if __name__ == "__main__":
    main = Main()
    fire.Fire(main)
