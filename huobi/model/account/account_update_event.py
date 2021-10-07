from huobi.constant import *
from huobi.model.account import AccountUpdate


class AccountUpdateEvent:
    """
    The account change information received by subscription of account.

    :member
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        change_type: The event that asset change notification related.
        account_change_list: The list of account change, the content is AccountChange class

    """

    def __init__(self):
        self.ch = 0
        self.data = AccountUpdate()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Topic")
        self.data.print_object()
