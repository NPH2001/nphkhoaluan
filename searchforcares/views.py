from django.views.generic import ListView

from .models import Searchforcare

from factors.models import Factor

from history.mixins import ObjectViewMixin
from history.signals import object_viewed_signal


import re
import random

from history.models import *

sequence_color = ""

from django.shortcuts import render, redirect

from factors.models import *

import json

from django.utils.html import escape

# bg = Factor.objects.get(pk=1)
# data = json.loads(bg.color)
# {'x':235,'y':237,'z':156}


def Detail_ac(request, pk):
    if request.method == "GET":
        data = Factor.objects.get(pk=pk)
        context = {"factor": data}
        return render(request, "search_motif/factor_ac.html", context, status=200)


# motif_found = {}


class SearchMotif(ObjectViewMixin, ListView):
    model = Searchforcare
    template_name = "search_motif/result_search_motif.html"

    motif_found = {}

    def colored(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def iupac_to_regex(self, substring):
        iupac_codes = {
            "R": "[AG]",
            "Y": "[CT]",
            "S": "[GC]",
            "W": "[AT]",
            "K": "[GT]",
            "M": "[AC]",
            "B": "[CGT]",
            "D": "[AGT]",
            "H": "[ACT]",
            "V": "[ACG]",
            "N": "[ACGT]",
        }
        pattern = ""
        for char in substring:
            if char in iupac_codes:
                pattern += iupac_codes[char]
            else:
                pattern += char

        return pattern

    def find_sequence_in_database(self, fragment_dna, database):
        found_sequences = []
        start = 0
        for key, value in database.items():
            if isinstance(value, str):
                for match in re.finditer(value, fragment_dna):
                    start = match.start()
                    end = start + len(value)
                    found_sequences.append((value, key, start, end))
                    # self.motif_found.update({key:value})

        return found_sequences

    def rev_comp_st(seq):
        """This function returns a reverse complement
        of a DNA or RNA strand"""
        seq = (
            seq.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
        )
        return seq.upper()[::-1]

    def foundsequences(self, found_sequences, fragment):
        colored_sequence = ""
        sequence_color = ""
        last_end = 0
        if found_sequences:
            found_sequences.sort(key=lambda x: x[2])  # Sort sequences by start position
            # print(found_sequences)
            for sequence, _, start, end in found_sequences:
                x = random.randrange(254)
                y = random.randrange(254)
                z = random.randrange(254)
                if start >= last_end:  # Ensure no overlap
                    colored_sequence += fragment[
                        last_end:start
                    ]  # Append non-matching portion
                    colored_sequence += f'<span class="highlight" style="background-color: rgb({x}, {y}, {z});">{(fragment[start:end])}</span>'  # Color matching portion
                    # colored_sequence += self.colored( x, y, fragment[start:end])
                    last_end = end
                    sequence_color += f'<span class="highlight" style="background-color: rgb({x}, {y}, {z});">{(fragment[start:end])}</span>'
                elif end > last_end:  # Handle overlap
                    colored_sequence += f'<span class="highlight" style="background-color: rgb({x}, {y}, {z});">{(fragment[start:end])}</span>'  # Color overlapping portion
                    last_end = end
                    sequence_color += f'<span class="highlight" style="background-color: rgb({x}, {y}, {z});">{(fragment[start:end])}</span>'
        colored_sequence += fragment[
            last_end:
        ]  # Append the remaining portion of the sequence
        return colored_sequence

    def fill_color(self, fragment):
        # Chuỗi cần xử lý
        vcc = fragment
        list_factor = []

        # Giả sử vcc_list chứa các đối tượng Factor với thuộc tính sq và color
        vcc_list = Factor.objects.all()
        vcc_list = sorted(vcc_list, key=lambda i: len(i.sq), reverse=True)

        # Danh sách để lưu trữ các vị trí đã được tô màu
        colored_positions = []

        # Danh sách tạm thời để lưu trữ các thẻ <span>
        span_list = []

        # Duyệt qua từng phần tử trong vcc_list
        for factor in vcc_list:
            pattern = self.iupac_to_regex(factor.sq)
            # Kiểm tra xem giá trị của thuộc tính sq có tồn tại trong chuỗi vcc không
            matches = re.finditer(pattern, vcc)

            # Tạo danh sách tạm thời để lưu trữ các vị trí của các cụm từ được tìm thấy
            positions = []
            for match in matches:
                # Lấy vị trí bắt đầu và kết thúc của cụm từ trong vcc
                start = match.start()
                end = match.end()
                # Kiểm tra xem vị trí này đã được tô màu trước đó chưa
                overlap = any(
                    start < colored_end and end > colored_start
                    for colored_start, colored_end in colored_positions
                )
                if not overlap:
                    # Thêm vị trí vào danh sách tạm thời
                    positions.append((start, end))
                    # Cập nhật danh sách các vị trí đã được tô màu
                    colored_positions.append((start, end))

            # Sắp xếp lại danh sách các vị trí theo vị trí bắt đầu (tăng dần)
            positions = sorted(positions, key=lambda x: x[0])

            # Thêm các thẻ <span> vào danh sách tạm thời
            for start, end in positions:
                span = f'<span style="background-color: {factor.color}; color:white;">{vcc[start:end]}</span>'
                span_list.append((start, end, span))

            # Thêm phần tử tương ứng vào list_factor
            if positions:
                list_factor.append(factor)

        # Sắp xếp lại danh sách các thẻ <span> theo vị trí bắt đầu (tăng dần)
        span_list = sorted(span_list, key=lambda x: x[0])

        # Thêm các thẻ <span> vào chuỗi vcc
        offset = 0
        for start, end, span in span_list:
            vcc = vcc[: start + offset] + span + vcc[end + offset :]
            offset += len(span) - (end - start)

        print("list_factor:", list_factor)
        print("vcc:", vcc)
        data = {}
        data["text_fill"] = vcc
        data["list_factor"] = list_factor
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fragment = self.request.GET.get("sequencetosubmit")
        # print('fragment:',fragment)
        reverse_fragment = SearchMotif.rev_comp_st(fragment)

        factors = Factor.objects.all()
        database = {}
        for factor in factors:
            database.update({factor.ac: factor.sq})

        # print('database:',database)

        found_sequences = self.find_sequence_in_database(fragment, database)
        reverse_found_sequences = self.find_sequence_in_database(
            reverse_fragment, database
        )

        context["sequence_color"] = sequence_color
        vgg = self.fill_color(fragment)
        vgg1 = self.fill_color(reverse_fragment)
        context["fragment"] = vgg["text_fill"]
        context["reverse_fragment"] = vgg1["text_fill"]
        context["motif_found"] = vgg["list_factor"]
        context["reverse_motif_found"] = vgg1["list_factor"]
        context["factor_ac"] = database

        # print ('self.request.user', self.request.user.is_authenticated)
        print("context motif_found", context["motif_found"])

        if self.request.user.is_authenticated:
            fdd = History_search_care.objects.create(
                F_r=context["fragment"],
                R_f_r=context["reverse_fragment"],
            )
            print("hhh", fdd.Ms)
            fdd.Ms.set(context["motif_found"])
            fdd.Ms_r.set(context["reverse_motif_found"])
            fdd.save()

            query = self.request.GET.get(
                "sequencetosubmit", ""
            )  # Lấy thông tin tìm kiếm từ request
            user = (
                self.request.user if self.request.user.is_authenticated else None
            )  # Lấy thông tin người dùng
            new_history = History.objects.create(
                user=user, query=query, Belong_history_search_care=fdd
            )

        return context

    def dispatch(self, request, *args, **kwargs):
        query = request.GET.get(
            "sequencetosubmit", ""
        )  # Lấy thông tin tìm kiếm từ request
        user = (
            request.user if request.user.is_authenticated else None
        )  # Lấy thông tin người dùng
        self.record_search_history(query, user, "")
        return super().dispatch(request, *args, **kwargs)
