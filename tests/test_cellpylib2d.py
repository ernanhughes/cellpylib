import unittest
import pytest

import numpy as np
import os

import cellpylib as cpl

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestCellularAutomataFunctions2D(unittest.TestCase):

    def test_init_simple2d_1x1(self):
        arr = cpl.init_simple2d(rows=1, cols=1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 1)

    def test_init_simple2d_1x1_val2(self):
        arr = cpl.init_simple2d(rows=1, cols=1, val=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 2)

    def test_init_simple2d_2x2(self):
        arr = cpl.init_simple2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertEqual(arr[0][0].tolist(), [0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1])

    def test_init_simple2d_3x3(self):
        arr = cpl.init_simple2d(rows=3, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])
        self.assertEqual(arr[0][2].tolist(), [0, 0, 0])

    def test_init_simple2d_2x3(self):
        arr = cpl.init_simple2d(rows=2, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])

    def test_init_simple2d_coords(self):
        arr = cpl.init_simple2d(rows=3, cols=3, coords=(2, 2))
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][2].tolist(), [0, 0, 1])

    def test_init_simple2d_coords_invalid_type(self):
        with pytest.raises(Exception):
            cpl.init_simple2d(rows=3, cols=3, coords="a")

    def test_init_simple2d_coords_invalid_length(self):
        with pytest.raises(Exception):
            cpl.init_simple2d(rows=3, cols=3, coords=(0, 1, 2))

    def test_init_random2d_1x1(self):
        arr = cpl.init_random2d(1, 1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 1)

    def test_init_random2d_1x1_k2(self):
        arr = cpl.init_random2d(rows=1, cols=1, k=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 2)

    def test_init_random2d_2x2(self):
        arr = cpl.init_random2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertTrue(0 <= arr[0][0][0] <= 1)
        self.assertTrue(0 <= arr[0][0][1] <= 1)
        self.assertTrue(0 <= arr[0][1][0] <= 1)
        self.assertTrue(0 <= arr[0][1][1] <= 1)

    def test_init_random2d_3x3_k2(self):
        arr = cpl.init_random2d(rows=3, cols=3, k=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertTrue(0 <= arr[0][0][0] <= 2)
        self.assertTrue(0 <= arr[0][0][1] <= 2)
        self.assertTrue(0 <= arr[0][0][2] <= 2)
        self.assertTrue(0 <= arr[0][1][0] <= 2)
        self.assertTrue(0 <= arr[0][1][1] <= 2)
        self.assertTrue(0 <= arr[0][1][2] <= 2)
        self.assertTrue(0 <= arr[0][2][0] <= 2)
        self.assertTrue(0 <= arr[0][2][1] <= 2)
        self.assertTrue(0 <= arr[0][2][2] <= 2)

    def test_init_random2d_2x3(self):
        arr = cpl.init_random2d(rows=2, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertTrue(0 <= arr[0][0][0] <= 1)
        self.assertTrue(0 <= arr[0][0][1] <= 1)
        self.assertTrue(0 <= arr[0][0][2] <= 1)
        self.assertTrue(0 <= arr[0][1][0] <= 1)
        self.assertTrue(0 <= arr[0][1][1] <= 1)
        self.assertTrue(0 <= arr[0][1][2] <= 1)

    def test_init_random2d_dtype(self):
        arr = cpl.init_random2d(rows=2, cols=2, dtype=np.float32)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertTrue(0.0 <= arr[0][0][0] < 1.0)
        self.assertTrue(0.0 <= arr[0][0][1] < 1.0)
        self.assertTrue(0.0 <= arr[0][1][0] < 1.0)
        self.assertTrue(0.0 <= arr[0][1][1] < 1.0)

    def test_tot_rule126_2d_n9_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot_rule126_2d_n9_simple_init.ca")
        actual = self._create_ca(expected, 126, 'Moore')
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule26_2d_n5_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot_rule26_2d_n5_simple_init.ca")
        actual = self._create_ca(expected, 26, 'von Neumann')
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_sequential_rule_2d(self):
        cellular_automaton = cpl.init_simple2d(3, 3)
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126),
                                 update_order=range(0, 9))
        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=18, neighbourhood='Moore',
                                          apply_rule=r.apply_rule)
        expected = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, 0]],
                    [[1, 1, 0], [0, 1, 0], [0, 0, 0]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                    [[1, 1, 1], [1, 1, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [0, 0, 0]],
                    [[1, 1, 1], [1, 1, 1], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[1, 1, 1], [1, 1, 1], [1, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 1, 0]]]
        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_game_of_life_rule(self):
        expected = self._convert_to_numpy_matrix("game_of_life.ca").reshape(60, 60, 60)

        # Glider
        cellular_automaton = cpl.init_simple2d(60, 60)
        cellular_automaton[:, [28, 29, 30, 30], [30, 31, 29, 31]] = 1
        # Blinker
        cellular_automaton[:, [40, 40, 40], [15, 16, 17]] = 1
        # Light Weight Space Ship (LWSS)
        cellular_automaton[:, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45, 48, 44, 44, 44, 45, 46, 47, 48]] = 1

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                          apply_rule=cpl.game_of_life_rule)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_langtons_loop(self):
        expected = self._convert_to_numpy_matrix("langtons_loop.ca")

        langtons_loop = cpl.LangtonsLoop()

        cellular_automaton = langtons_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=langtons_loop.rule)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_evolve_unknown_neighbourhood_type(self):
        cellular_automaton = np.array([ [[1,1,1], [1,1,1], [1,1,1]] ])
        with pytest.raises(Exception) as e:
            cpl.evolve2d(cellular_automaton, timesteps=2, neighbourhood='foo', apply_rule=cpl.game_of_life_rule)
        self.assertTrue("unknown neighbourhood type: foo" in str(e.value))

    def _convert_to_numpy_matrix(self, filename):
        with open(os.path.join(THIS_DIR, 'resources', filename), 'r') as content_file:
            content = content_file.read()
            content = content.replace('{{{', '')
        content = content.replace('}}}', '')
        content = content.replace('{{', '')
        content = content.replace('{', '')
        content = [x.split('},') for x in content.split('}},')]
        content = [[h.split(',') for h in x] for x in content]
        content = [[[int(i) for i in h] for h in x] for x in content]
        return np.array(content, dtype=np.int32)

    def _create_ca(self, expected, rule, neighbourhood):
        steps, _, _ = expected.shape
        cellular_automaton = np.array([expected[0]])
        return cpl.evolve2d(cellular_automaton, timesteps=steps, r=1, neighbourhood=neighbourhood,
                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=rule))
