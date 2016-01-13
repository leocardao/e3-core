from __future__ import absolute_import

import pytest
import e3.platform


def test_platform():

    a = e3.platform.Platform.get()
    b = e3.platform.Platform.get()

    assert b == a

    assert hash(b) == hash(a)

    c = e3.platform.Platform.get(
        platform_name='arm-linux-linux')

    assert b != c

    assert c.os.name == 'linux'


def test_immutable():

    a = e3.platform.Platform.get()

    with pytest.raises(AttributeError):
        a.domain = 'example.net'

    b = a._replace(domain='example.net')
    assert b != a