from httprunner import HttpRunner, Config, Step, RunRequest
import re
#查询考前辅导费缴费列表
class querry(HttpRunner):
    config = (
        Config("查询辅导费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询学员")
                .post("/stdFee/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data({"mobile": "${ENV(register_mobile)}"})
                .extract()
                .with_jmespath("body.body.data[0].learnId", "learnId")
                .with_jmespath("body.body.data[0].learnId", "learn_Id")
                .with_jmespath("body.body.data[0].payInfos[0].subOrderNo", "subOrderNo")
                .with_jmespath("body.body.data[0].grade", "grade")
                .with_jmespath("body.body.data[0].payInfos[0].feeAmount", "feeAmount")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]

#查询学院订单
class querry2(HttpRunner):
    config = (
        Config("查询学院订单")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
            )
    teststeps = [
        Step(
            RunRequest("查询学员")
                .post("/stdFee/list.do")
                .with_headers(**{
                "Content - Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"${ENV(COOKIE)}"
            })
                .with_data({"mobile": "${ENV(register_mobile)}"})
                .extract()
                .with_jmespath("body.body.data[0].learnId", "learnId")
                .with_jmespath("body.body.data[0].learnId", "learn_Id")
                .with_jmespath("body.body.data[0].payInfos[0].subOrderNo", "subOrderNo1")
                .with_jmespath("body.body.data[0].payInfos[1].subOrderNo", "subOrderNo2")
                .with_jmespath("body.body.data[0].payInfos[2].subOrderNo", "subOrderNo3")
                .with_jmespath("body.body.data[0].payInfos[3].subOrderNo", "subOrderNo4")
                .with_jmespath("body.body.data[0].payInfos[4].subOrderNo", "subOrderNo5")
                .with_jmespath("body.body.data[0].payInfos[5].subOrderNo", "subOrderNo6")
                .with_jmespath("body.body.data[0].grade", "grade")
                .with_jmespath("body.body.data[0].payInfos[0].feeAmount", "feeAmount")
                .validate()
                .assert_equal("status_code", 200)
        )
    ]
# 获取webtoken
class web_token(HttpRunner):
    config = (
        Config("获取webtoken")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("获取webtoken")
                .post("/stdFee/toPay.do")
                .with_headers(**{
                "Accept":"*/*",
                "User-Agent":"PostmanRuntime/7.28.4",
                "Accept-Encoding":"gzip, deflate, br",
                "Connection":"keep-alive",
                "Cookie": "${ENV(COOKIE)}"
            })
                .with_data({"learnId": "$learnId"})
                .extract()
                .with_jmespath("body","body") #获取body
        )
    ]

#缴辅导费
class pay_fee(HttpRunner):
    config = (
        Config("缴辅导费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("缴费")
                # .setup_hook('${get_html($body)}', "web_token")
                .post("/stdFee/pay.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "bms.yzwill.cn",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "${ENV(COOKIE)}"
                            })
                .with_data(
                {
                    "_web_token": "$_web_token",
                    "learnId": "$learnId",
                    "grade": "$grade",
                    "years": "0",
                    "itemCodes": "Y0",
                    "accDeduction": "0.00",
                    "couponsStr": "[]",
                    "zmDeduction": "0",
                    "payableCount": "$feeAmount",
                    "paymentType": "1",
                    "remark": "只缴费Y0",
                    "payData": '{"learnId":"$learnId","paymentType":"1","tradeType":"NATIVE","accDeduction":"0.00","zmDeduction":"0","coupons":"[]","items":"[{\\"orderNo\\":\\"$subOrderNo\\",\\"itemCode\\":\\"Y0\\",\\"itemName\\":\\"考前辅导费\\",\\"itemYear\\":\\"0\\",\\"amount\\":\\"$feeAmount\\",\\"accScale\\":0,\\"zmScale\\":0,\\"couponScale\\":0,\\"payAmount\\":\\"$feeAmount\\"}]","dataSources":"5","grade":"$grade","payAmount":"$feeAmount","remark":"只缴费Y0"}',
                }
                            )

                .validate()
                .assert_equal("status_code", 200)
        )
]

#缴学院订单
class pay_fee2(HttpRunner):
    config = (
        Config("缴费")
            .base_url("${ENV(BASE_URL)}")
            .verify(False)
            .variables()
    )
    teststeps = [
        Step(
            RunRequest("缴学院订单")
                # .setup_hook('${get_html($body)}', "web_token")
                .post("/stdFee/pay.do")
                .with_headers(**{
                "Content - Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content - Length": "246",
                "Host": "bms.yzwill.cn",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "${ENV(COOKIE)}",
                "X-Requested-With": "XMLHttpRequest",
                "sendTime": "1649334973077",
                "transferSeq": "1",
                "uri": "http://bms.yzwill.cn/stdFee/toPay.do?learnId=$learnId",
                            })
                .with_data(
                # {
                #     "_web_token": "$_web_token",
                #     "learnId": "$learnId",
                #     "grade": "$grade",
                #     "years": "1",
                #     "itemCodes": "S1",
                #     "itemCodes": "Y1",
                #     "years": "2",
                #     "itemCodes": "S2",
                #     "itemCodes": "Y2",
                #     "years": "3",
                #     "itemCodes": "S3",
                #     "itemCodes": "Y3",
                #     "accDeduction": "0.00",
                #     "couponsStr": "[]",
                #     "zmDeduction": "0",
                #     "payableCount": "120.00",
                #     "paymentType": "1",
                #     "remark:"
                #     "payData": '{"learnId":"$learnId","paymentType":"1","tradeType":"NATIVE","accDeduction":"0.00","zmDeduction":"0","coupons":"[]","items":"[{\"orderNo\":\"$subOrderNo1\",\"itemCode\":\"S1\",\"itemName\":\"代收第一年书费\",\"itemYear\":\"1\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo2\",\"itemCode\":\"Y1\",\"itemName\":\"代收第一年学费\",\"itemYear\":\"1\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo3\",\"itemCode\":\"S2\",\"itemName\":\"代收第二年书费\",\"itemYear\":\"2\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo4\",\"itemCode\":\"Y2\",\"itemName\":\"代收第二年学费\",\"itemYear\":\"2\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo5\",\"itemCode\":\"S3\",\"itemName\":\"代收第三年书费\",\"itemYear\":\"3\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo6\",\"itemCode\":\"Y3\",\"itemName\":\"代收第三年学费\",\"itemYear\":\"3\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"}]","dataSources":"5","grade":"$grade","payAmount":"120.00","remark":""}',
                # }
                    {
                        "_web_token": "$_web_token",
                        "accDeduction": "0.00",
                        "couponsStr": "[]",
                        "grade": "2022",
                        "itemCodes": "Y3",
                        "learnId": "$learnId",
                        "payData": '{"learnId":"$learnId","paymentType":"1","tradeType":"NATIVE","accDeduction":"0.00","zmDeduction":"0","coupons":"[]","items":"[{\"orderNo\":\"$subOrderNo1\",\"itemCode\":\"S1\",\"itemName\":\"代收第一年书费\",\"itemYear\":\"1\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo2\",\"itemCode\":\"Y1\",\"itemName\":\"代收第一年学费\",\"itemYear\":\"1\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo3\",\"itemCode\":\"S2\",\"itemName\":\"代收第二年书费\",\"itemYear\":\"2\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo4\",\"itemCode\":\"Y2\",\"itemName\":\"代收第二年学费\",\"itemYear\":\"2\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo5\",\"itemCode\":\"S3\",\"itemName\":\"代收第三年书费\",\"itemYear\":\"3\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"},{\"orderNo\":\"$subOrderNo6\",\"itemCode\":\"Y3\",\"itemName\":\"代收第三年学费\",\"itemYear\":\"3\",\"amount\":\"$feeAmount\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"$feeAmount\"}]","dataSources":"5","grade":"$grade","payAmount":"120.00","remark":""}',
                        "payableCount": "120.00",
                        "paymentType": "1",
                        "remark": "",
                        "years": "3",
                        "zmDeduction": "0",
                    }
                                        )

                .validate()
                .assert_equal("status_code", 200)
        )
]

if __name__ == '__main__':
    pay_fee2().test_start()
