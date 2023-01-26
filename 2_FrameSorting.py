import random

# Sorting the Frames
def sortFrame( frame ):
    frame.sort()
    return frame

def main():
    frame = list([])
    print("Enter the number of Frames >> ")
    n = int(input())

    for i in range(n):
        seqNum = random.randint(1, 10000)
        print(f'Enter the data for {i+1}th frame >> ')
        data = int(input())

        frame.append([seqNum, data])

    print("\n\nBefore Sorting >> ")
    for i in frame:
        print(f'Seq. Num -> {i[0]}, Data -> {i[1]}')
    
    frame = sortFrame(frame)

    print("\n\nAfter Sorting >> ")
    for i in frame:
        print(f'Seq. Num -> {i[0]}, Data -> {i[1]}')


if __name__ == "__main__":
    main()