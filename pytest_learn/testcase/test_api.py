import os

import pytest
import requests

from testcase.yaml_util import YamlUtil


class TestApi:

    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/testcase/test_api.yaml').read_yaml())
    def test_01_aa(self, args):
        url = args['request']['url']
        params = args['request']['params']
        res = requests.get(url, params=params)
        print(res.text)
