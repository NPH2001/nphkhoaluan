from django.views.generic import ListView
from .models import Motifsampler
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
import subprocess

from django.http import HttpResponseRedirect

from .forms import MotifsamplerForm

class MotifSamplerListView(ListView):
    model = Motifsampler
    template_name = 'motifsampler/motif_sampler.html'


class ResultMotifSamplerListView(ListView):
    model = Motifsampler
    context_object_name = 'motifsampler_result'
    template_name = 'motifsampler/result_motif_sampler.html'
           
    # def post(self, request, *args, **kwargs):
    #     return self.simple_upload(request)
    
    def simple_upload(request):
        if request.method == 'POST' and request.FILES['-f_file']:
            myfile = request.FILES['-f_file']
            fs = FileSystemStorage()
            if fs.exists(myfile.name):
                fs.delete(myfile.name)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'motifsampler/result_motif_sampler.html', {
                'uploaded_file_url': uploaded_file_url,
            })
        return render(request, 'motifsampler/result_motif_sampler.html')

    def get_query_params(self):
        filename = self.request.GET.get('-f_file'),
        position_specific = self.request.GET.get('-q_file'),
        genome__specific  = self.request.GET.get('-b_file'),
        output_o          = self.request.GET.get('output_o'),
        output_m          = self.request.GET.get('output_m'),
        number_of_times   = self.request.GET.get('-r_optional'),
        strands_of_sequences = self.request.GET.get('-s_optional'),
        length_of_mothif = self.request.GET.get('-w_optional'),
        number_of_diff_motif = self.request.GET.get('-n_optional'),
        maxial_allowed = self.request.GET.get('-x_optional'),
        maxium_number = self.request.GET.get('-M_optional'),
        sets_prior = self.request.GET.get('-p_optional'),
        sets_weight = self.request.GET.get('-Q_optional'),
        temporary_parameter = self.request.GET.get('-z_optional'),
        data_dict = {
            "filename": filename,
            "position_specific": position_specific,
            "genome__specific": genome__specific,
            "output_o": output_o,
            "output_m": output_m,
            "number_of_times": number_of_times,
            "strands_of_sequences": strands_of_sequences,
            "length_of_mothif" : length_of_mothif,
            "number_of_diff_motif" : number_of_diff_motif,
            "maxial_allowed": maxial_allowed,
            "maxium_number": maxium_number,
            "sets_prior": sets_prior,
            "sets_weight": sets_weight,
            "temporary_parameter": temporary_parameter,
        }
        _value = {}
        print("DATADICT:",data_dict)
        for key, value in data_dict.items():
            if value[0] is not None:
                int_value = value[0]
                data_dict.update({key: int_value})
            else:
                int_value = ''
                data_dict.update({key: int_value})

        str_command = './motif-sampler -f demo.fna -b demo.bg '

        if data_dict['filename'] != '':
            str_command += f" -f {data_dict['filename']}"
        if data_dict['position_specific'] != '':
            str_command += f" -p {data_dict['position_specific']}"
        if data_dict['genome__specific'] != '':
            str_command += f" -b{ data_dict['genome__specific']}"
        if data_dict['output_o'] != '':
            str_command += f" -o {data_dict['output_o']}"
        if data_dict['output_m'] != '':
            str_command += f" -m {data_dict['output_m']}"
        if data_dict['number_of_times'] != '':
            str_command += f" -r {data_dict['number_of_times']}"
        if data_dict['strands_of_sequences'] != '':
            str_command += f" -s {data_dict['strands_of_sequences']}"
        if data_dict['length_of_mothif'] != '':
            str_command += f" -w {data_dict['length_of_mothif']}"
        if data_dict['number_of_diff_motif'] != '':
            str_command += f" -n {data_dict['number_of_diff_motif']}"
        if data_dict['maxial_allowed'] != '':
            str_command += f" -x {data_dict['maxial_allowed']}"
        if data_dict['maxium_number'] != '':
            str_command += f" -M {data_dict['maxium_number']}"
        if data_dict['sets_prior'] != '':
            str_command += f" -p {data_dict['sets_prior']}"
        if data_dict['sets_weight'] != '':
            str_command += f" -Q {data_dict['sets_weight']}"
        if data_dict['temporary_parameter'] != '':
            str_command += f" -z {data_dict['temporary_parameter']}"
        


        command = str_command
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        directory_result = 'media_2024/' + data_dict['output_m']
        
        # with open(directory_result, 'r') as f:
        #     list_sequence = []
        #     for line in f:
        #         if line.startswith("#Consensus"):
        #             sequence = line.replace('#', '').replace('=', ':').strip()
        #             list_sequence.append(sequence)

        return command

    
    
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filename'] = self.get_query_params()
        return context
