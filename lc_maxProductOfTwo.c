int maxProduct(int* nums, int numsSize){
    int i, j, max, temp;
    
    max = -1;
    
    for(i=0; i<numsSize; i++)
    {
        for(j=i+1; j<numsSize; j++)
        {
            temp = (nums[i]-1) * (nums[j]-1);
            if (max < temp)
                max = temp;
        }
    }

    return max;
