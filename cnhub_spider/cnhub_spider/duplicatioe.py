from crop_info import models
class MyDupeFilter(object):

    @classmethod
    def from_settings(cls, settings):  # Scrapy内部会通过此方法创建对象
        return cls()

    def request_seen(self, request):
        url_db = models.RequestUrl.objects.filter(url=request.url).count()
        if url_db != 0:
            return True
        models.RequestUrl.objects.create(url=request.url)
        return False
        # if request.url in self.url_set:
        #     return True
        # self.url_set.add(request.url)
        # return False

    def open(self):  # 爬虫开始的时候会调用openj方法
        pass

    def close(self, reason):  # 爬虫关闭的时候会执行close方法
        pass

    def log(self, request, spider):  # 每一次请求都会调用log
        pass