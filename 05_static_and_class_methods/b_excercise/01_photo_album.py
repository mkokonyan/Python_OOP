from math import ceil

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for r in range(len(self.photos)):
            if 0 <= len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page" \
                       f" {r+1} slot {self.photos[r].index(label)+1}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for i in range(self.pages):
            result += (f"{'[] ' * len(self.photos[i])}").rstrip()
            result += "\n-----------\n"
        return result.strip()

album = PhotoAlbum.from_photos_count(5)

print(album.photos)
print(album.display())
