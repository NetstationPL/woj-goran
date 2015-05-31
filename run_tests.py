#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tests.test_player import TestPlayer
from tests.test_player_sprite import TestPlayerSprite

test_player = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
test_player_sprite = \
    unittest.TestLoader().loadTestsFromTestCase(TestPlayerSprite)

runner = unittest.TextTestRunner(verbosity=2)

alltests = unittest.TestSuite([test_player, test_player_sprite])

if __name__ == '__main__':
    runner.run(alltests)
