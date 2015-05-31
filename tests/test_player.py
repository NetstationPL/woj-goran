import unittest

from mock import Mock

from player import Player, STATE_WALK, STATE_IDLE


class TestPlayer(unittest.TestCase):

    def setUp(self):
        body = Mock()
        sprite = Mock()
        body.position = [0, 0]
        body.velocity = [0, 0]
        self.player = Player(body=body, sprite=sprite)

    def test_should_instantinate(self):
        self.assertIsNotNone(self.player)

    def test_should_has_position(self):

        self.assertTrue(hasattr(self.player, "position"))

    def test_position_should_have_two_ints(self):

        self.assertEqual(len(self.player.position), 2)
        self.assertIsInstance(self.player.position[0], int)
        self.assertIsInstance(self.player.position[1], int)

    def test_should_stand(self):
        self.player.body.velocity[0] = 10
        self.player.stand()
        self.assertEqual(self.player.velocity[0], 0)

    def test_should_has_stand_state(self):
        self.player.stand()
        self.assertTrue(self.player.is_standing())

    def test_should_walk_right(self):
        self.player.body.velocity[0] = 0
        self.player.walk()
        self.assertGreater(self.player.velocity[0], 0)

    def test_should_walk_left(self):
        self.player.body.velocity[0] = 0
        self.player.walk(-1)
        self.assertLess(self.player.velocity[0], 0)

    def test_should_has_walk_state(self):
        self.player.walk()
        self.assertTrue(self.player.is_walking())
        self.player.stand()
        self.player.walk(-1)
        self.assertTrue(self.player.is_walking())

    def test_should_has_sprite(self):
        sprite = Mock()
        self.player = Player(sprite=sprite)
        self.assertTrue(hasattr(self.player, "sprite"))

    def test_should_propagate_update_calls_to_sprite(self):

        self.player.update()

        self.assertTrue(self.player.sprite.update.called)

    def test_should_propagate_draw_calls_to_sprite(self):

        self.player.draw()

        self.assertTrue(self.player.sprite.draw.called)

    def test_should_set_speed(self):
        self.player.vertical_speed = 100
        self.player.walk()
        self.assertEqual(self.player.body.velocity[0],
                         self.player.vertical_speed)

    def test_should_set_state(self):
        self.assertEqual(self.player.sprite.state, STATE_IDLE)
        self.player.walk()
        self.assertEqual(self.player.sprite.state, STATE_WALK)
        self.player.stand()
        self.assertEqual(self.player.sprite.state, STATE_IDLE)

if __name__ == '__main__':
    unittest.main()
