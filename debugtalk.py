import time,base64,random,requests,json
from faker import Faker
from httprunner import __version__
from har.sql_statement import conn_sql
f = Faker(locale='zh_CN')
import re
def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


# 接口数据加密
def base64_encode(code):
    data = base64.b64encode(str(code).encode()).decode()
    # print(data)
    return data


# 获取随机手机号码
def get_mobile():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return str(random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8)))


# 获取未注册的随机手机号码
def get_not_exist_mobile():
    while True:
        mobile = get_mobile()
        data = {"mobile": mobile}
        response = requests.post("http://bms.yzwill.cn/recruit/getStudentInfoByMobile", data=data)
        result = response.text
        if result == '{"code":"00","body":null,"msg":"","ok":true}':
            return mobile
        else:
            continue
a = get_not_exist_mobile()
# 随机生成姓名
def get_name():
    """随机生成姓名"""
    return f.name()

# 生成身份证
def idcard():
    """生成身份证"""
    return f.ssn()
#缴费单
def feeList():
    feeList=[{"itemCode":"Y1","itemName":"代收第一年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"2","itemYear":"1","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S1","itemName":"代收第一年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"3","itemYear":"1","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y2","itemName":"代收第二年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"5","itemYear":"2","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S2","itemName":"代收第二年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"6","itemYear":"2","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"Y3","itemName":"代收第三年学费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"8","itemYear":"3","itemType":"2","feeId":None,"itemSeq":None},{"itemCode":"S3","itemName":"代收第三年书费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"9","itemYear":"3","itemType":"4","feeId":None,"itemSeq":None},{"itemCode":"YS","itemName":"代收艺术加考费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"100","itemYear":"1","itemType":"3","feeId":None,"itemSeq":None},{"itemCode":"Y0","itemName":"考前辅导费","amount":"20.00","discount":"0.00","fdId":None,"odId":None,"payable":"20.00","discountType":None,"orderNum":"103","itemYear":"0","itemType":"1","feeId":None,"itemSeq":None}]
    return feeList


#获取web_token
def get_html(body):
    pattern = re.compile(r'value="(.+)" name="_web_token"')  # 查找数字
    body = str(body, encoding="utf-8")
    a = pattern.findall(body)
    print(type(a))
    return a[0]

#执行生成学院订单
def College_order(learn_Id):
    sql = 'INSERT INTO pay.bd_sub_order (sub_order_no,order_no,item_code,item_name,item_seq,item_year,item_type,fee_amount,offer_amount,payable,sub_order_status,std_id,std_name,mobile,id_card,user_id,sub_learn_id ) SELECT bms.seq (),' \
          'CONCAT( "YZ", DATE_FORMAT( NOW(), "%Y%m%d%H%i%s" ), "12378"),it.item_code,it.item_name,it.delay_num,it.item_year,it.item_type,f.define_amount,0.00,f.define_amount,"1",li.std_id,li.ln_std_name,li.mobile,li.id_card,si.user_id,' \
          'li.learn_id FROM bms.bd_fee_define f LEFT JOIN bms.bd_learn_info li ON li.fee_id = f.fee_id LEFT JOIN bms.bd_fee_item it ON it.item_code = f.item_code LEFT JOIN bms.bd_student_info si ON si.std_id = li.std_id WHERE li.learn_id = "{}"'.format(learn_Id)
    data = conn_sql().get_data(sql)
    return data
# College_order('164880778923176371')

#执行删除生成多的最后两条订单
def delete_order(learnId):
    sql = 'delete from pay.bd_sub_order where sub_order_no in (select t.sub_order_no from (select * from pay.bd_sub_order where sub_learn_id = "{}" order by sub_order_no desc limit 0,2)as t)'.format(learnId)
    data = conn_sql().get_data(sql)
    return data
# delete_order('164881624213834118')