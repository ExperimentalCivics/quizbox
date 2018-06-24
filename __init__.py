from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.skills.context import adds_context, removes_context

class QuizBox(MycroftSkill):
    @intent_handler(IntentBuilder('Quizntent').require("Play").require("QuizKeyword"))
    @adds_context('QuizContext')
    def handle_quiz_intent(self, message):
        self.answer = False
        self.speak_dialog("quizbox.welcome")
        self.speak_dialog("quizbox.question", expect_response=True)

    @intent_handler(IntentBuilder('AnswerIntent').require("Answer").
                                  require('QuizContext').build())
    @removes_context('QuizContext')
    @adds_context('AnswerContext')
    def handle_answer_intent(self, message):
        self.answer = True
        self.speak_dialog("quizbox.correctAnswer")
        self.speak('Red bull gives you wings!', expect_response=False)

    def __init__(self):
        super(QuizBox, self).__init__(name="QuizBox")
        self.count = 0

def create_skill():
    return QuizBox()
