import subprocess
import unittest
from unittest import mock

import pytest
from ViniAudit.__main__ import run_from_cli
from ViniAudit.core.console import set_logger_configuration


class TestViniAuditClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        set_logger_configuration(is_debug=True)
        cls.has_run_Vini_suite = False

    @pytest.mark.xfail("only runs with AWS, cannot be used dynamically")
    @staticmethod
    def call_Vini_suite(args):
        args = ['./Vini.py'] + args

        args.append('aws')

        if TestViniAuditClass.profile_name:
            args.append('--profile')
            args.append(TestViniAuditClass.profile_name)
        # TODO: FIXME this only tests AWS

        args.append('--force')
        args.append('--debug')
        args.append('--no-browser')
        if TestViniAuditClass.has_run_Vini_suite:
            args.append('--local')
        TestViniAuditClass.has_run_Vini_suite = True

        sys = None
        with mock.patch.object(sys, 'argv', args):
            return run_from_cli()

    def test_Vini_suite_help(self):
        """Make sure that ViniAudit does not crash with --help"""
        command = './Vini.py --help'
        process = subprocess.Popen(command, shell=True, stdout=None)
        process.wait()
        assert process.returncode == 0

    @pytest.mark.xfail
    def test_Vini_suite_default_run(self):
        """Make sure that ViniAudit's default run does not crash"""
        rc = self.call_Vini_suite([])
        assert (rc == 0)
