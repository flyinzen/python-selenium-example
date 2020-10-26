from data import users
from src.dto.message import Message
import time

test_message = Message(
    to=users.bob.email,
    subject=f'Test subj {int(time.time())}',
    body='Message body comes here'
)