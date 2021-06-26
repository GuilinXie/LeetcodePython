# https://lei-d.gitbook.io/leetcode/recursion/tower-of-hanoi


def tower_of_hanoi(n):
    def helper(n, from_rod, to_rod, aux_rod):
        if n == 1:
            print("move disk 1 from ", from_rod, " to ", to_rod)
            return
        # move top n-1 disks to aux_rod
        helper(n - 1, from_rod, aux_rod, to_rod)
        # move the nth disk to to_rod
        print("Move disk ", n, " from rod ", from_rod, " to rod ", to_rod)
        # move top n-1 disks to to_rod
        helper(n - 1, aux_rod, to_rod, from_rod)

    helper(n, "A", "B", "C")


if __name__ == "__main__":
    tower_of_hanoi(3)
