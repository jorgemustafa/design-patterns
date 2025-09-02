from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def update(self, subject, event):
        pass

class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self._subscribers = set()

    def subscribe(self, subscriber: YoutubeSubscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber: YoutubeSubscriber):
        self._subscribers.discard(subscriber)

    def notify(self, event):
        for sub in list(self._subscribers):
            try:
                sub.update(self, event)
            except Exception as e:
                print(f"Failed to notify {getattr(sub, 'name', sub)}: {e}")

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, subject: YoutubeChannel, event):
        print(f'User {self.name} received notification from: {subject.name}: {event}')

channel = YoutubeChannel('channel1')
channel.subscribe(YoutubeUser('user1'))
channel.subscribe(YoutubeUser('user2'))
channel.subscribe(YoutubeUser('user3'))

channel.notify('New video release')