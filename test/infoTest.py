from Agent.info import Info
import unittest

class InfoTest(unittest.TestCase):

    def test_cpu_alert(self):
        info =Info()
        t = info.cpuAlert()
        print(t)
        self.assertIsNotNone(t)