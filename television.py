class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Function defines the initial settings fot the variable
        param a: status on/off
        param b: muted on/off
        param c: volume set at minimum of 0
        param d: channel set at minimum of 0
        """

        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL

    def power(self):
        """
        Function initialized the status variable
        param a: status of the television off
        """
        self.status = not self.status

    def mute(self):
        """
        Function initialized the muted variable
        param a: mute of the television off
        """
        self.muted = not self.muted

    def channel_up(self):
        """
        Function makes the channel increase on call
        param a: channel of the tv, increases by 1
        """
        if self.status:
            self.channel = (self.channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """
        Function makes the channel decrease on call
        param a: channel of the tv, decreases by 1
        """
        if self.status:
            self.channel = (self.channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        """
        Function makes the volume increase on call
        param a: volume of the tv, increases by 1
        """
        if self.status:
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                if self.muted:
                    self.muted = False

    def volume_down(self):
        """
        Function makes the volume decrease on call
        param a: volume of the tv, decreases by 1
        """
        if self.status:
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
                if self.muted:
                    self.muted = False

    def __str__(self):
        return f'Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}.'
