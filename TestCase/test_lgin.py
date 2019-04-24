from Common import Request,Assert
import allure

request = Request.Request()
assertion = Assert.Assertions()

@allure.feature('登入功能测试')
class Test_login:
    @allure.story('登入测试1')
    def test_login(self):

        login_resp = request.post_request(url='http://192.168.1.137:8080/admin/login',json={"username": "admin", "password": "123456"})

        resp_test = login_resp.text
        print(resp_test)

        resp_dict = login_resp.json()
        print(resp_test)

        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')


