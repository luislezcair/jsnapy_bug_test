import pprint
from jnpr.jsnapy import SnapAdmin
from jnpr.junos import Device

CONFIG_FILE = 'test_show_default_route.yml'
PRE_SNAP = 'pre_show_route_test.xml'
POST_SNAP = 'post_show_route_test.xml'

TESTS = {'tests': [CONFIG_FILE]}


if __name__ == "__main__":
    device = Device(host='example.com', user='jsnapy', passwd='123456')

    snap = SnapAdmin()
    r = snap.check(TESTS, PRE_SNAP, POST_SNAP, device)
    pprint.pprint(r[0].test_results)
