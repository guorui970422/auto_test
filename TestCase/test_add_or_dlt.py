from Common import Request,Assert,read_excel
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
Url='http://192.168.1.137:8080/'
head = {}
wpid=0
idsList=[]
excel_list = read_excel.read_excel_list('../document/yhq.xlsx')
lening = len(excel_list)
for i in range(lening):
    idsList.append(excel_list[i].pop())


@allure.feature('商品模块')
class Test_login:
    @allure.story('登入')
    def test_login(self):
        login_resp = request.post_request(url=Url+'admin/login',json={"username": "admin", "password": "123456"})
        resp_dict = login_resp.json()
        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'成功')
        info_data = resp_dict['data']
        token = info_data['token']
        tokenhand = info_data['tokenHead']
        global head
        head = {'Authorization': tokenhand+token}

    @allure.story('获取优惠券')
    def test_youhuiquan(self):
        prent = {'pageNum': '1', 'pageSize': '10'}
        rest_dic = request.get_request(url=Url + 'coupon/list', params=prent, headers=head)
        rest_add = rest_dic.json()
        assertion.assert_code(rest_dic.status_code, 200)
        assertion.assert_in_text(rest_add['message'], '成功')

        dic_data_ = rest_add['data']
        data__list_ = dic_data_['list']
        item = data__list_[0]
        global wpid
        wpid = item['id']
    @allure.story('删除优惠券')
    def test_dil(self):
        post_request = request.post_request(url=Url + 'coupon/delete/' + str(wpid), headers=head)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['message'], '成功')

    @allure.story('添加优惠券')
    @pytest.mark.parametrize("name,amount,minPoint,publishCount,msg",excel_list,ids=idsList)
    def test_add(self,name,amount,minPoint,publishCount,msg):
        json={"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,"minPoint":minPoint,"startTime":'',"endTime":'',
              "useType":0,"note":'',"publishCount":publishCount,"productRelationList":[],"productCategoryRelationList":[]}
        post_request = request.post_request(url=Url + 'coupon/create', json=json, headers=head)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(request_json['message'],msg)
