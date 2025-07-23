import random

def binary_search(container, desired_item):
    low = 0
    high = len(container) - 1

    while low <= high:
        mid = (high + low) // 2

        if desired_item == container[mid]:
            msg = f"Found {desired_item} in the list at index {mid}."
            return msg
        elif desired_item < container[mid]:
            high = mid - 1
        else:
            low = mid + 1

    msg = f"Could not find {desired_item}."
    return msg
            
def main():
    with open("input.txt") as file:
        info = file.read().split()
        info = [int(num.strip()) for num in info if num.strip()]
    
    info.sort()
    desired_value = random.randrange(1, 20)
    
    result_msg = binary_search(info, desired_value)

    with open("result.txt", "a") as file:
        file.write(f"{result_msg}\n")



if __name__ == "__main__":
    main()