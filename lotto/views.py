import random
from django.shortcuts import render, redirect
from .models import LottoTicket, WinningNumber

# 메인 화면
def home(request):
    last_winning = WinningNumber.objects.last()  # 가장 최근 당첨 번호 가져오기
    total_winners = 0

    if last_winning:
        winning_numbers = set(map(int, last_winning.numbers.split(',')))
        total_winners = LottoTicket.objects.filter(
            numbers__in=winning_numbers
        ).count()

    context = {
        'last_winning': last_winning,
        'total_winners': total_winners,
    }
    return render(request, 'lotto/home.html', context)

# 로또 구매 화면
def buy_ticket(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        is_auto = 'auto' in request.POST  # 자동 구매 여부

        # 비밀번호 중복 체크
        if LottoTicket.objects.filter(password=password).exists():
            return render(request, 'lotto/buy.html', {'error': '비밀번호가 이미 사용 중입니다.'})

        # 번호 생성 (자동 또는 수동)
        if is_auto:
            numbers = ",".join(map(str, random.sample(range(1, 46), 6)))
        else:
            numbers = request.POST.get('numbers')
            try:
                number_list = list(map(int, numbers.split(',')))
                if len(number_list) != 6 or any(n < 1 or n > 45 for n in number_list):
                    raise ValueError
            except ValueError:
                return render(request, 'lotto/buy.html', {'error': '잘못된 번호입니다.'})
            numbers = ",".join(map(str, number_list))

        # 로또 티켓 저장
        LottoTicket.objects.create(numbers=numbers, is_auto=is_auto, password=password)
        return redirect('home')

    return render(request, 'lotto/buy.html')

# 로또 번호 확인 화면
def check_ticket(request):
    if request.method == 'POST':
        password = request.POST.get('password')  # 입력된 비밀번호
        tickets = LottoTicket.objects.filter(password=password)  # 비밀번호로 티켓 검색

        if not tickets.exists():
            return render(request, 'lotto/check.html', {'error': '구매 내역이 없습니다.'})

        # 가장 최근의 당첨 번호 가져오기
        last_winning = WinningNumber.objects.last()
        winning_numbers = set(map(int, last_winning.numbers.split(','))) if last_winning else None

        results = []
        for ticket in tickets:
            ticket_numbers = set(map(int, ticket.numbers.split(',')))
            matches = len(ticket_numbers & winning_numbers) if winning_numbers else 0
            results.append({'ticket': ticket, 'matches': matches})

        return render(request, 'lotto/check.html', {'results': results})

    return render(request, 'lotto/check.html')


# 관리자 화면
def admin_panel(request):
    if request.method == 'POST' and 'draw' in request.POST:
        # 새로운 당첨 번호 생성
        numbers = ",".join(map(str, random.sample(range(1, 46), 6)))
        WinningNumber.objects.create(numbers=numbers)
        return redirect('admin_panel')

    # 모든 당첨 번호 가져오기
    winning_numbers_list = WinningNumber.objects.all()

    # 통계 계산
    total_tickets = LottoTicket.objects.count()
    last_winning = WinningNumber.objects.last()
    total_winners = 0

    if last_winning:
        winning_numbers = set(map(int, last_winning.numbers.split(',')))
        total_winners = LottoTicket.objects.filter(
            numbers__in=winning_numbers
        ).count()

    context = {
        'winning_numbers_list': winning_numbers_list,
        'total_tickets': total_tickets,
        'total_winners': total_winners,
    }
    return render(request, 'lotto/admin_panel.html', context)
