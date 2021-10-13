from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from muscle_movement.skin_module import skin_displacment
import sys
import traceback

class MainMuscle(View):
    def __init__(self):
        super(MainMuscle, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(MainMuscle, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'page_headding': 'Welcome To Muscle Tracker',
            'module_main_page': False
        }
        return render(request, 'main_page.html', context)

    def post(self, request, *args, **kwargs):
        try:
            im1 = request.FILES.get('image_0', None)
            im2 = request.FILES.get('image_1', None)
            if not im1 or not im2:
                return JsonResponse({'success': False, 'message': 'Please select two images'})
            image_string = skin_displacment(im1, im2)
            return JsonResponse({'success': True, 'image_str': image_string, 'message': 'Image generated!'})
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
            return JsonResponse({'success': False, 'message': 'Images updoaded'})