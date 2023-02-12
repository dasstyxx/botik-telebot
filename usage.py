# from botik.templates import back_home_widget
#
#
# class MyPage(Page):
#     async def make_page_content(self, user):
#         button1 = ButtonData("Button1", ButtonCallback(self.send, message=f"Cool button"))
#         button2 = ButtonData("Button2", ButtonCallback(self.nav.change_page, path=f"/pidoras"))
#
#         back_home_buttons = back_home_widget()
#
#         self.markup.add_row([button1, button2])
#         self.markup.add_row(back_home_buttons)
#
#         await self.send(user, "Choose your destiny:", markup=True)
