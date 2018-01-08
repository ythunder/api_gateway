# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from datetime import datetime

class ApiInfo(models.Model):
    api_name = models.CharField(max_length=16)
    api_desc = models.CharField(max_length=256)
    usr_id = models.IntegerField()
    cre_time = models.TimeField(max_length=32)
    upd_time = models.TimeField(max_length=32)
    version = models.CharField(max_length=8)
    status = models.IntegerField()

    def __unicode__(self):
        return u'{%s %s %d %s %s %d' % (self.api_name,
                                          self.api_desc, self.usr_id,
                                          self.cre_time, self.upd_time,
                                          self.status)

    # 插入API接口信息
    @staticmethod
    def insert(name, desc, usrid=1, status=1):
        api_info = ApiInfo()
        api_info.api_name = name
        api_info.api_desc = desc
        api_info.usr_id = usrid
        api_info.cre_time = datetime.now()
        api_info.upd_time = datetime.now()
        api_info.version = None
        api_info.status = status
        api_info.save()
        return True, api_info.id

    # 获取所有数据库中所有API信息
    @staticmethod
    def getAllApiInfo():
        return True, ApiInfo.objects.all()

    #
    @staticmethod
    def getInfoByUsrid(usrid):
        return True, ApiInfo.objects.filter(usr_id = usrid)

    @staticmethod
    def getInfoByStatus(status):
        return True, ApiInfo.objects.filter(status = status)

    @staticmethod
    def getInfoById(id):
        try:
            api_info = ApiInfo.objects.filter(id = id)
        except ApiInfo.DoesNotExist:
            return False, "Not Found!"
        else:
            return api_info

    @staticmethod
    # sign做模糊查询标志
    def getInfoByName(name, sign=0):
        if sign == 0:
            api_info = ApiInfo.objects.filter(api_name__contains=name)
        else:
            api_info = ApiInfo.objects.filter(api_name=name)
        return True, api_info


    @staticmethod
    def update(id,name=None,desc=None,status=None,version=None):
        new = ApiInfo.objects.get(id=id)

        if name is not None:
            new.api_name = name

        if desc is not None:
            new.api_desc = desc

        new.status = 0
        if status == "on":
            new.status = 1

        if version is not None:
            new.version = version

        new.save()
        return True, new

    @staticmethod
    def delete(id):
        exist, api_info = ApiInfo.objects.filter(id=id)
        if not exist:
            return False,"Dose not Found!"
        if exist:
            api_info.delete()
            return True,"delete success"


        return True


class VersInfo(models.Model):
    vers_name = models.CharField(max_length=16)
    api_id = models.IntegerField()
    ser_url = models.URLField()
    auth_type = models.IntegerField()
    status = models.IntegerField()

    @staticmethod
    def getAllVersInfo():
        return True, VersInfo.objects.all()

    @staticmethod
    def getVersByname(name, sign=0):
        if sign == 0:
            vers_info = VersInfo.objects.filter(vers_name__contains=name)
        else:
            vers_info = VersInfo.objects.filter(vers_name=name)
        return vers_info

    @staticmethod
    def getVersById(id):
        try:
            vers_info = VersInfo.objects.filter(id=id)
        except VersInfo.DoesNotExist:
            return False, "Not Found"
        return True, vers_info

    # 插入版本信息
    @staticmethod
    def insert(name, id, url, type, status):
        vers_info = VersInfo()
        vers_info.vers_name = name
        vers_info.api_id = id
        vers_info.ser_url = url
        vers_info.auth_type = type
        vers_info.status = status

        vers_info.save()
        return True, vers_info

    # 更新版本信息
    @staticmethod
    def update(id, name=None, apiId=None, url=None, type=None, status=None):
        new = VersInfo.objects.get(id=id)
        if name is not None:
            new.vers_name = name
        if apiId is not None:
            new.api_id = apiId
        if url is not None:
            new.ser_url = url
        if type is not None:
            if type == "on":
                new.auth_type = 1
            else:
                new.auth_type = 0
        if status is not None:
            if status == "on":
                new.status = 1
            else:
                new.status = 0

        new.save()
        return True, new

    @staticmethod
    def delete(id):
        vers_info = VersInfo.objects.filter(id=id).delete()
        return vers_info



class AclList(models.Model):
    api_id = models.IntegerField()
    vers_id = models.IntegerField()
    match_req = models.CharField(max_length=128)
    auth_type = models.IntegerField()
    cre_time = models.TimeField(max_length=32)
    upd_time = models.TimeField(max_length=32)
    status = models.IntegerField()

    @staticmethod
    def getAllAclInfo():
        return True, AclList.objects.all()

    # sign置0时模糊查询
    @staticmethod
    def getAclByMatch(match_str, sign=0):
        if sign == 0:
            acl_info = AclList.objects.filter(match_req__contains=match_str)
        else:
            acl_info = AclList.objects.get(match_req=match_str)
        return True, acl_info

    @staticmethod
    def getAclById(id):
        exist, acl_info = AclList.objects.get(id=id)
        if exist is True:
            return True, acl_info
        else:
            return False, "Not Found"


    @staticmethod
    def getAclByApiAndVers(apiId, version):
        acl_info = AclList.objects.get(api_id=apiId, version=version)
        return True, acl_info


    @staticmethod
    def insert(api_id, vers_id, match_req, auth_type,status):
        acl_info = AclList()
        acl_info.api_id = api_id
        acl_info.vers_id = vers_id
        acl_info.match_req = match_req
        acl_info.auth_type = auth_type
        acl_info.cre_time = datetime.now()
        acl_info.upd_time = datetime.now()
        acl_info.status = status

        acl_info.save()
        return True, acl_info

    @staticmethod
    def update(id, match_req=None, auth_type=None,status=None):
        new = AclList.objects.get(id=id)

        if match_req is not None:
            new.match_req = match_req

        if auth_type is not None:
            new.auth_type = auth_type

        new.upd_time = datetime.now()

        if status is not None:
            new.status = status

        new.save()
        return True, new

    @staticmethod
    def delete(id):
        AclList.objects.filter(id=id).delete()
        return True


# Create your models here.
