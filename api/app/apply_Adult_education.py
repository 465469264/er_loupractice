from httprunner import HttpRunner, Config, Step, RunRequest
import os
#APP改名字
class app_Adult_education(HttpRunner):
    config = (
        Config("改名")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{"mobile": "${get_not_exist_mobile()}",
                          "name":"${get_name()}",
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"realName":"$name","android_phoneModel":"SM-N9500","nickname":"zmc_zftmqusy","android_version":"7.18.2","android_sdk":28}}',
                          "data": "${base64_encode($number)}"
                          })
            )
    teststeps = [
        Step(
            RunRequest("注册后修改名字")
                .post("/proxy/us/updateUserInfo/1.0/")
                .with_headers(**{
                                "User-Agent":"Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                                "Content-Type":"text/yzedu+; charset=UTF-8",
                                "Host":"27-app.yzwill.cn",
                                "authtoken":"${ENV(register_auth_token)}",
                                "deviceId":"2a74253c-7c4d-3c84-abb6-e9e72fabb9a1",
                                "Content-Length":"308"
                                })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

#h获取个人信息
class get_inf0(HttpRunner):
    config = (
        Config("登录后获取个人信息")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"android_phoneModel":"SM-N9500","android_version":"7.18.2","android_sdk":28}}',
                          "data": "${base64_encode($number)}"
                          })
    )
    teststeps = [
        Step(
            RunRequest("登录后获取个人信息")
                .post("/proxy/us/userHome/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                # "Host": "27-app.yzwill.cn",
                "Host": "test.yzwill.cn",
                "authtoken": "${ENV(register_auth_token)}",
                "deviceId": "2a74253c-7c4d-3c84-abb6-e9e72fabb9a1",
                "Content-Length": "308"
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body.realName", "realName")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

#获取防重复zmtoken
class get_zmtoken(HttpRunner):
    config = (
        Config("获取zmtoken")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{
            "number": '{"header": {"appType": "3"},'
                      '"body":{"android_phoneModel":"SM-N9500","android_version":"7.18.2","android_sdk":28}}',
            "data": "${base64_encode($number)}"
        })
    )
    teststeps = [
        Step(
            RunRequest("获取zmtoken")
                .post("/proxy/proxy/getCommitToken/1.0/")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                # "Host": "27-app.yzwill.cn",
                "Host": "test.yzwill.cn",
                "authtoken": "${ENV(register_auth_token)}",
                "deviceId": "2a74253c-7c4d-3c84-abb6-e9e72fabb9a1",
                "Content-Length": "308"
            })
                .with_data('$data')
                .extract()
                .with_jmespath("body.body", "zmtoken")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]


#报名成教
class sign_up_education(HttpRunner):
    config = (
        Config("报名成教")
            .base_url("${ENV(app_BASE_URL)}")
            .verify(False)
            .variables(**{"idCard": "${idcard()}",
                          "number": '{"header": {"appType": "3"},'
                                    '"body":{"activeName":"amylee成人教育课程活动","pfsnLevelName":"1\u003e专科升本科类",'
                                    '"android_phoneModel":"SM-N9500","idCard":"$idCard","recruitType":"1","zmtoken":"$zmtoken",'
                                    '"android_version":"7.18.2","android_sdk":28,"unvsName":"amylee成人教育学校","timeStamp":"1648782200963",'
                                    '"pfsnName":"amylee成人教育","taName":"广州南沙","CREATOR":{},"grade":"2022","scholarship":"1273",'
                                    '"name":"$realName","pfsnLevel":"1","unvsId":"164690457468960222","pfsnId":"164690470996983675","taId":"169"}}',
                          "data": "${base64_encode($number)}"
                          })
        )
    teststeps = [
        Step(
            RunRequest("报名成教")
                .post("/proxy/mkt/enroll/1.0/ ")
                .with_headers(**{
                "User-Agent": "Android/environment=test/app_version=7.18.2/sdk=28/dev=samsung/phone=SM-N9500/android_system=9",
                "Content-Type": "text/yzedu+; charset=UTF-8",
                # "Host": "27-app.yzwill.cn",
                "Host": "test.yzwill.cn",
                "authtoken": "${ENV(register_auth_token)}",
                "deviceId": "2a74253c-7c4d-3c84-abb6-e9e72fabb9a1",
                "Content-Length": "308"
            })
                .with_data('$data')
                .validate()
                .assert_equal("status_code", 200)
        )
    ]


# if __name__ == '__main__':
#     sign_up_education().test_start()