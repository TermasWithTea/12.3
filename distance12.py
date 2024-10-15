import unittest

def froztest(func):
    def walltest(self, *args, **kwargs):
        if self.is_frozen == True:
            print("Тесты в этом кейсе заморожены")
        elif self.is_frozen == False:
            return func(self, *args, **kwargs)
    return walltest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @froztest
    def test_walk(self):
        runner = Runner('test-walk')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @froztest
    def test_run(self):
        runner = Runner('test_walk')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @froztest
    def test_challenge(self):
        challenger = Runner('test1')
        challenge2 = Runner('test2')

        for _ in range(10):
            challenger.run()
            challenge2.walk()
        self.assertNotEqual(challenger.distance, challenge2.distance)


if __name__ == '__main__':
    unittest.main()
