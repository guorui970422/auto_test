# from Common import Request,Assert
# import allure
# import pytest
# request = Request.Request()
# assertion = Assert.Assertions()
# Url='http://192.168.1.137:8080/'
# head = {}
# sku_id = []
# @allure.feature('商品模块')
# class Test_login:
#     @allure.story('登入')
#     def test_login(self):
#         login_resp = request.post_request(url=Url+'admin/login',json={"username": "admin", "password": "123456"})
#         resp_dict = login_resp.json()
#         assertion.assert_code(login_resp.status_code,200)
#         assertion.assert_in_text(resp_dict['message'],'成功')
#         info_data = resp_dict['data']
#         token = info_data['token']
#         tokenhand = info_data['tokenHead']
#         global head
#         head = {'Authorization': tokenhand+token}
#     @allure.story('获取商品分类信息')
#     def test_get(self):
#         yemian =  {'pageNum' : '1' , 'pageSize' : '10'}
#         get_request = request.get_request(url=Url + 'productCategory/list/0', params=yemian, headers=head)
#         json_sku = get_request.json()
#         assertion.assert_code(get_request.status_code, 200)
#         assertion.assert_in_text(json_sku['message'], '成功')
#         json_data = json_sku['data']
#         list_data = json_data['list']
#         sku_list = list_data[0]
#         global sku_id
#         sku_id=sku_list['id']
#     @allure.story('删除商品分类')
#     def test_skr(self):
#         dely_sku = request.post_request(url=Url + 'productCategory/delete/' + str(sku_id), headers=head)
#         dict_json = dely_sku.json()
#         assertion.assert_code(dely_sku.status_code, 200)
#         assertion.assert_in_text(dict_json['message'], '成功')
#     @allure.story('添加商品')
#     def test_sp_add(self):
#         req_eq = {'description': "", 'icon': "", 'keywords': "",'name': "兰博激你", 'navStatus': 0, 'parentId': 0, 'productUnit': ""}
#
#         add_post = request.post_request(url=Url + 'productCategory/create', json=req_eq ,headers=head)
#         add_json = add_post.json()
#         assertion.assert_code(add_post.status_code, 200)
#         assertion.assert_in_text(add_json['message'],'成功' )
#     @allure.story('添加商品2')
#     @pytest.mark.parametrize('name',["兰博激你"])
#     def test_add2(self,name):
#         req_eq = {'description': "", 'icon': "", 'keywords': "", 'name': name, 'navStatus': 0, 'parentId': 0,
#                   'productUnit': ""}
#         add_post = request.post_request(url=Url + 'productCategory/create',  json=req_eq , headers=head)
#         add_json = add_post.json()
#         assertion.assert_code(add_post.status_code, 200)
#         assertion.assert_in_text(add_json['message'],'成功' )
#     @allure.story('获取优惠券')
#     def test_youhuiquan(self):
#         prent = {'pageNum':'1','pageSize':'10'}
#         rest_dic = request.get_request(url=Url + 'coupon/list', params=prent,headers=head)
#         rest_add = rest_dic.json()
#         assertion.assert_code(rest_dic.status_code, 200)
#         assertion.assert_in_text(rest_add['message'], '成功')
#     @allure.story('添加优惠券')
#     @pytest.mark.parametrize('name',['张三','李四','周龙','张官100'],ids=['第一次','第二次','第三次','第四次'])
#     def test_addyhq(self,name):
#         req={'amount':100,'endTime': '','minPoint': 100,'name':name,'note': '','perLimit': 1,'platform': 0,
#              'productCategoryRelationList': [],'productRelationList': [],'publishCount':100,'startTime': '','type': 0,'useType': 0}
#         post_request = request.post_request(url=Url + 'coupon/create', json=req, headers=head)
#         request_json = post_request.json()
#         assertion.assert_code(post_request.status_code, 200)
#         assertion.assert_in_text(request_json['message'], '成功')
#
#
