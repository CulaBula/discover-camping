from django.shortcuts import render
from django.http import HttpResponse
from .models import Park

parks = [{'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Alice Lake Park', 'park_facility': 'Alice Lake- walk in', 'park_type': 'Standard', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Porteau Cove Park', 'park_facility': 'Porteau Cove - Walk In Sites W1 - W16', 'park_type': 'Walk-In', 'park_status': 'Unavailable'}, {'park_name': 'Garibaldi Park', 'park_facility': 'Elfin Lakes Shelter', 'park_type': 'Standard', 'park_status': 'Available'}, {'park_name': 'Mount Seymour Park', 'park_facility': 'Mount Seymour GS', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Mount Seymour Park', 'park_facility': 'Mount Seymour GS', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Porpoise Bay Park', 'park_facility': 'Porpoise Bay Picnic Shelters', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Golden Ears Park', 'park_facility': 'North Beach', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Montague Harbour Marine Park', 'park_facility': 'Montague Harbour', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Montague Harbour Marine Park', 'park_facility': 'Montague Harbour', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Montague Harbour Marine Park', 'park_facility': 'Montague Harbour', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Montague Harbour Marine Park', 'park_facility': 'Montague Harbour', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Montague Harbour Marine Park', 'park_facility': 'Montague Harbour', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Sasquatch Park', 'park_facility': 'Lakeside', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Ruckle Park', 'park_facility': 'Ruckle Groupsite', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Ruckle Park', 'park_facility': 'Ruckle Groupsite', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Ruckle Park', 'park_facility': 'Ruckle Groupsite', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cultus Lake Park', 'park_facility': 'Maple Bay Cabins', 'park_type': 'Cabin', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Cowichan River Park', 'park_facility': 'Stoltz Pool Campground', 'park_type': 'Standard - Half-Double', 'park_status': 'Unavailable'}, {'park_name': 'Gordon Bay Park', 'park_facility': 'Gordon Bay Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Gordon Bay Park', 'park_facility': 'Gordon Bay Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Gordon Bay Park', 'park_facility': 'Gordon Bay Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Gordon Bay Park', 'park_facility': 'Gordon Bay Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Gordon Bay Park', 'park_facility': 'Gordon Bay Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Miracle Beach Park', 'park_facility': 'Miracle Beach Picnic Shelter', 'park_type': 'Standard (Day Use)', 'park_status': 'Unavailable'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}, {'park_name': 'Goldstream Park', 'park_facility': 'Goldstream Group Camp', 'park_type': 'Group Camp Youth', 'park_status': 'Low Availability'}]

def home(request):
    context = {
        'title': 'Home',
        'parks':parks
        # 'parks':Park.objects.all()
    }
    return render(request, 'webui/home.html',context)

def query(request):
    return render(request, 'webui/query.html')