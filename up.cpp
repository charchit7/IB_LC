int Solution::maximumGap(const vector<int> &A) {
    // minimum gap if all elements are equidistant i.e. min, min + 1*gap, min + 2*gap, min + (n-1)*gap
    //  and maximum when they all elements are either max or min, so gap can be max-min -- maximum gap
    // max = min + (n-1)*gap
    // gap = max-min / (n-1) -- minimum gap
    // we will create buckets such that: min + index*gap = number
    // index = (number - min)*(n-1) / (max - min)
    // If you pick any 2 numbers from a single bucket, their difference will be less than gap, and hence they would never contribute to maxgap ( Remember maxgap >= gap ). We only need to store the largest number and the smallest number in each bucket, and we only look at the numbers across bucket.
    // Now, we just need to go through the bucket sequentially ( they are already sorted by value ), and get the difference of min_value with max_value of previous bucket with at least one value. We take maximum of all such values.
    if(A.size()==1) return 0;
    int mx_element = *max_element(A.begin(), A.end());
    int mn_element = *min_element(A.begin(), A.end());
    if(mx_element==mn_element) return 0;
    vector<int> max_number_bucket(A.size(), INT_MIN);
    vector<int> min_number_bucket(A.size(), INT_MAX);
    for(auto element: A){
        int index = (element - mn_element)*(A.size() - 1) / (mx_element - mn_element);
        max_number_bucket[index] = max(max_number_bucket[index], element);
        min_number_bucket[index] = min(min_number_bucket[index], element);
    }
    int max_diff = INT_MIN;
    int index1 = 0, index2=1;
    while(index1 < A.size() and index2 < A.size()){
        if(max(max_number_bucket[index2], min_number_bucket[index2])==INT_MAX) 
        {
            index2++;
            continue;
        }
        max_diff = max(max_diff, 
                        max(
                            abs(max_number_bucket[index1] - min_number_bucket[index2]), 
                            abs(max_number_bucket[index1] - min_number_bucket[index2])
                            )
                        );
        index1 = index2;
        index2++;
    }
    return max_diff;
}