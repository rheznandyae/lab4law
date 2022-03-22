from mahasiswa.models import Mahasiswa
from django.http import JsonResponse, HttpResponse

def add_mahasiswa(nama, alamat, npm):
    try:
        Mahasiswa.objects.get(npm=npm)
        response = {'status': 'failed', 'operation': 'post', 'messages': 'data already exists'}
        return JsonResponse(response)
    except:
        new_mahasiswa = Mahasiswa(nama=nama, alamat=alamat, npm=npm)
        new_mahasiswa.save()
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        response = {'status': 'success', 'operation': 'post', 'data': {'nama': mahasiswa.nama, 'alamat': mahasiswa.alamat, 'npm': mahasiswa.npm, 'photo': mahasiswa.photo.name}}
        return JsonResponse(response)

def get_mahasiswa(npm):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        response = {'status': 'success', 'operation': 'get', 'data': {'nama': mahasiswa.nama, 'alamat': mahasiswa.alamat, 'npm': mahasiswa.npm, 'photo': mahasiswa.photo.name}}
        return JsonResponse(response)
    except:
        response = {'status': 'failed', 'operation': 'get', 'meesages': 'data not exists'}
        return JsonResponse(response)

def delete_mahasiswa(npm):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        Mahasiswa.delete(mahasiswa)
        return JsonResponse({'status': 'success', 'operation': 'delete'})
    except:
        response = {'status': 'failed', 'operation': 'delete', 'meesages': 'data not exists'}
        return JsonResponse(response)

def update_mahasiswa(npm, nama, alamat):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        mahasiswa.nama = nama
        mahasiswa.alamat = alamat
        mahasiswa.save()
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        response = {'status': 'success', 'operation': 'update', 'data': {'nama': mahasiswa.nama, 'alamat': mahasiswa.alamat, 'npm': mahasiswa.npm, 'photo': mahasiswa.photo.name}}
        return JsonResponse(response)
    except:
        response = {'status': 'failed', 'operation': 'get', 'meesages': 'data not exists'}
        return JsonResponse(response)

def add_photos(npm, photo):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        mahasiswa.photo = photo
        mahasiswa.save()
        response = {'status': 'success', 'operation': 'update', 'data': {'nama': mahasiswa.nama, 'alamat': mahasiswa.alamat, 'npm': mahasiswa.npm, 'photo': mahasiswa.photo.name}}
        return JsonResponse(response)
    except:
        response = {'status': 'failed', 'operation': 'post', 'meesages': 'data not exists'}
        return JsonResponse(response)

def get_photos(npm):
    try: 
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        valid_image = mahasiswa.photo.name
        with open(valid_image, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except:
        response = {'status': 'failed', 'operation': 'get', 'meesages': 'data not exists'}
        return JsonResponse(response)