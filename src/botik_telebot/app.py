import asyncio

from botik.app import App
from botik.templates.page_templates import PageTemplates
from botik.input.user_input import UserInput
from botik.navigation.navigation import Navigation
from botik.page.page_factory import PageFactory
from botik_telebot.api.api import TgApi
from botik_telebot.input.message_handlers.raw_message_handlers import RawMessageHandlers
from botik_telebot.page.page_factory import TgPageFactory


class TgApp(App):
    def start(self):
        asyncio.run(self.bot.polling())

    def __init__(self, bot, start_callback=None):
        super().__init__(bot)
        self.message_handlers = RawMessageHandlers(bot, start_callback,
                                                   self.users, self.navigator,
                                                   self.user_input, self.events)

    def initialize(self, bot):
        api = TgApi(bot)
        self.navigator = Navigation()
        self.templates = PageTemplates(self.navigator)

        self._page_fac: PageFactory = TgPageFactory(api, self.navigator, self.templates, self.events)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)
