import ORIGINALONEtwo
import unittest

def froztest(func):
    def walltest(self, *args, **kwargs):
        if self.is_frozen == True:
            print("Тесты в этом кейсе заморожены")
        elif self.is_frozen == False:
            return func(self, *args, **kwargs)
    return walltest

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @froztest
    def setUp(self):
        self.usain = ORIGINALONEtwo.Runner("Уэйн", 10)
        self.andrei = ORIGINALONEtwo.Runner("Андрей", 9)
        self.Nick = ORIGINALONEtwo.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_result.items():
            print(f'{test_name}:{result}')

    @froztest
    def test_usain_and_nick(self):
        tournament = ORIGINALONEtwo.Tournament(90, self.usain, self.Nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        print(f'once: {formatted_result}')
        self.all_result['usein_and_nick'] = result
        self.assertFalse(list(result.values())[-1] == 'Nick')

    @froztest
    def test_andrei_and_nick(self):
        tournament = ORIGINALONEtwo.Tournament(90, self.andrei, self.Nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        print(f'duo: {formatted_result}')
        self.all_result['andrei_and_nick'] = result
        self.assertFalse(list(result.values())[-1] == 'Nick')

    @froztest
    def test_trio(self):
        tournament = ORIGINALONEtwo.Tournament(90, self.usain, self.andrei, self.Nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        print(f'trio: {formatted_result}')
        self.all_result['trio'] = result
        self.assertFalse(list(result.values())[-1] == 'Nick')


if __name__ == '__main__':
    unittest.main()

