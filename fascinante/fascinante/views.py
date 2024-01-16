from django.shortcuts import render 
from django.http import JsonResponse
from django.views.generic import View
from schedules.forms import SchedulingForm

class HomePageView(View):
  template_name = 'index.html'

  def get(self, request, *args, **kwargs):
      form = SchedulingForm()
      return render(request, self.template_name, {'form': form})
  
  def post(self, request, *args, **kwargs):
      form = SchedulingForm(request.POST)

      if form.is_valid():
          agendamento = form.save()
          return JsonResponse({'status': 'success', 'message': 'Agendamento feito com sucesso!', 'agendamento_id': agendamento.id})
      else:
          return JsonResponse({'status': 'error', 'message': 'Erro ao agendar. Verifique os dados e tente novamente.'})
