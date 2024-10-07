from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, aftor,  page_count):
        self.title = title
        self.author = aftor
        self.page_count = page_count
        self.current_page = 0
        self.bookmark = None

    def get_info(self):
        return f"Title: {self.title}, Aftor: {self.aftor},  Pages: {self.page_count}"

    def read_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print(f"Reading page {self.current_page} of '{self.title}'")
        else:
            print(" finished the book")

    def bookmark_page(self):
        self.bookmark = self.current_page
        print(f"Bookmarked page {self.bookmark} of '{self.title}'")

    @abstractmethod
    def specific_method(self):
        pass


class EBook(Book):
    def __init__(self, title, aftor, page_count, file_size):
        super().__init__(title, aftor, page_count)
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}' of size {self.file_size} MB.")

    def specific_method(self):
        return f"EBook specific method for '{self.title}'"
class AudioBook(Book):
    def __init__(self, title, aftor,  page_count, duration):
        super().__init__(title, aftor, page_count)
        self.duration = duration

    def play(self):
        print(f"Playing audio of '{self.title}' for {self.duration} minutes.")

    def specific_method(self):
        return f"AudioBook specific method for '{self.title}'"

ebook = EBook("destinewin", "sobirov asadbek, "123456789", 5)
audiobook = AudioBook("mindsed", "donyor", "987654321", 180)

print(ebook.get_info())
ebook.download()
ebook.read_page()
ebook.bookmark_page()

print(audiobook.get_info())
audiobook.play()
audiobook.read_page()
audiobook.bookmark_page()