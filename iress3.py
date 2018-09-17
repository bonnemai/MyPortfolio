
def get_smallest_numerical_value(phone_numbers):
    map_num_value_phone_nb={}
    smallest_num_value=10**10
    for phone_number in phone_numbers:
        num_value=int(phone_number.replace('-', ''))
        map_num_value_phone_nb[num_value]=phone_number
        if num_value<smallest_num_value:
            smallest_num_value=num_value
    return map_num_value_phone_nb[smallest_num_value]

def solution(S):
    lines=S.split('\n')
    phone_cost={}
    phone_duration={}
    for line in lines:
        l=line.split(',')
        duration=l[0].split(':')
        duration_h=int(duration[0])
        duration_m=int(duration[1])
        duration_s=int(duration[2])
        duration_secs=60*60*duration_h + 60*duration_m + duration_s
        duration_mins=60*duration_h + duration_m
        phone_nb=l[1]
        # <5 mins: 3 cents per sec
        if duration_secs< 5 * 60:
            cost = 3 * duration_secs
        # >5 mins: 150 cents every started min:5:00 = 5 x 150, 5:01 = 6 x 150
        elif duration_s==0:
            cost = 150 * duration_mins
        else:
            cost = 150 * (duration_mins+1)
        if phone_nb in phone_cost:
            phone_cost[phone_nb]+=cost
            phone_duration[phone_nb]+=duration_secs
        else:
            phone_cost[phone_nb]=cost
            phone_duration[phone_nb]=duration_secs

    # Now get Max:
    total_cost = 0
    good_friends_duration=-1
    for phone_nb in phone_cost:
        total_cost+=phone_cost[phone_nb]
        if phone_duration[phone_nb]>good_friends_duration:
            good_friends_duration=phone_duration[phone_nb]
            # good_friend_cost=phone_cost[phone_nb]

    # Get all friends with the same duration
    # good_friend_cost=-1
    good_friends_numbers=[]
    for phone_nb in phone_duration:
        if phone_duration[phone_nb]==good_friends_duration:
            good_friends_numbers.append(phone_nb)

    # Longest total duration = free
    # Tie...
    free_number=get_smallest_numerical_value(good_friends_numbers)

    return total_cost-phone_cost[free_number]

_str=  "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
# _str=  "00:01:07,400-234-090\n00:01:07,701-080-080"

nbs=  ["400-234-090", "701-080-080"]
print(get_smallest_numerical_value(nbs))
print(solution(  _str))
