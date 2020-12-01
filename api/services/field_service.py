from django.http import JsonResponse
from rest_framework import status

from api.models import Inclinometry, Well, Mer, Rate, FieldCoordinate, Zone
from api.serializers import IncSerializer, WellSerializer, MerSerializer, RateSerializer, FieldCoordinateSerializer, \
    ZoneSerializer


# CHILD OBJECTS
# /fields/{id}/wells GET
def get_field_wells(pk):
    wells = Well.objects.filter(well__field_id=pk)
    serializer = WellSerializer(wells, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/inclinometry GET
def get_field_inclinometry(pk):
    inc = Inclinometry.objects.filter(well__field_id=pk)
    serializer = IncSerializer(inc, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/mer GET
def get_field_mer(pk):
    mer = Mer.objects.filter(well__field_id=pk)
    serializer = MerSerializer(mer, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/rates GET
def get_field_rates(pk):
    rate = Rate.objects.filter(well__field_id=pk)
    serializer = RateSerializer(rate, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/coordinates GET
def get_field_coordinates(pk):
    rate = FieldCoordinate.objects.filter(field_id=pk)
    serializer = FieldCoordinateSerializer(rate, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/zones GET
def get_field_zones(pk):
    rate = Zone.objects.filter(well__field_id=pk)
    serializer = ZoneSerializer(rate, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/inclinometry DELETE
def delete_field_inclinometry(pk):
    count = Inclinometry.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Inc were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/mer DELETE
def delete_field_mer(pk):
    count = Mer.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Mer were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/rates DELETE
def delete_field_rates(pk):
    count = Rate.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Rates were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/coordinates DELETE
def delete_field_coordinates(pk):
    count = FieldCoordinate.objects.filter(field_id=pk).delete()
    return JsonResponse({'message': '{} Coordinates were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/zones DELETE
def delete_field_zones(pk):
    count = Zone.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Zones were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)
