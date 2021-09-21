
import pytest
from tests.test_toolsqaform import UnitTestForm

@pytest.mark.usefixtures("setup")
class BaseClass(UnitTestForm):

    UnitTestForm()
