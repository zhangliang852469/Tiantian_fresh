from django.db import models
from db.basemodel import BaseModel

# 商品表：商品SPU表、首页轮播商品表、商品种类表、首促销活动表、首页分类商品表、商品图片表、商品SKU表,其中SPU指商品
# 不包括规格， SKU指具体规格的商品


class GoodsType(BaseModel):
    """商品种类"""
    name = models.CharField(max_length=20, verbose_name='商品种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='种类图片')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

class GoodsSPU(BaseModel):
    """商品SPU表"""
    name = models.CharField(max_length=20, verbose_name='SPU名称')
    detail = models.HTMLField(blak=True, verbose_name='商品描述')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'df_goods_SPU'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

class GoodsSKU(BaseModel):
    """商品SKU表"""
    status_choices = (
        (0, '下架'),
        (1, '上架'),
    )

    name = models.CharField(max_length=20, verbose_name='商品SKU名称')
    desc = models.CharField(max_length=258, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unit = models.CharField(max_length=20, verbose_name='单位')
    stock = models.IntegerField(default=1, verbose_name="商品库存")
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    image = models.ImageField(upload_to='goods', verbose_name='图片')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')

    type_id = models.ForeignKey('GoodsType', verbose_name='商品类型')
    spu_id = models.ForeignKey('GoodsSPU', verbose_name='商品SPU')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'df_goods_sku'
        verbose_name = '商品SKU名称'
        verbose_name_plural = verbose_name

class GoodsImage(BaseModel):
    """商品图片"""
    image = models.ImageField(upload_to='goods', verbose_name='商品图片')
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品SKU名称')

    class Meta:
        db_table = 'df_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

class IndexGoodsBanner(BaseModel):
    """首页轮播图"""
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    sku = models.ForeignKey('GoodsSKU', verbose_name="商品SKU名称")
    image = models.ImageField(upload_to='goods', verbose_name='商品图片')

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name

class IndexPromotionBanner(BaseModel):
    """促销活动表"""
    name = models.CharField(max_length=20, verbose_name='促销活动名称')
    image = models.ImageField(upload_to='banner', verbose_name='促销图片')
    url = models.URLField(verbose_name='活动链接')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = '促销活动名称'
        verbose_name_plural = verbose_name

class IndexTypeGoodsBanner(BaseModel):
    """首页分类商品表"""
    DISPLAY_TYPE_CHOICES = (
        (0, '标题'),
        (1, '图片')
    )

    sku = models.ForeignKey('GoodsSKU', verbose_name='商品SKU名称')
    type = models.ForeignKey('GoodsType', verbose_name='商品种类')
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES,
                                            verbose_name='展示方式')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = '首页商品分类'
        verbose_name_plural = verbose_name



































