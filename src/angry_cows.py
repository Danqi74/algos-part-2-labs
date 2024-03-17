def sort(array):
    is_sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_sorted = False
    if is_sorted:
        return
    quick_sort(array, 0, len(array)-1)


def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1


def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)


def can_be_placed(N, C, free_sections, distance):
    cows = 1
    last_cow_idx = 0
    for i in range(1, N):
        if free_sections[i] - free_sections[last_cow_idx] >= distance:
            cows += 1
            last_cow_idx = i
            if cows == C:
                return True
    return False


def get_distance(N, C, free_sections) :
    """
    Function to count minimum maximum distance to place the cows
    N -> numbers of cows must be placed
    C -> numbers of angry cows
    """
    if N > len(free_sections):
        return 0
    sort(free_sections)
    sections_difference = free_sections[-1] - free_sections[0]
    if C == 2 and sections_difference > 1:
        return sections_difference
    max_dist = sections_difference // (C-1)
    min_dist = 2
    result = 0
    while min_dist <= max_dist:
        middle = (min_dist + max_dist) // 2
        if can_be_placed(N, C, free_sections, middle):
            result = middle
            min_dist = middle + 1
        else:
            max_dist = middle -1
    return result
