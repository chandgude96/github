class Test_mul:
    def test_mul_01(self):
        a = 9
        b = 7
        mul = a * b
        print("the mul of a and b is:",mul)
        if mul == 63:
            assert True
        else:
            assert False