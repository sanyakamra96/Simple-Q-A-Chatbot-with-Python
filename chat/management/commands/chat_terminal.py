from django.core.management.base import BaseCommand
from django.conf import settings

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


class Command(BaseCommand):
    help = "Start a terminal chat session with the ChatterBot."

    def handle(self, *args, **options):
        # Create chatbot from Django settings
        bot = ChatBot(**settings.CHATTERBOT)

        self.stdout.write(self.style.SUCCESS("Initializing and training bot..."))

        # Train using English corpus (greetings, conversations, etc.)
        corpus_trainer = ChatterBotCorpusTrainer(bot)
        corpus_trainer.train("chatterbot.corpus.english")  # built-in corpus
        # Official corpus training usage :contentReference[oaicite:3]{index=3}

        # Optional small custom training for better “assignment demo” feel
        custom_trainer = ListTrainer(bot)
        custom_trainer = ListTrainer(bot)
        custom_trainer.train([
            "Hi",
            "Hello! How can I help you today?",

            "Hey how is it going?",
            "I’m doing great! How about you?",

            "I am Sanya",
            "Nice to meet you Sanya! 😊",

            "Who are you?",
            "I am a friendly chatbot built by Sanya!",

            "What can you do?",
            "I can chat with you, answer simple questions, and keep you company!",

            "How are you?",
            "I’m doing well, thank you for asking!",

            "Bye",
            "Talk to you soon! 👋",
        ])


        self.stdout.write(self.style.SUCCESS(
            "\nTerminalBot is ready! Type 'exit' or 'quit' to stop.\n"
        ))

        # Chat loop
        while True:
            try:
                user_text = input("user: ").strip()
                if user_text.lower() in {"exit", "quit"}:
                    print("bot: Bye! 👋")
                    break

                response = bot.get_response(user_text)
                print(f"bot: {response}")

            except (KeyboardInterrupt, EOFError):
                print("\nbot: Bye! 👋")
                break
            except Exception as e:
                print(f"bot: Oops — something went wrong: {e}")
