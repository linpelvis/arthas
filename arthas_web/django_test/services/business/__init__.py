from arthas_web.django_test.services import TestServiceBase

class TestBase(TestServiceBase):
    def setup(self):
        pass

    def setUp(self):
        TestServiceBase.setUp(self)
        # use sync mode for test
        pass

    def tearDown(self):
        TestServiceBase.tearDown(self)

    def assertStatus200(self, response):
        self.assertTrue(response.status_code == 200,
                        'post status code must be 200, not %s'%response.status_code)

