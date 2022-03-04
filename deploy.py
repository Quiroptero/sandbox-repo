import time
import os
import fire



class Main:

    def __init__(self):
        self.start = time.time()

    def display_env(self, name: str):
        print(os.environ.get(name))


if __name__ == "__main__":
    fire.Fire(Main())

