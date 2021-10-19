subrb_km = [3, 6, 8, 14, 20, 22, 25]
population = [4, 3, 5, 6, 2, 3, 1]

sums_distnces_weighted = [] 

for km_check in range(25):
    temp_diff = 0
    for ind, km_sub_i in enumerate(subrb_km):
       temp_diff += abs(((km_sub_i-km_check)))*population[ind]
    sums_distnces_weighted.append(temp_diff)

print('KMs ranging', sums_distnces_weighted)
print('KM to choose:',sums_distnces_weighted.index(min(sums_distnces_weighted)))
    
