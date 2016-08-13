from mock import patch, call
import string
import unittest

from .coupon_code import CouponCode

class TestCouponCode(unittest.TestCase):
    def setUp(self):
        self.coupon_code = CouponCode()

    def test_lenth_of_coupon_code_shoud_have_10_characters_long(self):
        expected_coupon_code = self.coupon_code.generate_coupon_code()
        self.assertEqual(len(expected_coupon_code), 10)

    def test_coupon_code_should_start_with_MQ(self):
        expected_coupon_code = self.coupon_code.generate_coupon_code()
        self.assertEqual(expected_coupon_code[0:2], 'MQ')

    @patch('server-side-test.coupon_code.random')
    def test_coupon_code_should_generate_correctly(
        self,
        mock_random
    ):
        mock_random.choice.side_effect = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h'
        ]
        expected_coupon_code = self.coupon_code.generate_coupon_code()

        self.assertEqual(expected_coupon_code, 'MQabcdefgh')
        self.assertEqual(mock_random.choice.call_count, 8)
        choices = string.ascii_letters + string.digits
        expected_calls = [call(choices) for i in range(8)]
        self.assertEqual(mock_random.choice.mock_calls, expected_calls)

    @patch('server-side-test.coupon_code.CouponCode.generate_coupon_code')
    @patch('server-side-test.coupon_code.open')
    def test_should_write_250_coupon_code_on_text_file_correctly(
        self,
        mock_open,
        mock_coupon_code
    ):

        self.coupon_code.write_coupon_code_to_text_file()

        self.assertEqual(mock_coupon_code.call_count, 250)
        mock_open.assert_called_once_with('section2.txt', 'w')
        self.assertEqual(
            mock_open.return_value.__enter__.return_value.write.call_count,
            1
        )


if __name__ == '__main__':
    unittest.main()
