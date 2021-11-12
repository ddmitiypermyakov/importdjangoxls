from django.db import models


class Products(models.Model):

    name=models.CharField('Наименование',max_length=255,db_index=True)
    description=models.TextField('Описание',blank=True,help_text='Опишите товар')
    price = models.DecimalField('Цена',max_digits=6,decimal_places=2,default=0.00)
    date_published=models.DateTimeField('Дата публикации',auto_now_add=True)
    available = models.BooleanField('Наличие',default=False)

    def __str__(self):
        return self.name


