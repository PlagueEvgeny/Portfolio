from django.db import models


class Hello(models.Model):
    title = models.TextField()
    cover_hello = models.ImageField(upload_to='img/hello/')
    desc = models.TextField()


class About(models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='img/about/', blank=True)
    

class Facts(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="facts")
    random = models.CharField(max_length=128, blank=True)


class Portfolio(models.Model):
    caver = models.ImageField(upload_to='caver/', blank=True)
    name = models.CharField(max_length=128)
    desc = models.TextField()
    github = models.URLField(max_length=128, blank=True)
    company = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    portfolio = models.ImageField(upload_to='portfolio/', blank=True)

    def __str__(self):
        return f"{self.image.name} - {self.portfolio}"


class Certificate(models.Model):
    name = models.CharField(max_length=64, blank=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='certificate/', blank=True)
    file = models.FileField(upload_to='file/certificate/', blank=True)

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=64, blank=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='tools/', blank=True)


class UseTools(models.Model):
    tools = models.ForeignKey(Tools, on_delete=models.CASCADE, related_name='tools')
    icon = models.ImageField(upload_to='icon/', blank=True)
    text = models.TextField(blank=True)
