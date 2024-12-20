// min to max
void ShakerSort(int arr[], int size)
{
	for (int i = 1; i < size; i++)
	{
		int key = arr[i];
		int j;
		for (j = i - 1; j >= 0 && arr[j] > key; j--)
		{
			arr[j + 1] = arr[j];
		}
		arr[j + 1] = key;
	}
}

// max to min
void ReverseShakerSort(int arr[], int size)
{
    for (int i = 1; i < size; i++)
    {
        int key = arr[i];
        int j;
        for (j = i - 1; j >= 0 && arr[j] < key; j--) // Change '>' to '<'
        {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;
    }
}
