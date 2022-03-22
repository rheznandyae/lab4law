
from rest_framework.decorators import api_view
import mahasiswa.service as mahasiswa_service

# Create your views here.
@api_view(['POST'])
def add_mahasiswa(request):
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    npm = request.POST['npm']
    return mahasiswa_service.add_mahasiswa(nama, alamat, npm)

@api_view(['GET'])
def get_mahasiswa(request, npm):
    return mahasiswa_service.get_mahasiswa(npm)

@api_view(['DELETE'])
def delete_mahasiswa(request, npm):
    return mahasiswa_service.delete_mahasiswa(npm)

@api_view(['PUT'])
def update_mahasiswa(request, npm):
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    return mahasiswa_service.update_mahasiswa(npm, nama, alamat)

@api_view(['POST'])
def add_photos(request, npm):
    photo = request.FILES['photos']
    return mahasiswa_service.add_photos(npm, photo)

@api_view(['GET'])
def get_photos(request, npm):
    return mahasiswa_service.get_photos(npm)