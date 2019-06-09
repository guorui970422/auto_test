from Common import Request,Assert
import allure
import pytest

request = Request.Request()
assertions = Assert.Assertions()
Url='http://192.168.1.104:8080/'
head = {}
jk_id = []
sp_id = []
@allure.feature('营销模块')
class Test_jk():

    @allure.story('登录')
    def test_a(self):
        post_request = request.post_request(url=Url+'admin/login', json={"username": "admin", "password": "123456"})
        dict_request = post_request.json()
        assertions.assert_code(post_request.status_code,200)
        assertions.assert_in_text(dict_request['message'],'成功')
        request_data = dict_request['data']
        token_ = request_data['token']
        tokenhead=request_data['tokenHead']
        global head
        head={'Authorization':tokenhead+token_}


    @allure.story('秒杀活动页面')
    def test_b(self):
        yemian = {'pageNum':1,'pageSize':5}
        get_request = request.get_request(url=Url + 'flash/list?', params=yemian, headers=head)
        request_json = get_request.json()
        assertions.assert_code(get_request.status_code, 200)
        assertions.assert_in_text(request_json['message'], '成功')


    @allure.story('添加活动')
    def test_c(self):
        rep={'endDate': "2019-06-10",'nullstartDate': "2019-06-08",'status': 1,'title': "大海你全是水"}
        request_post_request = request.post_request(url=Url + 'flash/create', json=rep, headers=head)
        request_json = request_post_request.json()
        assertions.assert_code(request_post_request.status_code, 200)
        assertions.assert_in_text(request_json['message'],'成功')

    @allure.story('查询')
    def test_d(self):
        yemian = {'pageNum': 1, 'pageSize': 5,'keyword':'水'}
        get_request = request.get_request(url=Url + 'flash/list?', params=yemian, headers=head)
        request_json = get_request.json()
        assertions.assert_code(get_request.status_code, 200)
        assertions.assert_in_text(request_json['message'], '成功')
        json_data_ = request_json['data']
        print(json_data_)
        data__list_ = json_data_['list']
        list__id_ = data__list_[0]
        global sp_id
        sp_id=list__id_['id']
        print(sp_id)

    @allure.story('修改')
    def test_e(self):
        rep={'createTime': 1560051381000,'endDate': "2019-06-25",
                'startDate': "2019-06-08",
                'status': 2,
                'title': "海你全是水"}
        post_request = request.post_request(url=Url + 'flash/update/'+str(sp_id), json=rep, headers=head)
        request_json = post_request.json()
        assertions.assert_code(post_request.status_code, 200)
        assertions.assert_in_text(request_json['message'], '成功')

    @allure.story('查询')
    def test_f(self):
        yemian = {'pageNum': 1, 'pageSize': 5, 'keyword': '水'}
        get_request = request.get_request(url=Url + 'flash/list?', params=yemian, headers=head)
        request_json = get_request.json()
        assertions.assert_code(get_request.status_code, 200)
        assertions.assert_in_text(request_json['message'], '成功')

    @allure.story('删除')
    def test_g(self):
        post_request = request.post_request(url=Url + 'flash/delete/' + str(sp_id), headers=head)
        request_json = post_request.json()
        assertions.assert_code(post_request.status_code,200)
        assertions.assert_in_text(request_json['message'],'成功')


