from Common import Login,Request,Assert,read_excel
import allure
import pytest
assertion=Assert.Assertions()
request=Request.Request()
hend=[]
url='http://192.168.1.137:8080/'
param = {'pageNum':'1','pageSize':'5'}
idsList=[]
excel_list = read_excel.read_excel_list('./document/tuihuo.xlsx')
lening = len(excel_list)
for i in range(lening):
    idsList.append(excel_list[i].pop())
tids=0



@allure.feature('订单退货测试')
class Test_sel:
    @allure.story('获取退货订单')
    def test_sel(self):
        global hend
        hend = Login.Login().get_token()
        rest_dic = request.get_request(url=url + 'returnReason/list', params=param, headers=hend)
        rest_add = rest_dic.json()
        assertion.assert_code(rest_dic.status_code,200)
        assertion.assert_in_text(rest_add['message'],'成功')
        add_data_ = rest_add['data']
        data__list_ = add_data_['list']
        iTem = data__list_[0]
        global tids
        tids = iTem['id']

    @allure.story('增加退货订单')
    @pytest.mark.parametrize("name,sort,status,createTime,msg",excel_list,ids=idsList)
    def test_add(self,name,sort,status,createTime,msg):
        json={"name":name,"sort":sort,"status":status,"createTime":createTime}
        post_request = request.post_request(url=url + 'returnReason/create',json=json,headers=hend)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code,200)
        assertion.assert_in_text(request_json['message'],msg)

    @allure.story('删除订单')
    def test_dil(self):
        post_request = request.post_request(url=url + 'returnReason/delete?ids=' + str(tids),headers=hend)
        request_json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(request_json['message'], '成功')


