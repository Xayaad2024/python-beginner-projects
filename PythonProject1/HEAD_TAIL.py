#this program uses coin to make simulation of randoms
import random
head = 1
tail = 2
def main():
    head_count = 0
    tail_count = 0
    tosses = int(input("How many tosses do you want:"))
    for i in range(tosses):
        number = random.randint(head,tail)
        if number == head:
            print("head")
        else:
            print('tail')
            tail_count += 1
        print(f"the total head is {head_count}")
        print(f"the total tail is {tail_count}")
        print(f"Grand total is {head_count + tail_count}")
main()