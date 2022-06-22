from mygeodemo import mygeodemo
from mygeodemo.mygeodemo import LeafMap

def test_LeafMap():
    m = LeafMap()
    assert isinstance(m, LeafMap), print('Map was not successfully created')

