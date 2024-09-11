from django.shortcuts import render, redirect

from .forms import BinPackingDemoForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')


def glance(request):
    return render(request, 'glance.html')


def demo_view(request):
    if request.method == 'POST':
        form = BinPackingDemoForm(request.POST)
        if form.is_valid():
            bin_capacity = form.cleaned_data['bin_capacity']
            item_list = form.cleaned_data['item_list']
            items = [int(item.strip()) for item in item_list.split(',')]
            algorithm = form.cleaned_data['algorithm']

            if algorithm == 'first_fit':
                bins, steps, num_bins_used, remaining_capacities = first_fit(bin_capacity, items)
            elif algorithm == 'next_fit':
                bins, steps, num_bins_used, remaining_capacities = next_fit(bin_capacity, items)
            elif algorithm == 'best_fit':
                bins, steps, num_bins_used, remaining_capacities = best_fit(bin_capacity, items)
            elif algorithm == 'worst_fit':
                bins, steps, num_bins_used, remaining_capacities = worst_fit(bin_capacity, items)

            # Prepare data for the template
            bin_details = [
                {'items': bins[i], 'remaining_capacity': remaining_capacities[i]}
                for i in range(num_bins_used)
            ]

            context = {
                'steps': steps,
                'num_bins_used': num_bins_used,
                'bin_details': bin_details,
            }
            return render(request, 'steps.html', context)
        else:
            error_msg = "Form is invalid. Please correct the errors below."
            return render(request, 'demo.html', {'form': form, 'error_msg': error_msg})

    else:
        form = BinPackingDemoForm()

    return render(request, 'demo.html', {'form': form})


def FF(request):
    return render(request, 'FF.html')


def NF(request):
    return render(request, 'NF.html')


def BF(request):
    return render(request, 'BF.html')


def WF(request):
    return render(request, 'WF.html')


def applications(request):
    return render(request, 'applications.html')


def first_fit(bin_capacity, items):
    bins = []
    steps = []
    for item in items:
        placed = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                steps.append(f"Put item {item} in existing bin with remaining capacity {bin_capacity - sum(bin)}")
                placed = True
                break
        if not placed:
            bins.append([item])
            steps.append(f"Created new bin to fit item {item} with remaining capacity {bin_capacity - item}")

    remaining_capacities = [bin_capacity - sum(bin) for bin in bins]
    num_bins_used = len(bins)

    return bins, steps, num_bins_used, remaining_capacities


def next_fit(bin_capacity, items):
    bins = [[]]  # Start with one empty bin
    steps = []
    for item in items:
        if sum(bins[-1]) + item <= bin_capacity:
            bins[-1].append(item)
            steps.append(f"Put item {item} in current bin with remaining capacity {bin_capacity - sum(bins[-1])}")
        else:
            bins.append([item])
            steps.append(f"Created new bin to fit item {item} with remaining capacity {bin_capacity - item}")

    remaining_capacities = [bin_capacity - sum(bin) for bin in bins]
    num_bins_used = len(bins)

    return bins, steps, num_bins_used, remaining_capacities


def best_fit(bin_capacity, items):
    bins = []
    steps = []
    for item in items:
        min_space = bin_capacity + 1
        best_bin = None
        for bin in bins:
            space_left = bin_capacity - sum(bin)
            if space_left >= item and space_left < min_space:
                min_space = space_left
                best_bin = bin
        if best_bin is not None:
            best_bin.append(item)
            steps.append(f"Put item {item} in best bin with remaining capacity {bin_capacity - sum(best_bin)}")
        else:
            bins.append([item])
            steps.append(f"Created new bin to fit item {item} with remaining capacity {bin_capacity - item}")

    remaining_capacities = [bin_capacity - sum(bin) for bin in bins]
    num_bins_used = len(bins)

    return bins, steps, num_bins_used, remaining_capacities


def worst_fit(bin_capacity, items):
    bins = []
    steps = []
    for item in items:
        max_space = -1
        worst_bin = None
        for bin in bins:
            space_left = bin_capacity - sum(bin)
            if space_left >= item and space_left > max_space:
                max_space = space_left
                worst_bin = bin
        if worst_bin is not None:
            worst_bin.append(item)
            steps.append(f"Put item {item} in worst bin with remaining capacity {bin_capacity - sum(worst_bin)}")
        else:
            bins.append([item])
            steps.append(f"Created new bin to fit item {item} with remaining capacity {bin_capacity - item}")

    remaining_capacities = [bin_capacity - sum(bin) for bin in bins]
    num_bins_used = len(bins)

    return bins, steps, num_bins_used, remaining_capacities

