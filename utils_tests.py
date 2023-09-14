import utils

def assert_expect_error(func, value):
    errored_flag = False
    try:
        func(value)
    except:
        errored_flag = True

    assert(errored_flag)


def test_reverse():
    assert(utils.reversed(123) == 321)              ## integer
    assert_expect_error(utils.reversed, -123)       ## negative
    assert_expect_error(utils.reversed, 1.23)       ## float
    assert_expect_error(utils.reversed, "hello")    ## string
    print("reverse test passed")

def test_formatter():
    assert(utils.formatter(10) == ('0b1010', '0o12'))       ## integer
    assert(utils.formatter(-10) == ('-0b1010', '-0o12'))    ## negative
    assert_expect_error(utils.formatter, 1.1)               ## float
    assert_expect_error(utils.formatter, "hello")           ## string
    print("formatter test passed")


if __name__ == '__main__':
    test_reverse()
    test_formatter()
