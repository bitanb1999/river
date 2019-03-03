from . import base
from . import rolling_max
from . import rolling_min


class RollingPeakToPeak(base.RunningStatistic):
    """Computes a windowed peak to peak (max - min) over a window.

    Attributes:
        window_size (int): Size of the rolling window.

    Example:

    ::

        >>> from creme import stats

        >>> X = [1, -4, 3, -2, 2, 1]
        >>> ptp = stats.RollingPeakToPeak(window_size=2)
        >>> for x in X:
        ...     print(ptp.update(x).get())
        0
        5
        7
        5
        4
        1

    """

    def __init__(self, window_size):
        self.max = rolling_max.RollingMax(window_size)
        self.min = rolling_min.RollingMin(window_size)

    @property
    def name(self):
        return 'rolling_ptp'

    def update(self, x):
        self.max.update(x)
        self.min.update(x)
        return self

    def get(self):
        return self.max.get() - self.min.get()
