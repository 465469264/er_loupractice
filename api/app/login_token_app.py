import requests
import base64
import json
import os

from httprunner.loader import load_dot_env_file
def w_env(login_token,auth_token):
    """
    更新后台的authtoken，减少登录操作
    :param authtoken:
    :return:
    """
    file_dir = os.path.abspath('../..')  # 获取上级路径
    dot_env_path = os.path.join(file_dir, ".env")
    dot_env = load_dot_env_file(dot_env_path)
    dot_env.update({'login_token': login_token})
    dot_env.update({'auth_token': auth_token})
    print(dot_env)
    with open(dot_env_path, "w") as f:
        for k, v in dot_env.items():
            k_v = k + '=' + str(v)
            f.write(k_v)
            f.write('\n')

if __name__ == '__main__':
    s = requests.Session()
    app_url = "http://test.yzwill.cn/proxy/us/loginOrRegister/1.0/"
    headers = {
        "User-Agent": "Android/environment=test/app_version=7.18.1/sdk=30/dev=samsung/phone=SM-G988U/android_system=.env",
        "Content-Type": "base64.b64encode",
        "Host": "test.yzwill.cn"}
    data = base64.b64encode(json.dumps(dict(body={"mobile": "13832198240",
                                                  "valicode": "888888", "regChannel": "6"},
                                            header={"appType": "4"})).encode("utf-8"))
    r = s.post(url=app_url,data = data ,headers=headers, verify=False)
    dictJson = r.json()
    print(dictJson)
    token1= dictJson["body"]["app_auth_token"]
    token2= dictJson["body"]["auth_token"]
    login_token =token1
    auth_token =token2
    w_env(login_token,auth_token)