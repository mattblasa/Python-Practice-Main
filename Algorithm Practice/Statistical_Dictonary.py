def get_statistics(input_list):
    sorted_imput = sorted(input_list) #sort list by numerical 
    input_length = len(sorted_imput) #check the length of the imput

    #mean 
    mean = sum(sorted_imput) / imput_length

    #median 
    middle_idx = (len(sorted_imput) - 1) // 2 #floor division to get middle index, if number is odd 
    median = sorted_imput[middle_idx] #find the index in the data set 

    if input_length % 2 == 0: #this in case the number of numbers is even 
        middle_num_1 = sorted_imput[middle_idx] # 
        middle_num_2 = sorted_imput[middle_idx+1]
        median = (middle_num_1 + middle_num_2) /2

    #mode 
    number_counts = {x: sorted_imput.count(x) for i in set(sorted_imput)} #counts the amount of each unique number
    mode = max(number_counts.keys(), key=lambda unique_number: number_counts[unique_number]) #needs explanation

    #sample variance 
    sample_variance = sum([])

    #sample_standard deviation
    


    #mean CI interval 


    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
