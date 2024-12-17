class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()

    def how_many(self, people):
        new_listeners = set(person.lower() for person in people) - self.listeners
        self.listeners.update(new_listeners)
        return len(new_listeners)
