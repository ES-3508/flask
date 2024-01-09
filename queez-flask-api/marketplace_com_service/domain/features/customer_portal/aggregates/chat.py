from ..valueobjects.messageid import MessageID
from ..valueobjects.senderid import SenderID
from ..valueobjects.receiverid import ReceiverID
from ..valueobjects.message import MessageText


class Chat:
    def __init__(self, message_id: MessageID, sender_id: SenderID, receiver_id: ReceiverID, msg: MessageText):
        self.message_id = message_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.msg = msg