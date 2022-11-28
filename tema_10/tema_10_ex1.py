import unittest
import HtmlTestRunner

from Tema.tema_9 import Login
from Curs.cod_intalnirea_10.auth import Authentication
from Curs.cod_intalnirea_10.alerts import Alerts
from Curs.cod_intalnirea_10.context_menu import ContextMenu
from Curs.cod_intalnirea_10.key_press import Keyboard

'''1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul'''

class HomeworkSuite(unittest.TestCase):
    def test_suite(self):
        # Creeam un obiect al clasei TestSuite
        test_to_run = unittest.TestSuite()
        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
        ])

        # Generam raportul HTML
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name="Report Homework_10",
            report_title="First Report Homework 10"
        )
        runner.run(test_to_run)