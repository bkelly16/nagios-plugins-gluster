#
# Copyright 2014 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

from testrunner import PluginsTestCase as TestCaseBase
from plugins import nscautils
from glusternagios import utils


class TestProc(TestCaseBase):
    def _maskGetoutputSuccess(self, val):
        return 0, "PROCS OK:", ""

    def _maskGetoutputCritical(self, val):
        return 0, "PROCS CRITICAL:", ""

    def _maskSendToNsca(self, hostName, service, status, msg):
        return service, status, msg

    def test_Nfs(self):
        nscautils.send_to_nsca = self._maskSendToNsca
        utils.execCmd = self._maskGetoutputCritical
