from threading import Thread


class ThreadWithReturnValue(Thread):

    # constructor
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    # the main thread function
    def run(self):
        """
        Run thread and save its return value
        :return: None
        """
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    # overrides join function in threading.Thread
    def join(self):
        """
        Returns the value saved during run function (self._return)
        :return: Thread return value
        """
        Thread.join(self)
        return self._return
