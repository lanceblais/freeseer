#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
# Copyright (C) 2012 Free and Open Source Software Learning Centre
# http://fosslc.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/Freeseer/freeseer/

import unittest
import logging

from freeseer.frontend.reporteditor.reporteditor import ReportEditorApp

from PyQt4 import QtGui, QtTest, Qt

class TestReportEditorApp(unittest.TestCase):
	'''
	Test cases for ReportEditorApp. 
	'''


	def setUp(self):
		'''
		Stardard init method: runs before each test_* method

		Initializes a QtGui.QApplication and ReportEditorApp object.
		ReportEditorApp() causes the UI to be rendered.
		'''

		self.app = QtGui.QApplication([])
		self.report_editor = ReportEditorApp()
		self.report_editor.show()


	def test_close_report_editor(self):
		'''
		Tests closing the ReportEditorApp
		'''

		QtTest.QTest.mouseClick(self.report_editor.editorWidget.closeButton, Qt.Qt.LeftButton)
		self.assertFalse(self.report_editor.editorWidget.isVisible())
