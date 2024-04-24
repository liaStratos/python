import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertEqual(tv.status, False)
        self.assertEqual(tv.muted, False)
        self.assertEqual(tv.volume, Television.MIN_VOLUME)
        self.assertEqual(tv.channel, Television.MIN_CHANNEL)

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertEqual(tv.status, True)
        tv.power()
        self.assertEqual(tv.status, False)

    def test_mute(self):
        tv = Television()
        tv.mute()
        self.assertEqual(tv.muted, True)
        tv.mute()
        self.assertEqual(tv.muted, False)

    def test_channel_up(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        self.assertEqual(tv.channel, Television.MIN_CHANNEL + 1)
        for _ in range(Television.MAX_CHANNEL):
            tv.channel_up()
        self.assertEqual(tv.channel, Television.MIN_CHANNEL)

    def test_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        self.assertEqual(tv.channel, Television.MAX_CHANNEL)
        for _ in range(Television.MAX_CHANNEL):
            tv.channel_down()
        self.assertEqual(tv.channel, Television.MAX_CHANNEL)

    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        self.assertEqual(tv.volume, Television.MIN_VOLUME + 1)
        for _ in range(Television.MAX_VOLUME):
            tv.volume_up()
        self.assertEqual(tv.volume, Television.MAX_VOLUME)

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_down()
        self.assertEqual(tv.volume, Television.MIN_VOLUME)
        for _ in range(Television.MIN_VOLUME):
            tv.volume_down()
        self.assertEqual(tv.volume, Television.MIN_VOLUME)


if __name__ == '__main__':
    unittest.main()
