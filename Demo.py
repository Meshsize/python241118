import sys
import timeit

# List와 Tuple의 기본 차이 비교
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("=== List와 Tuple 비교 ===")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}\n")

# 1. 가변성 (Mutability)
print("1. 가변성 (Mutability)")
my_list[0] = 10  # List는 변경 가능
print(f"수정된 List: {my_list}")

try:
    my_tuple[0] = 10  # Tuple은 변경 불가
except TypeError as e:
    print(f"Tuple 수정 불가: {e}")

print("\n")

# 2. 메모리 사용량
print("2. 메모리 사용량")
print(f"List 메모리 크기: {sys.getsizeof(my_list)} bytes")
print(f"Tuple 메모리 크기: {sys.getsizeof(my_tuple)} bytes\n")

# 3. 성능 테스트 (반복문 실행 시간 비교)
print("3. 성능 테스트 (반복문 실행 시간 비교)")

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"List 생성 시간: {list_time:.6f}초")
print(f"Tuple 생성 시간: {tuple_time:.6f}초\n")

# 4. 함수에서 사용
print("4. 함수에서 List와 Tuple 사용")
def process_data(data):
    return sum(data)

print(f"List로 전달: {process_data(my_list)}")
print(f"Tuple로 전달: {process_data(my_tuple)}")
