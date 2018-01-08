# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from datetime import datetime

from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from gateway.models import ApiInfo, VersInfo, AclList

# 主页面
def homePage(request):
    return render_to_response('index.html')

# 添加api接口页面
def addApiView(request):
    return render_to_response('api_add.html')


# 添加版本信息页面
def addVersView(request):
    flag ,results = ApiInfo.getAllApiInfo()
    return render_to_response('version_add.html', {'results':results})

#添加ACL信息页面
def addAclView(request):
    flag, api_list = ApiInfo.getAllApiInfo()

    if 'id' in request.GET and request.GET['id']:
        api_id = int (request.GET['id'])
        version_list = VersInfo.objects.filter(api_id=api_id)
        return render_to_response('acl_add.html',{'api_list':api_list,'version_list':version_list,'acl_api_id':api_id})
    else:
        return render_to_response('acl_add.html',{'api_list':api_list})

# 添加新API接口信息
def insertApiInfo(request):
    api_name = request.GET['api-name']
    api_desc = request.GET['description']
    status = request.GET['status']

    # 有效性检查
    if status is not "on":
        status = 0
        ApiInfo.insert(name=api_name,desc=api_desc, status=status)

    # status为on时，model层默认为1
    ApiInfo.insert(name=api_name, desc=api_desc)
    flag, result = ApiInfo.getAllApiInfo()
    if flag:
        return render_to_response('api_view.html', {'results':result})



#添加新版本信息
@csrf_protect
def insertVersInfo(request):
    vers_name = request.GET['version-name']
    api_id = request.GET['api']
    ser_url = request.GET['version_uri']
    auth_type = request.GET['auth_type']
    status = request.GET['status']

    if auth_type == "on":
        auth_type = 1
    else:
        auth_type = 0

    if status == "on":
        status = 1
    else:
        status = 0

    VersInfo.insert(name=vers_name,id=api_id,url=ser_url,type=auth_type,status=status)

    flag,res_vers = VersInfo.getAllVersInfo()
    if flag:
        return render_to_response('version_view.html', {'res_vers':res_vers}, context_instance=RequestContext(request))


def insertAclInfo(request):
    vers_id = int(request.GET['vers_id'])
    api_id = int(request.GET['api_id'])
    match_req = None
    if 'expression' in request.GET:
        match_req = request.GET['expression']

    auth_type = request.GET['auth_type']
    if auth_type == "on":
        auth_type = 1
    else:
        auth_type = 0

    status = request.GET['status']
    if status == "on":
        status = 1
    else:
        status = 0

    AclList.insert(api_id=api_id,vers_id=vers_id,match_req=match_req,
                   auth_type=auth_type,status=status)

    flag, res_acl = AclList.getAllAclInfo()
    if flag:
        return render_to_response('acl_view.html', {'result':res_acl})


# 删除API接口信息，将status改为0ting
def deleteApiInfo(request):
    api_id = request.GET['id']
    ApiInfo.objects.filter(id=api_id).delete()

    # 打印api接口信息
    flag, result = ApiInfo.getAllApiInfo()
    if flag:
        return render_to_response('api_view.html', {'results': result})


def deleteVersInfo(request):
    vers_id = request.GET['id']
    VersInfo.objects.filter(id=vers_id).delete()

    flag, res_vers = VersInfo.getAllVersInfo()
    if flag:
        return render_to_response('version_view.html', {'res_vers': res_vers})

def deleteAclInfo(request):
    acl_id = request.GET['id']
    AclList.objects.filter(id=acl_id).delete()

    flag, res_acl = AclList.getAllAclInfo()
    if flag:
        return render_to_response('acl_view.html', {'result': res_acl})


# 更改API接口信息
def updateApiInfo(request):
    api_id = request.GET['id']
    result = ApiInfo.objects.filter(id = api_id)
    for api_info in result:
        name_info = api_info.api_name
        desc_info = api_info.api_desc
    return render_to_response('api-edit.html', {'name':name_info, 'desc':desc_info, 'id':api_id })


def updateVersInfo(request):
    vers_id = request.GET['id']
    result = VersInfo.objects.filter(id = vers_id)

    for vers_info in result:
        api_id = vers_info.api_id
        vers_name = vers_info.vers_name
        ser_url = vers_info.ser_url

    return render_to_response('vers-edit.html', {'api_id':api_id, 'vers_name':vers_name, 'ser_url':ser_url, 'id':vers_id})



def updateAclInfo(request):
    acl_id = request.GET['id']
    result = AclList.objects.get(id=acl_id)

    match_req = result.match_req
    return render_to_response('acl-edit.html',{'match':match_req, 'id':acl_id })



#提交更新后的api信息
def commitApiInfo(request, id):
    api_id = int(id)
    api_name = request.GET['api-name']
    api_desc = request.GET['description']
    api_version = request.GET['version']
    status = request.GET['status']

    # 更新
    ApiInfo.update(id=api_id, name=api_name, desc=api_desc, version=api_version)

    # 更新后信息
    result_list = ApiInfo.objects.all()
    return render_to_response('api_view.html', {'results': result_list})


def commitVersInfo(request, id):
    vers_id = int(id)
    vers_name = request.GET['version-name']
    api_id = request.GET['api']
    ser_url = request.GET['version_uri']

    auth_type = None
    if 'auth_type' in request.GET:
        auth_type = request.GET['auth_type']

    status = None
    if 'status' in request.GET:
        status = request.GET['status']

    VersInfo.update(id=vers_id,name=vers_name,apiId=api_id,url=ser_url,type=auth_type,status=status)

    flag, res_vers = VersInfo.getAllVersInfo()
    if flag:
        return render_to_response('version_view.html', {'res_vers': res_vers})

def commitAclInfo(request, id):
    acl_id = int(id)
    match_req = None
    if 'expression' in request.GET:
        match_req = request.GET['expression']

    auth_type = request.GET['auth_type']
    if auth_type == "on":
        auth_type = 1
    else:
        auth_type = 0

    status = request.GET['status']
    if status == "on":
        status = 1
    else:
        status = 0

    AclList.update(acl_id,match_req=match_req,auth_type=auth_type,status=status)

    flag, res_acl = AclList.getAllAclInfo()
    if flag:
        return render_to_response('acl_view.html', {'result':res_acl})

# 陈列API接口信息
def disApiInfo(request):
    # 查询数据表中所有数据
    # 将数据弄进api_view.html页面
    # 返回api_view.html页面
    result_list = ApiInfo.objects.all()
    return render_to_response('api_view.html',{'results':result_list})


def disVersInfo(request):
    flag, res_vers = VersInfo.getAllVersInfo()
    #res_vers = VersInfo.objects.filter(api_id=1)
    if flag:
        return render_to_response('version_view.html', {'res_vers': res_vers})


def disAclInfo(request):
    flag, res_acl = AclList.getAllAclInfo()
    if flag:
        return render_to_response('acl_view.html', {'result':res_acl})

# Create your views here.
