from pathlib import Path
from typing import Union

import numpy as np
from numpy.typing import NDArray
from xmipy import XmiWrapper


class SwapWrapper(XmiWrapper):
    def __init__(
        self,
        lib_path: Union[str, Path],
        lib_dependency: Union[str, Path, None] = None,
        working_directory: Union[str, Path, None] = None,
        timing: bool = False,
    ):
        super().__init__(lib_path, lib_dependency, working_directory, timing)

    def get_head_ptr(self) -> NDArray[np.float64]:
        """
        Gets heads array from SWAP

        Parameters
        ----------
        none

        Returns
        -------
         swap_head: NDArray[np.float64]
            array of the heads used by SWAP. Array as pointer to the SWAP intenal array
        """
        return self.get_value_ptr("MODFLOW_groundwater_level")

    def get_volume_ptr(self) -> NDArray[np.float64]:
        """
        Gets volume array from SWAP

        Parameters
        ----------
        none

        Returns
        -------
         swap_volume: NDArray[np.float64]
            array of volume used by SWAP. Array as pointer to the SWAP intenal array
        """
        return self.get_value_ptr("SWAP_groundwater_recharge")

    def get_storage_ptr(self) -> NDArray[np.float64]:
        """
        Gets storage array from metaswap

        Parameters
        ----------
        none

        Returns
        -------
         swap_storage: NDArray[np.float64]
            array of storage used by SWAP. Array as pointer to the SWAP intenal array
        """
        return self.get_value_ptr("SWAP_specific_yield")
