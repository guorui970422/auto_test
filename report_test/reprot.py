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