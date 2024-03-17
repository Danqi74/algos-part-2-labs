def get_max_peak(nums):
    if len(nums) < 3:
        return -1
    peaks_len=[]
    current_pos = 0
    current_peak = 0
    is_left = False
    is_right = False
    while current_pos < len(nums)-1:
        while (current_pos < len(nums)-1) and (nums[current_pos] < nums[current_pos+1]):
            current_pos += 1
            current_peak += 1
            is_left = True
        while (current_pos < len(nums)-1) and (nums[current_pos] > nums[current_pos+1]):
            current_pos += 1
            current_peak += 1
            is_right = True
        current_peak += 1
        if is_left and is_right and current_peak>=3:
            peaks_len.append(current_peak)
        current_pos += 1
        current_peak = 0
        is_left = False
        is_right = False
    if peaks_len:
        return max(peaks_len)
    return -1
