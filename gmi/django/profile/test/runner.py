import os
import sys

from django.conf import settings
from django_nose import NoseTestSuiteRunner

os.environ['DJANGO_SETTINGS_MODULE'] = 'gmi.django.profile.test.settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


def runtests(*test_labels):
    runner = NoseTestSuiteRunner(verbosity=1, interactive=True)
    failures = runner.run_tests(test_labels)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])

