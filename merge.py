def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 배열을 반으로 나누기
        left_half = arr[:mid]
        right_half = arr[mid:]
        #print("{} {}".format(left_half,right_half))
        merge_sort(left_half)  # 왼쪽 반 정렬
        merge_sort(right_half)  # 오른쪽 반 정렬

        # 정렬된 두 반을 병합
        i, j, k = 0, 0, 0      #i는 왼쪽 리스트 인덱스 , j는 오른쪽 리스트 인덱스, k는 정렬된 정보를 넣는 리스트 인덱스
        while i < len(left_half) and j < len(right_half):  #나눠진 리스트 하나가 다 소모될때 까지
            if left_half[i] < right_half[j]:  #왼쪽 리스트가 더 작을 때 왼쪽 리스트의 요소를 넣음
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]  #오른쪽 리스트가 더 작을 때 오른쪽 리스트의 요소를 넣음
                j += 1
            k += 1

        # 남은 요소들 복사
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# 예제 사용
merge_list = [5, 10, 7, 9, 3, 1, 1, 2, 5, 4, 6, 7, 12, 11, 8]
print("정렬 전: {}".format(merge_list))

merge_sort(merge_list)

print("정렬 후: {}".format(merge_list))
