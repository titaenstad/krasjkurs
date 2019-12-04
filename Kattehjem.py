class Kattehjem:
    def __init__(self):
        self._katter = []

    def flyttInnKatt(self, katt):
        self._katter.append(katt)

    def flyttUtKatt(self, katt):
        self._katter.remove(katt)

    def hentKatter(self):
        return self._katter
