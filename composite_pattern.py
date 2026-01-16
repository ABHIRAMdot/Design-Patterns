# composite pattern
class FileSystemItem:
    def show(self):
        pass

class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("File:", self.name)

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print("Folder:", self.name)
        for item in self.items:
            item.show()

    
file1 = File("a.txt")
file2 = File("b.txt")

subfolder = Folder("Photos")
subfolder.add(File("pic1.jpg"))
subfolder.add(File("pic2.jpg"))

main_folder = Folder("Documents")
main_folder.add(file1)
main_folder.add(file2)
main_folder.add(subfolder)

main_folder.show()
