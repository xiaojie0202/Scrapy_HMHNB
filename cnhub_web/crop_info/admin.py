from django.contrib import admin
from crop_info import models
# Register your models here.


# @admin.register(models.CategoryOne)
# class CategoryOneAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
# @admin.register(models.CategoryTwo)
# class CategoryTwoAdmin(admin.ModelAdmin):
#     list_display = ['name']
#



'''
# 一级分类
class CategoryOne(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')

    def __str__(self):
        return self.name

# 二级分类
class CategoryTwo(models.Model):
    category_one = models.ForeignKey(CategoryOne, verbose_name='所属一级分类')
    name = models.CharField(max_length=64, verbose_name='名称')

    def __str__(self):
        return '%s--->%s' % (self.category_one.name, self.name)
# 三级分类
class CategoryThree(models.Model):
    category_tow = models.ForeignKey(CategoryTwo, verbose_name='所属二级分类')
    name = models.CharField(max_length=64, verbose_name='名称')

    def __str__(self):
        return '%s--->%s--->%s' % (self.category_tow.category_one.name, self.category_tow.name, self.name)


# 商品
class Commodity(models.Model):
    category_three = models.ForeignKey(CategoryThree, verbose_name='所属三级分类')
    name = models.CharField(max_length=128, verbose_name='商品名称')
    price = models.FloatField(verbose_name='价格')
    unit = models.CharField(max_length=32, verbose_name='单位')
    place_of_dispatch = models.CharField(max_length=128, verbose_name='发货地')
    start_wholesale = models.CharField(max_length=64, verbose_name='起批数量')
    specification = models.ManyToManyField('Specification')

    def __str__(self):
        return '%s--%s' % (self.category_three.name, self.name)


# 规格
class Specification(models.Model):
    name = models.CharField(max_length=64, verbose_name='规格名称')
    value = models.CharField(max_length=64, verbose_name='规格值')

# 所有请求的url
class RequestUrl(models.Model):
    url = models.CharField(max_length=256, verbose_name='请求url')


'''