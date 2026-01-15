arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicate elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == K:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                # Skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < K:
                left += 1
            else:
                right -= 1

    return result


# Example usage
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(three_sum(arr))
