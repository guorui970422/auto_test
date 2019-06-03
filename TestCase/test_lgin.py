from Common import Request,Assert
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
Url='http://192.168.1.137:8080/'
head = {}

@allure.feature('登入功能测试')
class Test_login:
    @allure.story('登入测试1')
    def test_login(self):

        login_resp = request.post_request(url=Url+'admin/login',json={"username": "admin", "password": "123456"})

        resp_test = login_resp.text
        print(resp_test)

        resp_dict = login_resp.json()
        print(resp_test)

        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')

        info_data = resp_dict['data']
        token = info_data['token']
        tokenhand = info_data['tokenHead']
        global head
        head = {'Authorization': tokenhand+token}

    @allure.story('获取用户信息')
    def test_info(self):

        get_info = request.get_request(url=Url + 'admin/info', headers=head)
        info_json = get_info.json()
        assertion.assert_code(get_info.status_code,200)
        assertion.assert_in_text(info_json['message'],'成功')

    @allure.story("测试登录")
    @pytest.mark.parametrize("username,password,msg",
                             [['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误'],
                              ['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误']])
    def info_long(self,username,password,msg):
        loing_test = request.post_request(url=Url + 'admin/info', json={"username":username, "password":password})

        loing_test = loing_test.text
        long_json = loing_test.json()
        assertion.assert_code(loing_test.status_code, 200)
        assertion.assert_in_text(long_json['message'], msg)






