import unittest
from ViniAudit.output.html import *
from ViniAudit.output.utils import *

#
# Test methods for ViniAudit/output
#
class TestViniOutput(unittest.TestCase):

    ########################################
    # html.py
    ########################################

    def test_html_report(self):
        test_html = HTMLReport(report_name='test')
        assert (test_html.report_name == 'test')
        assert ('json' in test_html.get_content_from_folder(templates_type='conditionals'))
        assert ('json' in test_html.get_content_from_file(filename='/json_format.html'))

    def test_get_filename(self):
        assert ('ViniAudit-report/report.html' in get_filename("REPORT"))
        assert ('ViniAudit-report/ViniAudit-results/ViniAudit_results.js' in get_filename("RESULTS"))
        assert ('ViniAudit-results/ViniAudit_results.js' in get_filename("RESULTS", relative_path=True))
        assert ('ViniAudit-report/ViniAudit-results/ViniAudit_exceptions.js' in get_filename("EXCEPTIONS"))
        assert ('ViniAudit-results/ViniAudit_exceptions.js' in get_filename("EXCEPTIONS", relative_path=True))
        assert ('ViniAudit-report/ViniAudit-results/ViniAudit_errors.json' in get_filename("ERRORS"))
        assert ('ViniAudit-results/ViniAudit_errors.json' in get_filename("ERRORS", relative_path=True))
