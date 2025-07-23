import random

ilist = [100, 55, 40, 19, 7, 7, 7, 6, 1]

ilist.sort(reverse=True)

t1list = []
t2list = []

sum_t1 = 0
sum_t2 = 0

variance = 1  # desired team size difference. Team 2 will always be the greater team due to team 1 having first pick (they get "best", I should honestly write this to have it select based off highest sum avg)

T = len(ilist)

# Check if a split can happen, otherwise enforce equal teams
if (T - variance) % 2 != 0:
    variance = 0

idealTeamSize = (T - variance) // 2
target_t1 = idealTeamSize
target_t2 = idealTeamSize + variance

# balancing looped, changed to reflect target sizes
for num in ilist:
    if len(t1list) >= target_t1:
        t2list.append(num)
        sum_t2 += num
    elif len(t2list) >= target_t2:
        t1list.append(num)
        sum_t1 += num
    else:
        if sum_t1 <= sum_t2:
            t1list.append(num)
            sum_t1 += num
        else:
            t2list.append(num)
            sum_t2 += num

def shuffle_between_teams(t1, t2, max_swaps=3, balance_tolerance=10):
    t1 = t1.copy()
    t2 = t2.copy()

    for _ in range(max_swaps):
        if not t1 or not t2:
            break

        # Randomly select one player from each team
        p1 = random.choice(t1)
        p2 = random.choice(t2)

        # Do the swap
        t1.remove(p1)
        t2.remove(p2)
        t1.append(p2)
        t2.append(p1)

        # Check balance (optional)
        if abs(sum(t1) - sum(t2)) > balance_tolerance:
            # Revert swap if unbalanced
            t1.remove(p2)
            t2.remove(p1)
            t1.append(p1)
            t2.append(p2)

    return t1, t2

new_t1, new_t2 = shuffle_between_teams(t1list, t2list)
