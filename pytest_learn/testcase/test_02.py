import pytest


class Test02:

    @pytest.mark.smoke
    def test_03(self):
        print('03')

    def test_04(self,my_fixture):
        print('04')
