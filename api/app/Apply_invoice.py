from httprunner import HttpRunner, Config, Step, RunRequest

class Adult_education(HttpRunner):
    config = (
        Config("申请个人发票")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{"mobile": "${ENV(login_mobile)}"})
            )
    teststeps = [
        Step(
            RunRequest("查询学员")
                .post("/proxy/bds/myApplyType/1.0/ ")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data({"recruitType": "1",
                            "loginName": "彭正",
                            "operatorId": "160255473873614461",
                            "mobile": "13381264851"})

                .validate()
                .assert_equal("status_code", 200)
        )

    ]
if __name__ == '__main__':
    Adult_education().test_start()