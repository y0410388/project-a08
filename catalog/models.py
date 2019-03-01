from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "Male"),
        ('female', "Female"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "User"
        verbose_name_plural = "User"

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=40)
    type = models.ManyToManyField("type" )
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE,)
    model = models.CharField(max_length=40)
    price = models.CharField(max_length=5)
    quantity = models.CharField(max_length=5)
    description = models.CharField(max_length=350, blank= True)
    image = models.ImageField(upload_to="org/%Y/%m", max_length=100, blank= True)
    status = models.CharField(max_length=20, default='disable')
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']


    def get_absolute_url(self):
        return reverse('Item-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Favorites(models.Model):
    item =  models.ForeignKey("Item", on_delete=models.CASCADE,)
    create_on = models.DateTimeField(auto_now_add=True)

class Shopping_cart(models.Model):
    item =  models.ForeignKey("Item", on_delete=models.CASCADE,)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.CharField(max_length=20, default='on hold')
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Delivery_company(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(blank= True)
    phone = models.CharField(max_length=8, blank= True)


    def __str__(self):
        return self.name

class Delivery(models.Model):
    shopping_order = models.ForeignKey("Shopping_cart", on_delete=models.CASCADE,)
    company = models.ForeignKey("Delivery_company", on_delete=models.CASCADE,)
    address = models.CharField(max_length=255)
    recipient = models.CharField(max_length=20)
    phone = models.CharField(max_length=8)
    fee = models.IntegerField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Pay(models.Model):
    shopping_order = models.ForeignKey("Shopping_cart", on_delete=models.CASCADE,)
    delivery_order = models.ForeignKey("Delivery", on_delete=models.CASCADE,)
    pay_method = models.CharField(max_length=20)
    total = models.IntegerField()
    c_number = models.IntegerField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Complaint_type(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return self.name

class Complaint(models.Model):
    shopping_order = models.ForeignKey("Shopping_cart", on_delete=models.CASCADE,)
    type = models.ForeignKey("Complaint_type", on_delete=models.CASCADE,)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    status = models.CharField(max_length=20, default='new')
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Re_complaint(models.Model):
    complaint_order = models.ForeignKey("Complaint", on_delete=models.CASCADE,)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Return_type(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return self.name

class Return_service(models.Model):
    complaint_order = models.ForeignKey("Complaint", on_delete=models.CASCADE,)
    type = models.ForeignKey("Return_type", on_delete=models.CASCADE,)
    content = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='new')

    def __str__(self):
        return str(self.id)

class Problem_type(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return self.name

class Problem_report(models.Model):
    type = models.ForeignKey("Problem_type", on_delete=models.CASCADE,)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    status = models.CharField(max_length=20, default='new')
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Re_problem(models.Model):
    problem_order = models.ForeignKey("Problem_report", on_delete=models.CASCADE,)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    item =  models.ForeignKey("Item", on_delete=models.CASCADE,)
    content = models.CharField(max_length=255, blank=True)
    grade = models.IntegerField(default=1, blank=True)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Re_comment(models.Model):
    comment_order = models.ForeignKey("Comment", on_delete=models.CASCADE,)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Logo", max_length=100)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
