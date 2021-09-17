import logging
import pytest

from tests.test_toolsqabooks import UnitTestBooks
from tests.test_toolsqaform import UnitTestForm

@pytest.mark.usefixtures("setup")
class BaseClass(UnitTestForm,UnitTestBooks):

    UnitTestForm()
    UnitTestBooks()
