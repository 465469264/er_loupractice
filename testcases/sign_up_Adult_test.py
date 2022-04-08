from api.app.register_app_test import register
from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.app.apply_Adult_education import app_Adult_education,get_inf0,get_zmtoken,sign_up_education


class TestCase_sign_up_adult(HttpRunner):
    config = (
        Config("APP报名成教")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            )
    teststeps = [
        Step(RunTestCase("注册后登录改名").call(app_Adult_education)),
        Step(RunTestCase("获取个人信息").call(get_inf0).export(*["realName"])),
        Step(RunTestCase("获取报名zmtoken").call(get_zmtoken).export(*["zmtoken"])),
        Step(RunTestCase("报名成教").call(sign_up_education)),
    ]
if __name__ == '__main__':
    register().register1()
    TestCase_sign_up_adult().test_start()