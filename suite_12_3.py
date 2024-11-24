import unittest
import tests_12_3

testic = unittest.TestSuite()

testic.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testic.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

texttest = unittest.TextTestRunner(verbosity=2)
texttest.run(testic)