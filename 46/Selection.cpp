// min to max
void SelectionSort(int arr[], int size)
{
	using namespace std;
	for (int i = 0; i < size; i++)
		for (int j = i + 1; j < size; j++)
			if (arr[j] < arr[i])
				swap(arr[j], arr[i]);
}

// max to min
void ReverseSelectionSort(int arr[], int size)
{
    using namespace std;
    for (int i = 0; i < size; i++)
        for (int j = i + 1; j < size; j++)
            if (arr[j] > arr[i]) // Change '<' to '>'
                swap(arr[j], arr[i]);
}
