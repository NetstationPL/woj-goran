import unittest
import time

from mock import Mock
import pygame

from player_sprite import PlayerSprite


class TestPlayerSprite(unittest.TestCase):

    def setUp(self):
        body = Mock()
        body.position = (10, 10)
        body.velocity = [0, 0]

        self.sprite = PlayerSprite(body)

    def test_should_has_image(self):
        self.assertTrue(hasattr(self.sprite, "image"))

    def test_should_has_body(self):
        self.assertTrue(hasattr(self.sprite, "body"))

    def test_should_has_xy_from_body(self):
        self.assertEqual(self.sprite.rect.x, self.sprite.body.position[0])
        self.assertEqual(self.sprite.rect.y, self.sprite.body.position[1])

    def test_should_update_xy_from_body(self):
        self.sprite.body.position = (20, 20)
        self.sprite.update()

        self.assertEqual(self.sprite.rect.x, self.sprite.body.position[0])
        self.assertEqual(self.sprite.rect.y, self.sprite.body.position[1])

    def test_should_play_animation_on_state(self):
        images_1 = ['image1', 'image2', 'image3']
        self.sprite.body.velocity[0] = 100
        self.sprite.images = [None, images_1]
        self.sprite.state = 1

        time.sleep(self.sprite.get_animation_speed() / 1000.0)
        self.sprite.update()
        self.assertEqual(self.sprite.image, images_1[1])
        time.sleep(self.sprite.get_animation_speed() / 1000.0)
        self.sprite.update()
        self.assertEqual(self.sprite.image, images_1[2])

    def test_should_reset_frame_on_change_state(self):
        pygame.image.load = Mock()
        self.sprite.frame = 2
        self.sprite.state = 1
        self.assertEqual(self.sprite.frame, 0)

    def test_shouldnt_reset_if_state_same(self):
        self.sprite.state = 1
        self.assertEqual(self.sprite.frame, 0)
        self.sprite.frame = 1
        self.sprite.state = 1
        self.assertEqual(self.sprite.frame, 1)

    def test_shouldnt_reset__time_if_state_same(self):
        self.sprite.state = 1
        ltime = self.sprite.last_frame_time

        self.sprite.state = 1

        self.assertEqual(self.sprite.last_frame_time, ltime)

    def test_should_change_frame(self):
        self.sprite.images = ((1, 2, 3),)
        self.sprite.frame = 0
        self.sprite.body.velocity[0] = 1
        self.sprite.change_frame()
        self.assertEqual(self.sprite.frame, 1)

    def test_get_current_frame(self):
        self.sprite.images = ((1, 2, 3),)
        self.sprite.frame = 1
        self.assertEqual(self.sprite.get_current_frame(), 2)

    def test_should_animation_speed_depends_on_velocityx(self):
        self.sprite.body.velocity = [10, 0]
        speed = self.sprite.get_animation_speed()
        self.sprite.body.velocity[0] = 100
        self.assertLess(self.sprite.get_animation_speed(), speed)

    def test_should_set_pos_direction(self):
        self.sprite.body.velocity[0] = 10
        self.sprite.change_direction()
        self.assertEqual(self.sprite.direction, 1)

    def test_should_set_neg_direction(self):
        self.sprite.body.velocity[0] = -10
        self.sprite.change_direction()
        self.assertEqual(self.sprite.direction, -1)

    def test_direction_not_change_after_stop(self):
        self.sprite.body.velocity[0] = -10
        self.sprite.change_direction()
        self.sprite.body.velocity[0] = 0
        self.sprite.change_direction()
        self.assertEqual(self.sprite.direction, -1)

    def test_change_direction_on_update(self):
        self.sprite.change_direction = Mock()
        self.sprite.update()
        self.assertTrue(self.sprite.change_direction.called)

    def test_flip_image_on_neg_direction(self):
        pygame.transform.flip = Mock()
        self.sprite.direction = -1
        self.sprite.update()
        self.assertTrue(pygame.transform.flip.called)
