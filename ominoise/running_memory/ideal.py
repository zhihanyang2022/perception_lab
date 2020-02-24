# instructions_text = visual.TextStim(...)
# how to record the screen flip time for an upcoming event?

#   prepare_func()
#   win.timeOnFlip(timer, 'tStartRefresh')
#   win.flip()

class Timer:

    def __init__(self, win):
        self.win = win
        self.start_time = None
        self.end_time = None

    def record_start_time(self, action_func):
        action_func()
        self.win.timeOnFlip(self, 'start_time')
        win.flip()

    def record_end_time(self):
        self.win.timeOnFlip(self, 'end_time')
        win.flip()

    @property
    def start_and_end_time(self, reset=True):
        assert self.start_time is not None and self.end_time is not None
        return self.start_time, self.end_time

    def erase(self):
        self.start_time, self.end_time = None, None

# timer = Timer()
# timer.record_start_time()
# timer.record_end_time()
# timer.start_and_end_time
# timer.erase()
