# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]
# (c) modified by Aishik Tokdar(t.me/aishik_tokdar)

from telethon import TelegramClient


class TortkClient(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for now only queue is required
        self.queue = None
        self.dl_passwords = {}
        self.pyro = None
