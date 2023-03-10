"""
Copyright (c) 2022 Sven Gronauer (Technical University of Munich)

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""
import unittest
import numpy as np
import gym
import pybullet as p


def rpy_to_firmware_quaternion(rpy: np.ndarray):
    """Function implemented on CrazyFlie Firmware.

    see: https://gitlab.lrz.de/projectphoenix/crazyflie-firmware-phoenix/-/blob/neuralTask/src/modules/src/stabilizer.c#L235

    Parameters
    ----------
    rpy

    Returns
    -------

    """
    assert rpy.shape == (3, )
    roll, pitch, yaw = rpy
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    # watch out the order !!!!
    return np.array([x, y, z, w])


class TestQuaternion(unittest.TestCase):

    def test_quaternion_firmware_calculation(self):
        """Test the implemented Quaternion calc of our Firmware..."""

        rpy = np.random.uniform(-2, 2, 3)
        abcd = rpy_to_firmware_quaternion(rpy)
        # back check
        rpy_prime = p.getEulerFromQuaternion(abcd)
        # print(abcd)
        print(rpy)
        print(rpy_prime)
        self.assertTrue(np.allclose(rpy, rpy_prime))


if __name__ == '__main__':
    unittest.main()
