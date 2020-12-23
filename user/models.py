from django.db import models


class TUser(models.Model):
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_pwd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 't_user'


class TBook(models.Model):
    book_name = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    publish = models.CharField(max_length=20, blank=True, null=True)
    publish_time = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    isbn = models.IntegerField(blank=True, null=True)
    word_count = models.BigIntegerField(blank=True, null=True)
    page_count = models.BigIntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=20, blank=True, null=True)
    book_paper = models.CharField(max_length=20, blank=True, null=True)
    book_wrapper = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    old_price = models.FloatField(blank=True, null=True)
    new_price = models.FloatField(blank=True, null=True)
    editor_recommendation = models.CharField(max_length=2000, blank=True, null=True)
    content_introduction = models.CharField(max_length=2000, blank=True, null=True)
    author_incroduction = models.CharField(max_length=2000, blank=True, null=True)
    menu = models.CharField(max_length=2000, blank=True, null=True)
    media_review = models.CharField(max_length=2000, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    picture = models.CharField(max_length=20, blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)

    def discount(self):
        return "%.2f" % (self.old_price / self.new_price * 10)

    class Meta:
        db_table = 't_book'


class TAddress(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=6, blank=True, null=True)
    cellphone = models.CharField(max_length=11, blank=True, null=True)
    addr_mobile = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_address'


class TCar(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_car'

    def totalprice(self):
        return "%.2f" % (self.book.new_price * self.count)


class TOrder(models.Model):
    order_id = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_order'


class TOrderItem(models.Model):
    count = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 't_order_item'


class TCategory(models.Model):
    category_id = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_category'
