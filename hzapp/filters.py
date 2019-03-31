#!/usr/bin/env python
# -*- coding: utf-8 -*-
import django_filters
from django.contrib.auth.models import User
from django.db.models import Q
class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户实体过滤器
    """
    username = django_filters.CharFilter(field_name='username')

    class Meta:
        model = User
        fields = ['username', ]

# class equipment_tableFilter(django_filters.rest_framework.FilterSet):
    # """
   # 站点实体过滤器
    # """
    # user_id = django_filters.CharFilter(name='user_id')

    # class Meta:
        # model = equipment_table
        # fields = ['user_id', ]
#
