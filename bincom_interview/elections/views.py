from django.shortcuts import render
from .models import AnnouncedPuResult
from .models import PollingUnit, AnnouncedPuResult, LGA
from django.shortcuts import redirect

def polling_unit_result(request, uniqueid):
    results = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=uniqueid)
    return render(request, 'polling_unit_result.html', {'results': results})

def lga_results(request):
    if request.method == 'POST':
        lga_id = request.POST['lga']
        print(f"Selected LGA ID: {lga_id}")
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        print(f"Polling Units: {polling_units}")
        total_results = {}
        for pu in polling_units:
            results = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=pu.uniqueid)
            print(f"Results for Polling Unit {pu.uniqueid}: {results}")
            for result in results:
                total_results[result.party_abbreviation] = total_results.get(result.party_abbreviation, 0) + result.party_score
        print(f"Total Results: {total_results}")
        return render(request, 'lga_results.html', {'total_results': total_results})

    lgas = LGA.objects.all()
    print(f"LGAs: {lgas}")
    return render(request, 'select_lga.html', {'lgas': lgas})

def add_polling_unit_result(request):
    if request.method == 'POST':
        uniqueid = request.POST['uniqueid']
        party_scores = request.POST.getlist('party_scores')
        parties = request.POST.getlist('parties')
        for party, score in zip(parties, party_scores):
            AnnouncedPuResult.objects.create(
                polling_unit_uniqueid=uniqueid,
                party_abbreviation=party,
                party_score=score,
                entered_by_user='admin',
                date_entered=timezone.now(),
                user_ip_address=request.META['REMOTE_ADDR']
            )
        return redirect('polling_unit_result', uniqueid=uniqueid)
    return render(request, 'add_polling_unit_result.html')