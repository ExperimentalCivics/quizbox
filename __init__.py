from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class QuizBox(MycroftSkill):

    def __init__(self):
        super(QuizBox, self).__init__(name="QuizBox")
        self.count = 0

    @intent_handler(IntentBuilder("").require("query").require("QuizBox"))
    def handle_hello_world_intent(self, message):
        self.speak_dialog("quizbox.welcome")

def create_skill():
    return QuizBox()
