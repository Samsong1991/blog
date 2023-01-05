# @Time     : 2023/1/5 5:41 下午
# @Author   : Samsong
# @File     : constants.py
# @Description:
class Constant(object):
    ARTICLE_STATUS = (
        ('Draft', '草稿'),
        ('Published', '已发布'),
        ('Deleted', '已删除')
    )
    ARTICLE_STATUS_DELETED = 'Deleted'
    ARTICLE_STATUS_PUBLISHED = 'Published'
    ARTICLE_STATUS_DRAFT = 'Draft'

    GENDERS = (
        ('Male', '男'),
        ('Female', '女'),
        ('Unknown', '未知'),
    )
    GENDERS_UNKNOWN = 'Unknown'
