import unittest
from triotestONETWO import TournamentTest
from distance12 import RunnerTest



class TesrSuite(TournamentTest, RunnerTest):
    runnertest = unittest.TextTestRunner(verbosity=2)
