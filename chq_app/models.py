from django.db import models
from datetime import datetime 
from django.forms import Textarea



# Create your models here.


class master(models.Model):

    choise_bank=[
        ('State Bank of India', 'State Bank of India'),
        ('Bandhan Bank', 'Bandhan Bank'),
        ('HDFC Bank', 'HDFC Bank'),
        ('IDBI Bank', 'IDBI Bank'),
        ('Axis Bank', 'Axis Bank'),
        ('Union Bank of India', 'Union Bank of India'),
        ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'),
        ('Indian Bank', 'Indian Bank'),
        ('Punjab National bank', 'Punjab National bank'),
        ('Bank of Baroda', 'Bank of Baroda'),
        ('Indian Overseas Bank', 'Indian Overseas Bank'),
        ('Central Bank of India', 'Central Bank of India'),
        ('Canara Bank', 'Canara Bank'),
        ('UCO Bank', 'UCO Bank'),
        ('ICICI Bank', 'ICICI Bank'),
        ('IDFC FIRST Bank', 'IDFC FIRST Bank'),
        ('KARNATAKA BANK LTD', 'KARNATAKA BANK LTD'),
        ('Bank of India', 'Bank of India'),
        ('IndusInd Bank', 'IndusInd Bank'),
        ('Yes Bank', 'Yes Bank'),
    ]

    choice_agent=[
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Raju Barui', 'Raju Barui'),
        ('Deepraj Manna', 'Deepraj Manna'),
        ('Sanjay Banerjee', 'Sanjay Banerjee'),
        ('Arindam Prasad Mitra', 'Arindam Prasad Mitra'),
        ('Pradip Dutta', 'Pradip Dutta'),
        ('Suman Ghosh', 'Suman Ghosh'),
        
        
    ]

    choice_status=[
        ('Received', 'Received'),
        ('Deposited to bank', 'Deposited to bank'),
        ('Cleared', 'Cleared'),
        ('Bounced', 'Bounced'),
        ('Cancelled', 'Cancelled'),
    ]

    client=models.CharField(max_length=100, null=False)
    amount=models.IntegerField(null=False)
    chq=models.CharField(max_length=10, default='C->')
    bank=models.CharField(max_length=50, choices=choise_bank, null=False)
    status=models.CharField(max_length=20, choices=choice_status, null=False)
    agent=models.CharField(max_length=25, choices=choice_agent, null=False)
    date=models.DateTimeField(default=datetime.now)
    remarks=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f'CLIENT: {self.client}   STATUS: {self.status} DATE: {self.date}'




class order(models.Model):

    choice_agent=[
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Raju Barui', 'Raju Barui'),
        ('Deepraj Manna', 'Deepraj Manna'),
        ('Sanjay Banerjee', 'Sanjay Banerjee'),
        ('Arindam Prasad Mitra', 'Arindam Prasad Mitra'),
        ('Pradip Dutta', 'Pradip Dutta'),
        ('Suman Ghosh', 'Suman Ghosh'),
        
        
    ]

    choice_delivery=[
        ('Delivered','Delivered'),
        ('Not Delivered','Not Delivered'),
        ('Cancelled','Cancelled'),
    ]

    choice_payment=[
        ('Cash Received','Cash Received'),
        ('Ondate Cheque Received','Ondate Cheque Received'),
        ('Postdate Cheque Received','Postdate Cheque Received'),
        ('Online NEFT','Online NEFT'),
        ('UPI Payment','UPI Payment'),
        ('No Payment','No Payment'),
    ]

    choice_delivery_agent=[
        ('Kaka','Kaka'),
        ('Raju Barui','Raju Barui'),
        ('Rituraj Saran', 'Rituraj Saran'),
    ]

    date=models.DateTimeField(default=datetime.now)
    shop_name=models.CharField(max_length=80, null=False)
    invoice=models.CharField(max_length=11,default='I->', null=False)
    amount=models.IntegerField(null=False)
    agent=models.CharField(max_length=25, choices=choice_agent, null=False)
    deliverysts=models.CharField(max_length=25,choices=choice_delivery,null=False)
    deliveryagt=models.CharField(max_length=25,choices=choice_delivery_agent, null=False)
    paymentsts=models.CharField(max_length=50,choices=choice_payment, null=False)
    remarks=models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'AGENT: {self.agent} DELIVERY STATUS: {self.deliverysts} DATE: {self.date}'



class replacement(models.Model):


    choice_agent=[
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Raju Barui', 'Raju Barui'),
        ('Deepraj Manna', 'Deepraj Manna'),
        ('Sanjay Banerjee', 'Sanjay Banerjee'),
        ('Arindam Prasad Mitra', 'Arindam Prasad Mitra'),
        ('Pradip Dutta', 'Pradip Dutta'),
        ('Suman Ghosh', 'Suman Ghosh'),
        
    ]

    choice_status=[
        ('Received','Received'),
        ('CN Given','CN Given'),
        ('Item Given','Item Given'),
        ('DOA Received','DOA Received'),
        ('DOA Given','DOA Given'),
    ]

    date=models.DateTimeField(default=datetime.now)
    recv_challan=models.CharField(max_length=30, blank=True)
    client=models.CharField(max_length=30, null=False)
    item=models.TextField(max_length=400,null=False)
    qty=models.IntegerField(null=False)
    agent=models.CharField(max_length=25,choices=choice_agent, null=False)
    status=models.CharField(max_length=15,choices=choice_status, null=False)
    issue=models.CharField(max_length=100,blank=True)
    delv_doc=models.CharField(max_length=10,blank=True)
    delv_date=models.CharField(max_length=20,blank=True)
    remarks=models.CharField(max_length=80,blank=True)
    bar=models.CharField(max_length=20,blank=True)
    img = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f'CLIENT: {self.client}   STATUS: {self.status} DATE: {self.date}'
    

class new_order(models.Model):

    choice_agent=[
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Raju Barui', 'Raju Barui'),
        ('Deepraj Manna', 'Deepraj Manna'),
        ('Sanjay Banerjee', 'Sanjay Banerjee'),
        ('Arindam Prasad Mitra', 'Arindam Prasad Mitra'),
        ('Pradip Dutta', 'Pradip Dutta'),
        ('Suman Ghosh', 'Suman Ghosh'),
        
    ]

    choice_status=[
        ('New Order', 'New Order'),
        ('Pending Material', 'Pending Material'),
        ('Billed', 'Billed'),
        ('Cancelled', 'Cancelled'),
    ]

    date=models.DateTimeField(default=datetime.now)
    agent=models.CharField(max_length=25,choices=choice_agent, null=False)
    shop=models.CharField(max_length=50, null=False)
    status=models.CharField(max_length=20,choices=choice_status, null=False)
    order_details=models.TextField(max_length=400,null=False)
    remarks=models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'AGENT: {self.agent}   STATUS: {self.status} DATE: {self.date}'
    

class boat_ticket(models.Model):

    choice_pickup=[
        ('Pickup from Home','Pickup from Home'),
        ('Pickup from Retailer','Pickup from Retailer'),
    ]

    choice_agent=[
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Raju Barui', 'Raju Barui'),
        ('Deepraj Manna', 'Deepraj Manna'),
        ('Sanjay Banerjee', 'Sanjay Banerjee'),
        ('Arindam Prasad Mitra', 'Arindam Prasad Mitra'),
        ('Pradip Dutta', 'Pradip Dutta'),
        ('Suman Ghosh', 'Suman Ghosh'),
        
    ]

    choice_status=[
        ('New Ticket','New Ticket'),
        ('Ticket issued','Ticket issued'),
        ('Ticket resolved','Ticket resolved'),
        ('Ticket rejected','Ticket rejected'),
    ]

    date=models.DateTimeField(default=datetime.now)
    name=models.CharField(max_length=30, null=False)
    mobile=models.CharField(max_length=11,null=False)
    email=models.EmailField(max_length=50,null=False)
    full_address=models.TextField(max_length=400,null=False)
    landmark=models.CharField(max_length=100,null=False)
    model=models.CharField(max_length=50,null=False)
    colour=models.CharField(max_length=25,null=False)
    issue=models.CharField(max_length=100,null=False)
    invoice=models.CharField(max_length=15,null=False)
    inv_img = models.ImageField(upload_to='boat_invoice/',blank=False,null=False)
    retailer=models.CharField(max_length=100,null=False)
    retailer_ph=models.CharField(max_length=15,blank=True)
    pickup=models.CharField(max_length=20,choices=choice_pickup,null=False)
    agent=models.CharField(max_length=25,choices=choice_agent,blank=True)
    status=models.CharField(max_length=25,choices=choice_status,blank=True)
    remarks=models.CharField(max_length=120, blank=True)

    

    def __str__(self):
        return f'RETAILER: {self.retailer}   STATUS: {self.status} DATE: {self.date}'
    
