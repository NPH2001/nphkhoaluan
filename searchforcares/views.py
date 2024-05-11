from django.views.generic import ListView

from .models import Searchforcare

from factors.models import Factor

from history.mixins import ObjectViewMixin
from history.signals import object_viewed_signal


import re
import numpy as np




# motif_found = {}

class SearchMotif(ObjectViewMixin, ListView):
  model = Searchforcare
  template_name = 'search_motif/result_search_motif.html'

  motif_found = {}

  
  def find_sequence_in_database(self, fragment_dna, database):
    found_sequences = []
    start = 0
    for key, value in database.items():
        for match in re.finditer(value, fragment_dna):
            start = match.start()
            end = start + len(value)
            found_sequences.append((value, key, start, end))
            # self.motif_found.update({key:value})

    return found_sequences
  
  def rev_comp_st(seq):
        '''This function returns a reverse complement 
        of a DNA or RNA strand'''
        seq = seq.replace("A", "t").replace(
            "C", "g").replace("T", "a").replace("G", "c")
        seq = seq.upper()
        return seq
  
  def foundsequences(found_sequences, fragment):
        colored_sequence = ""
        last_end = 0
        if found_sequences:
            for sequence, _, start, end in found_sequences:
                colored_sequence += fragment[last_end:start]  # Append non-matching portion
                colored_sequence +=  f'<span class="highlight">{(fragment[start:end])}</span>'   # Color matching portion
                last_end = end
            colored_sequence += fragment[last_end:]  # Append the remaining portion of the sequence
        return colored_sequence
  
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fragment = self.request.GET.get('sequencetosubmit')
        reverse_fragment = SearchMotif.rev_comp_st(fragment)
        
        color_map = {}
        factors = Factor.objects.all()
        database = {}
        for factor in factors:
            database.update({factor.ac: factor.sq})
            color_map[factor.ac] = list(np.random.choice(range(256), size=3))

        found_sequences = self.find_sequence_in_database(fragment, database)
        reverse_found_sequences = self.find_sequence_in_database(reverse_fragment, database)
        
        context['motif_found'] = {key: value for key, value, _, _ in found_sequences}
        context['reverse_motif_found'] = {key: value for key, value, _, _ in reverse_found_sequences}
        context['factor_ac'] = database
        context['fragment_results'] = SearchMotif.foundsequences(found_sequences, fragment)
        context['reverse_fragment_results'] = SearchMotif.foundsequences(reverse_found_sequences, reverse_fragment)
        return context
  
  def dispatch(self, request, *args, **kwargs):
        query = request.GET.get('sequencetosubmit', '')  # Lấy thông tin tìm kiếm từ request
        user = request.user if request.user.is_authenticated else None  # Lấy thông tin người dùng
        self.record_search_history(query, user)
        return super().dispatch(request, *args, **kwargs)

