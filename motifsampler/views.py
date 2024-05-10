from django.views.generic import ListView
from .models import Motifsampler

class MotifSamplerListView(ListView):
    model = Motifsampler
    template_name = 'motifsampler/motif_sampler.html'


class ResultMotifSamplerListView(ListView):
    model = Motifsampler
    context_object_name = 'motifsampler_result'
    template_name = 'motifsampler/result_motif_sampler.html'

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
        a = [filename, position_specific, genome__specific, output_o, output_m, number_of_times, strands_of_sequences, length_of_mothif, number_of_diff_motif,
             maxial_allowed, maxium_number, sets_prior, sets_weight, temporary_parameter]
        converted_list = [int(item[0]) if item[0] is not None and item[0].isdigit() else item[0] for item in a]
        return converted_list

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filename'] = self.get_query_params()
        return context

