def frequency(l):
    # Count the frequency of each element
    counts = {}
    for num in l:
        counts[num] = counts.get(num, 0) + 1
        
    # Find the minimum and maximum frequencies
    freq_values = counts.values()
    min_freq = min(freq_values)
    max_freq = max(freq_values)
    
    # Collect elements matching min and max frequencies
    minfreqlist = [num for num, freq in counts.items() if freq == min_freq]
    maxfreqlist = [num for num, freq in counts.items() if freq == max_freq]
    
    # Sort the lists in ascending order
    minfreqlist.sort()
    maxfreqlist.sort()
    
    return (minfreqlist, maxfreqlist)
print (frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))