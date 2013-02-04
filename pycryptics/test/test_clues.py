import unittest
# from pycryptics.solve_clue import CrypticClueSolver, split_clue_text
from pycryptics.parse_and_solve import solve_clue_text, split_clue_text


class TestClues(unittest.TestCase):
    def test_known_clues(self):
        # with CrypticClueSolver() as solver:
        #     for clue_text in open('clues/known_clues.txt', 'r').readlines():
        #         phrases, lengths, pattern, known_answer = split_clue_text(clue_text)
        #         solver.setup(clue_text)
        #         answers = solver.run()
        #         for a in answers[:5]: print a
        #         self.assertEqual(answers[0].answer.lower(), known_answer.lower().strip())
        for clue_text in open('clues/known_clues.txt', 'r').readlines():
            phrases, lengths, pattern, known_answer = split_clue_text(clue_text)
            answers = solve_clue_text(clue_text)
            # solver.setup(clue_text)
            # answers = solver.run()
            for a in answers[:5]: print a
            self.assertEqual(answers[0].answer.lower(), known_answer.lower().strip())
