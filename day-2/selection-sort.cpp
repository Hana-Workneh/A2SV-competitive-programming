class Solution
{
    public:
    int select(int arr[],int i){
        return arr[i];
    }
    void selectionSort(int arr[],int n){
        for(int i=0;i<n;i++){
            int indexOfMinimum=i;
            for(int j=i+1;j<n;j++){
                if(arr[j] < arr[i]){
                    indexOfMinimum=j;
                    if(indexOfMinimum != i){
                         swap(arr[j],arr[i]);
                    }
                }
            }
        }
    }
};
