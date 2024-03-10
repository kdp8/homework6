import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("GreetCommand executed successfully.")
        print("Hello, World!")