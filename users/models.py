from django.db import models

# Create your models here.
# user database creates automatic password for users and sends reset password links to email

class User(models.Model):
	username  = models.CharField(max_length=100,null=True)
	email     = models.EmailField(null=True)
	address   = models.TextField(null=True)
	password  = models.CharField(max_length=100)

	def __str__(self, *args, **kwargs):
		return self.email