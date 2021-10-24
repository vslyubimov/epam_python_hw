# тут тоже нет теста, я не разобрался до конца с mock.
# сделаю чуть позднее

# understand how to do Mock testing and do it here
#
# def MyUrlOpenMock():
#     filename = "test_read_website_page.txt"
#     with open(filename, "w") as fp:
#         fp.write("iiii")
#     return mock_open(fp)

# def test_func_wikipedia():
#     with patch('homework4.task02.urlopen') as urlopen_patch:
#         filename = "test_read_website_page.txt"
#
#         with open(filename, "wb") as fp:
#             fp.write(b'iiiiin')
#             urlopen_patch.return_value = open(filename, 'rb')
#             assert count_dots_on_i('website')

# class TestUrlopen(TestCase):
#     @patch('homework4.task02.urlopen')
#     def test_patching(self, Mock_urlopen):
#         filename = "test_read_website_page.txt"
#         func = Mock_urlopen()
#
#         func.read.return_value = b'iiii'
#         with open(filename, "wb") as fp:
#             self.assertEqual(, 4)
# fp.write(b'iiiiin')
# Mock_urlopen.return_value = open(filename, 'rb')
# assert count_dots_on_i('website')

# assert count_dots_on_i('http://foo')


# def test_finc_pythoncom():
#     ...
#
#
# def test_mock():
#     ...
#
#
# def test_something_negative():
#     ...
