from fsm import *

class Run(State):
    def transitions(self):
        return {
            "toWalk": Walk(),
        }

    def execute(self):
        print "Person is running"

class Walk(State):
    def transitions(self):
        return {
            "toRun": Run(),
            "toStop": Stop(),
        }

    def execute(self):
        print "Person is walking"

class Stop(State):
    def transitions(self):
        return {
            "toWalk": Walk(),
        }

    def execute(self):
        print "Person stopped!"

fsm = FSM(Stop())
fsm.transition("toWalk")
fsm.transition("toStop")
fsm.transition("toWalk")
fsm.transition("toRun")
fsm.transition("toWalk")
fsm.transition("toStop")
fsm.transition("toRun")