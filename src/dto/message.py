from dataclasses import dataclass


@dataclass
class Message:
    to: str
    subject: str
    body: str
