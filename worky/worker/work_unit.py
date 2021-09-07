class WorkUnit():
    """
    A unit of work.
    """

    def __init__(self, data, internal = False):
        self.data = data
        self.internal = internal

    def __str__(self):
        return f"{self.internal and 'Internal'}WorkUnit({self.data})"


Break = WorkUnit("break", True)
