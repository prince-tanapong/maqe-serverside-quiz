import random
import string

class CouponCode:
    def generate_coupon_code(self):
        start_coupon_code = 'MQ'
        choices = string.ascii_letters + string.digits
        coupon_code = ''.join(random.choice(choices) for i in range(8))
        return start_coupon_code + coupon_code

    def write_coupon_code_to_text_file(self):
        all_coupon_code = ''
        for i in range(250):
            all_coupon_code += '{0}\n'.format(self.generate_coupon_code())
        with open("section2.txt", "w") as text_file:
            text_file.write(all_coupon_code)

if __name__ == '__main__':
    CouponCode().write_coupon_code_to_text_file()
