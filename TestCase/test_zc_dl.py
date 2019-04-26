from Common import Request,Assert,Tools
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()

url='http://192.168.1.137:1811/'



phone= Tools.phone_num()
newphone= Tools.phone_num()
pwd=Tools.random_str_abc(3)+Tools.random_123(3)
newpwd=Tools.random_str_abc(3)+Tools.random_123(3)
rePwd=pwd
userName=Tools.random_str_abc(3)+Tools.random_123(4)
newuserName=Tools.random_str_abc(3)+Tools.random_123(4)



@allure.feature('用户测试')
class Test_zc:
    @allure.story('注册用户')
    def test_zc(self):
        json={"phone": phone, "pwd": pwd,"rePwd": rePwd,"userName": userName}
        post_request = request.post_request(url=url + 'user/signup', json=json)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(request_json['respBase'], '成功')
    @allure.story('冻结用户')
    def test_dj(self):
        post_request = request.post_request(url=url + 'user/lock', params={"userName": userName},
                                            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')

    @allure.story('解除冻结用户')
    def test_jd(self):
        post_request = request.post_request(url=url + 'user/unLock', params={"userName": userName},
                                            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')
    @allure.story('登入用户')
    def test_loign(self):
        json={"pwd":pwd,"userName": userName}
        post_request = request.post_request(url=url + 'user/login', json=json)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')

    @allure.story('修改密码')
    def test_adm(self):
        json={"newPwd":newpwd,"oldPwd": pwd,"reNewPwd": newpwd,"userName":userName}
        post_request = request.post_request(url=url + 'user/changepwd', json=json, )
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')


    @allure.story('登入修改密码后的用户')
    def test_loign(self):
        json = {"pwd": newpwd, "userName": userName}
        post_request = request.post_request(url=url + 'user/login', json=json)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['respDesc'], '成功')






