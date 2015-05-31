import unittest

from mock import Mock
import pygame

from player_sprite import PlayerSprite


class TestPlayerSprite(unittest.TestCase):

    def setUp(self):
        body = Mock()
        body.position = (10, 10)

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
        self.sprite.state = 1
        images_1 = ['image1', 'image2', 'image3']
        self.sprite.images = [None, images_1]
        self.sprite.update()

        self.assertEqual(self.sprite.image, images_1[1])
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