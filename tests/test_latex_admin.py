#!/usr/bin/env python

"""Tests for `latex_admin` package."""


import unittest

from click.testing import CliRunner
# from latex_admin import latex_admin
from latex_admin import cli


class TestLatexAdmin(unittest.TestCase):
    """Tests for `latex_admin` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        self.assertIn('latex_admin.cli.main', result.output)
        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--help  Show this message and exit.', help_result.output)
