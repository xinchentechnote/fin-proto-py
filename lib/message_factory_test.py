
from lib.message_factory import MessageFactory


class DummyMessageFactory(MessageFactory[str,object]): ...

class DummyMessage: ...

factory = DummyMessageFactory()
factory.register("DUMMY", DummyMessage)

def test_message_factory():
    factory1 = DummyMessageFactory()
    factory2 = DummyMessageFactory()
    assert factory1 is factory2  # Singleton behavior
    message = factory1.create("DUMMY")
    assert isinstance(message, DummyMessage)