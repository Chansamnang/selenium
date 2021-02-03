import unittest
import HtmlTestRunner
import os
from login import Login

dir = os.getcwd()

Login_testcase = unittest.TestLoader().loadTestsFromTestCase(Login)

test_suite = unittest.TestSuite([Login_testcase])

outfile = open(dir + '\LoginTestSummary.html', 'w')

runner = HtmlTestRunner.HTMLTestRunner(
    stream=outfile,
    report_title='Test Report',
    descriptions='Testing',
)

runner.run(test_suite)