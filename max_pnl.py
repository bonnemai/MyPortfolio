

def max_pnl(values):
    ''' I give you 1Y history of closes. What's the max PnL I could have made if I couldn't short sell. '''
    if len(values)>0:
        min_value=values[0]
        max_value=None
        all_pnls=[]
        for value in values:
            if value<min_value:
                min_value=value
                if max_value is not None:
                    all_pnls.append(max_value-min_value)
                    max_value=None
            if max_value is None or max_value<value:
                max_value=value
                all_pnls.append(max_value-min_value)
        if len(all_pnls)>0:
            return max(all_pnls)


print(max_pnl([1,2,3,4])) # should be 3

print(max_pnl([2,5,1,5])) # should be 4