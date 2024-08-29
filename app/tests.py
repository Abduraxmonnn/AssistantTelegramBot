# async def main():
#     bot = Bot(token=TOKEN)
#     dp = Dispatcher()
#
#     # Define a condition, e.g., environment variable or a config file
#     condition = get_some_condition()  # Replace this with your condition
#
#     # Define commands based on the condition
#     if condition == 'condition1':
#         bot_commands = [
#             types.BotCommand(command="/start", description="Start bot for subscribe"),
#             types.BotCommand(command="/help", description="Get info about bot"),
#         ]
#         dp.include_routers(
#             start_handler.router,
#             help_handler.router
#         )
#     else:
#         bot_commands = [
#             types.BotCommand(command="/notify", description="Notification ON/OFF"),
#             types.BotCommand(command="/me", description="Information about User"),
#         ]
#         dp.include_routers(
#             notify_on_off_handler.router,
#             user_info_handler.router
#         )
#
#     await bot.set_my_commands(bot_commands)
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Exit")
