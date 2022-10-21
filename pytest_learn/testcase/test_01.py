# from time import sleep
import pytest


class Test01:
    a = 10

    @pytest.mark.run(order=4)
    def test_01(self):
        # sleep(3)
        print('01')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @pytest.mark.skip(reason="jump")
    def test_02(self):
        # sleep(3)
        print('02')

    @pytest.mark.run(order=2)
    @pytest.mark.usermange
    @pytest.mark.skipif(a < 18, reason="limit")
    def test_03(self):
        # sleep(3)
        print('03')

    @pytest.mark.run(order=1)
    def test_04(self):
        # sleep(3)
        print("04")
