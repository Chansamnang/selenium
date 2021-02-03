import unittest
import HtmlTestRunner
import os
from testcase1 import LoginTestCase1
from testcase2 import LoginTestCase2

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
Login_Test_Case1 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase1)
Login_Test_Case2 = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase2)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([Login_Test_Case1, Login_Test_Case2])

# open the report file
outfile = open(dir + '\SeleniumPythonTestSummary.html', 'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=outfile,
    report_title='Test Report',
    descriptions='Testing',
    combine_reports=True    # combine test case together
)

# run the suite using HTMLTestRunner
runner.run(test_suite)