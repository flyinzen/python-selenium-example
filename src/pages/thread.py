from src.pages.base import BaseEntity


class MessagesThreadPage(BaseEntity):
    def body(self, text: str):
        return self.s(f'//div[contains(text(), "{text}")][@role="gridcell"]')

    def check_message_contains(self, text: str):
        assert self.body(text).is_displayed()
        return self
