// min to max
void BubbleSort(int arr[], int size)
{
    using namespace std;
    for (int i = 0; i < size; i++)
        for (int j = size - 1; j > i; j--)
            if (arr[j] < arr[j - 1]) // Change '>' to '<'
                swap(arr[j], arr[j - 1]);
}

// max to min
void reverseBubbleSort(int arr[], int size)
{
	using namespace std;
	for (int i = 0; i < size; i++)
		for (int j = size - 1; j > i; j--)
			if (arr[j] > arr[j - 1])
				swap(arr[j], arr[j - 1]);
}