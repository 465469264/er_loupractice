from api.web.login_web_test import login
from httprunner import HttpRunner, Config, Step, RunRequest,RunTestCase
from api.web.Adult_education_pay_fee import querry,querry2,pay_fee,pay_fee2,web_token

class Pay_fee(HttpRunner):
    config = (
        Config("缴费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            )
    teststeps = [
        # 缴费辅导费,并生成学院订单
        # Step(RunTestCase("获取缴费信息,生成学院订单").call(querry).teardown_hook('${College_order($learn_Id)}',"learn_Id").export(*["learnId","learn_Id","subOrderNo","grade","feeAmount"])),
        # Step(RunTestCase("获取缴费web_token").call(web_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        # Step(RunTestCase("缴辅导费").call(pay_fee)),
        #删除没用的学院订单,缴费学院订单
        Step(RunTestCase("获取缴费信息").call(querry2).teardown_hook('${delete_order($learn_Id)}', "learn_Id").export(*["learnId","subOrderNo1","subOrderNo2","subOrderNo3","subOrderNo4","subOrderNo5","subOrderNo6","grade","feeAmount"])),
        Step(RunTestCase("获取缴费信息").call(web_token).teardown_hook('${get_html($body)}', "_web_token").export(*["_web_token"])),
        Step(RunTestCase("缴学院订单费").call(pay_fee2)),




    ]



if __name__ == '__main__':
    # login().login()
    Pay_fee().test_start()