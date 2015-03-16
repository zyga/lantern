#!/usr/bin/env python3
# This file is part of Lantern.
#
# Copyright 2015 Canonical Ltd.
# Written by:
#   Zygmunt Krynicki <zygmunt.krynicki@canonical.com>
#
# Lantern is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3,
# as published by the Free Software Foundation.
#
# Lantern is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Lantern.  If not, see <http://www.gnu.org/licenses/>.
import argparse
import logging
import sys
import uuid

try:
    from plainbox.impl.applogic import PlainBoxConfig
    from plainbox.impl.commands.inv_run import RunInvocation
    from plainbox.provider_manager import ManageCommand
    from plainbox.provider_manager import docstring
    from plainbox.provider_manager import manage_py_extension
    from plainbox.provider_manager import setup, N_, _
except ImportError as exc:
    raise SystemExit(
        """
        Unable to import plainbox.

        Please check if you have plainbox >= 0.20 installed on your machine. If
        the error persists please report it with the following additional
        information on: https://bugs.launchpad.net/plainbox/+filebug

        {}
        """.format(exc))


class CustomRunInvocation(RunInvocation):

    @property
    def expected_app_id(self):
        return 'lantern'


@manage_py_extension
@docstring(N_(
    """
    run all of the lantern tests

    @EPILOG@

    This command is similar to a hard-coded version of ``plainbox run``
    that has the lantern testing provider installed and runs the
    'all-tests' test plan from the same provider.
    """))
class RunCommand(ManageCommand):

    gettext_domain = "plainbox-provider-lantern"

    def register_parser(self, subparsers):
        parser = self.add_subcommand(subparsers)
        parser.add_argument(
            '-n', '--non-interactive', action='store_true',
            help=_("skip tests that require interactivity"))
        parser.add_argument(
            '--no-color', dest='color', action='store_false',
            help=argparse.SUPPRESS)
        parser.set_defaults(color=None)

    def invoked(self, ns):
        provider_loader = lambda: [self.get_provider()]
        config_loader = lambda: PlainBoxConfig.get()
        ns.output_format = 'text'
        ns.output_options = []
        ns.output_file = sys.stdout
        ns.transport = None
        ns.dont_suppress_output = True
        ns.dry_run = False
        ns.test_plan = (
            '2015.pl.zygoon.lantern::all-tests')
        ns.whitelist = []
        ns.include_pattern_list = []
        ns.exclude_pattern_list = []
        # Silence the confusing and incorrect errors about missing test plan
        logging.getLogger("plainbox.commands.checkbox").setLevel(
            logging.CRITICAL)
        inv = CustomRunInvocation(provider_loader, config_loader, ns, ns.color)
        fname = 'lantern-submission-{}.json'.format(uuid.uuid1())
        inv.run()
        with open(fname, 'wb') as stream:
            ns.output_file = stream
            ns.output_format = 'json'
            ns.output_options = (
                "with-io-log,flatten-io-log,with-resource-map,"
                "with-attachments,with-comments")
            inv.create_exporter()
            inv.export_and_send_results()


setup(
    name='2015.pl.zygoon.lantern:lantern',
    version="0.1",
    description=N_("Lantern Brightness Analysis and Debugging"),
    gettext_domain='plainbox-provider-lantern',
)
