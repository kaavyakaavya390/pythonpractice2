class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename} in mode: {self.mode}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        if exc_type:
            print(f"An exception occurred: {exc_value}")
            return False


with FileManager("my_file.txt", "w") as f:
    f.write("Hello, Welcome!!!")

# with FileManager("another_file.txt", "r") as f:
#     content = f.read()
