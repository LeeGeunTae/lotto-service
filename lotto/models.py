from django.db import models

class LottoTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    numbers = models.CharField(max_length=20)  # 저장 형식: "1,2,3,4,5,6"
    is_auto = models.BooleanField(default=True)
    password = models.CharField(max_length=4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WinningNumber(models.Model):
    draw_date = models.DateTimeField(auto_now_add=True)
    numbers = models.CharField(max_length=20)  # 저장 형식: "1,2,3,4,5,6"

class LottoStats(models.Model):
    draw_date = models.DateTimeField()
    total_tickets = models.IntegerField()
    winners = models.IntegerField()
