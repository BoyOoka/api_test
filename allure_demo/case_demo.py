from allure_demo import cls_demo
import unittest
import pytest
import allure


class TestCaseDemo(cls_demo.Demo, unittest.TestCase):

    @allure.title('加法测试')
    def test_add(self):
        result = self.add(3, 3)
        self.assertEqual(result, 8, '加法')

    @allure.title('乘法测试')
    def test_plus(self):
        result = self.plus(3, 3)
        self.assertEqual(result, 12, '乘法')

    def test_division(self):
        result = self.division(9, 3)
        self.assertEqual(result, 3, '除法')

    @allure.title('减法')
    @pytest.mark.skipif(1+1 != 2, reason='skip if')
    def test_sub(self):
        result = self.subtraction(7, 2)
        self.assertEqual(result, 3, '减法')
        assert True

    @allure.feature('Xfail')
    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_xfail_expected_failure(self):
        """this test is an xfail that will be marked as expected failure"""
        assert True

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    @allure.feature('Xfail')
    def test_xfail_unexpected_pass(self):
        """this test is an xfail that will be marked as unexpected success"""
        assert True
