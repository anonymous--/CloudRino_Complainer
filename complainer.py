import twitter

class complain():
    def __init__(self, days, position, date, old_position):
        self.days = days
        self.position = position
        self.date = date
        self.old_position = old_position
        if days <= 1:
            days = ('{} day'.format(self.days))
        else:
            days = ('{} days'.format(self.days))

    def not_moved(self):
        twitter.send(str(
            "Hello cloudrino, it has been {} since I last checked and there hasn't been any change in my position."
            "\nMy last position was {} on {}.\nThis is an automated message since I haven't seen any change in a "
            "very long time, I decided to make this bot.\nIf you don't like this bot you can find our email by "
            "looking into my position and email me about it.".format(
                self.days, self.position, self.date)))

    def moved_back(self):
        twitter.send(str("Aargh, I have been bushed back. My old postition was {}, and now I'm at {}. Will report back in 24 hours"
                   .format(self.old_position, self.position)))

    def moved_up(self):
        twitter.send(str("Ahh, thanks I have been moved up in my position. My old position was {}, now I'm at {}.\n"
                   "Thank you.".format(self.old_position, self.position)))