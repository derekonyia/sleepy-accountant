from django.shortcuts import render
from .models import Invoice, InvoiceDetail

# Create your views here.

def dashboard_view(request):
	invoice = Invoice.objects.all() # change this to only return invoice issued and owned by user
	context = {
			'all_invoice' : invoice,
	}
	return render(request, 'dashboard.html', context)

def invoice_detail_view(request, id):
	invoice = Invoice.objects.get(pk=id)
	invoice_details = invoice.invoicedetail_set.all()
	print(invoice_details[0].description)
	subtotal = 0
	tax = invoice.tax
	for val in invoice_details:
		subtotal += val.amount
	total = subtotal + tax
	context ={
		'invoice':invoice,
		'invoice_details':invoice_details,
		'subtotal': subtotal,
		'total': total,
	}
	return render(request, 'invoice_detail_view.html', context)
