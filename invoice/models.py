from django.db import models
from datetime import date
# from users.models import User

# i_hash is made with host password and would be used to validate hash 
# maybe hash should work like password in reverse the hash on paper while the raw password in db
# create a customer databse incase they dont want to signup
# customer table would help make relationship with who buys what and help determining wether a product is worth buying, how frequent customer buys products, what they like etc 
# customer table should be created in users app so that when cutomer signs up we can suggest wether customer frequents certain stores and should provide clue/hash to claim invoices by user


# class Customer(models.Model):
	# client_email   = models.EmailField(null=True)
	# client_addr	   = models.TextField(null=True)


class Invoice(models.Model):
	b_name 		   = models.CharField(max_length=200)
	i_hash         = models.CharField(max_length=1064)
	client         = models.ForeignKey(
					'users.User', 
					on_delete=models.CASCADE, 
					null=True,
					related_name='client'
					)

	issuer		   = models.ForeignKey(
					'users.User', 
					on_delete=models.CASCADE, 
					null=True,
					related_name='issuer'
					)

	issue_date	   = models.DateField(default=date.today)
	Subtotal	   = models.IntegerField() 
	tax			   = models.IntegerField()
	total 		   = models.IntegerField()

	def __str__(self):
		return self.b_name



class InvoiceDetail(models.Model):
	invoice     = models.ForeignKey(
				'Invoice',
				on_delete=models.CASCADE, 
		)
	description = models.TextField()
	unit_cost   = models.IntegerField() 
	qty         = models.IntegerField() 
	amount      = models.IntegerField() 


	def __str__(self):
		return self.description