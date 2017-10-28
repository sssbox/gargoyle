# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import django
from django.core.management import call_command


def test_no_migrations_required(db):
    if django.VERSION >= (1, 10):
        try:
            call_command('makemigrations', 'gargoyle', check=1)
        except SystemExit:
            raise AssertionError('Migrations required')
    else:
        try:
            call_command('makemigrations', 'gargoyle', exit=1)
        except SystemExit:
            pass
        else:
            raise AssertionError('Migrations required')
