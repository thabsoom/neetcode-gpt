import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z=z-np.max(z)
        exp_z=np.exp(z)
        z=exp_z/sum(exp_z)
        return np.round(z,4)


