#!/usr/bin/env python3

import unittest
from testpack_helper_library.unittests.dockertests import Test1and1Common
import time


class Test1and1Image(Test1and1Common):

    # <tests to run>

    def test_application(self):
        time.sleep(5)
        driver = self.getChromeDriver()
        driver.get("http://%s:8080/" % (Test1and1Image.container_ip))
        self.assertTrue(
            driver.title.find('phpMyAdmin') > -1,
            msg="Failed to find application page"
        )

    # </tests to run>

if __name__ == '__main__':
    unittest.main(verbosity=1)
