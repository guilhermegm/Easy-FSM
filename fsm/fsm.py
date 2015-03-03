class SimpleFSM(object):
    def __init__(self, initial_state):
        self.cur_state = initial_state

    def transition(self, trans_name):
        if self.cur_state:
            self.cur_state.exit()

        transitions = self.cur_state.transitions()

        if trans_name in transitions:
            if self.cur_state != transitions[trans_name]:
                self.cur_state.enter()
                self.cur_state = transitions[trans_name]
            self.cur_state.execute()
        else:
            print "No transition found at state ({0}), transition ({1})".format(self.cur_state.__class__.__name__, trans_name)