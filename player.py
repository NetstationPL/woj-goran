# -*- coding: utf-8 -*-

STATE_WALK = 1
STATE_JUMP = 2
STATE_IDLE = 0


class Player(object):
    """ Player object."""

    def __init__(self, body=None, sprite=None):
        self.body = body
        self.sprite = sprite
        self.vertical_speed = 10
        self.sprite.state = STATE_IDLE

    @property
    def position(self):
        return self.body.position

    @property
    def velocity(self):
        return self.body.velocity

    def update(self):
        self.sprite.update()

    def draw(self):
        self.sprite.draw()

    def is_jumping(self):
        pass

    def jump(self):
        pass

    def walk(self, direction=1):
        self.body.velocity[0] = self.vertical_speed * direction
        self.sprite.state = STATE_WALK

    def is_walking(self):
        return self.body.velocity[0] != 0

    def stand(self):
        self.body.velocity[0] = 0
        self.sprite.state = STATE_IDLE

    def is_standing(self):
        return self.body.velocity[0] == 0

    # def jump(self):
    #     if self.is_jumping():
    #         return
    #     self.body.apply_impulse(pymunk.vec2d.Vec2d(0, -4000))
    #     if self.is_walking():
    #         self.body.apply_impulse(
    #             pymunk.vec2d.Vec2d(5000 * self.direction * -1, 0))
