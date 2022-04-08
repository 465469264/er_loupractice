a = {
    "code": "00",
    "body": {
        "data": [
            {
                "stdId": "164881624206606652",
                "stdName": "甘婷婷",
                "learnId": "164881624213834118",
                "pfsnLevel": "1",
                "stdStage": "2",

                "accAmount": "180.00",
                "zmAmount": "0.00",
                "recruitType": "1",
                "unvsName": "amylee成人教育学校",
                "grade": "2022",
                "pfsnName": "amylee成人教育",
                "feeName": "amylee成人教育学校(20222)-2022级-20",
                "offerName": "",
                "stdType": "1",
                "relation": 4,
                "payInfos": [
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "S1",
                        "itemName": "代收第一年书费",
                        "payable": "20.00",
                        "subOrderStatus": "1",
                        "subOrderNo": "7233421262414938225",
                        "orderNum": 2,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "Y1",
                        "itemName": "代收第一年学费",
                        "payable": "20.00",
                        "subOrderStatus": "1",
                        "subOrderNo": "7233421262414938224",
                        "orderNum": 4,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "S2",
                        "itemName": "代收第二年书费",
                        "payable": "20.00",
                        "subOrderStatus": "1",
                        "subOrderNo": "7233421262414938228",
                        "orderNum": 5,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "Y2",
                        "itemName": "代收第二年学费",
                        "payable": "20.00",
                        "subOrderStatus": "1",
                        "subOrderNo": "7233421262414938226",
                        "orderNum": 7,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "S3",
                        "itemName": "代收第三年书费",
                        "payable": "20.00",
                        "subOrderStatus": "1",
                        "subOrderNo": "7233421262414938229",
                        "orderNum": 8,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "Y3",
                        "itemName": "代收第三年学费",
                        "payable": "20.00",
                        "subOrderNo": "7233421262414938227",
                        "orderNum": 10,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "0.00",
                        "feeType": "1"
                    },
                    {
                        "learnId": "164881624213834118",
                        "itemCode": "Y0",
                        "itemName": "考前辅导费",
                        "payable": "20.00",
                        "subOrderStatus": "2",
                        "subOrderNo": "164932167466741402",
                        "orderNum": 103,
                        "feeAmount": "20.00",
                        "offerAmount": "0.00",
                        "payTime": 1649321791000,
                        "payType": 0,
                        "isRefund": 0,
                        "isToUniversity": 0,
                        "toUniversityTimeStr": "",
                        "payAmount": "20.00",
                        "feeType": "1"
                    }
                ],
                "feeId": "164696524049826516",
                "nowFeeId": "164696524049826516",
                "scholarship": "1273",
                "taId": "169",
                "pfsnId": "164690470996983675",
                "createTime": "2022-04-01 20:30:42",
                "feeType": "1",
                "isReturnSchool": 0,
                "tutorPayInfos": [],
                "firstPayInfos": [],
                "secondPayInfos": [],
                "thirdPayInfos": [],
                "otherPayInfos": []
            }
        ],
        "recordsTotal": 1,
        "recordsFiltered": 1
    },
    "msg": ""
}
b = a["body"]["data"][0]["payInfos"][0]["subOrderNo"]

c = a["body"]["data"][0]["payInfos"][1]["subOrderNo"]
d = a["body"]["data"][0]["payInfos"][2]["subOrderNo"]
e = a["body"]["data"][0]["payInfos"][3]["subOrderNo"]
f = a["body"]["data"][0]["payInfos"][4]["subOrderNo"]
g = a["body"]["data"][0]["payInfos"][5]["subOrderNo"]
h = a["body"]["data"][0]["payInfos"][0]["feeAmount"]
i = a["body"]["data"][0]["grade"]
print(b,c,d,e,f,g,h,i)