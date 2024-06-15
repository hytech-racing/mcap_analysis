# req_requested_rpms = [17100, 17100, 17100, 16335]
requested_rpms = [13694, 12742, 12055, 11983]

 
requested_torques_nm = [11.09, 11.13, 11.54, 12.14]


total = 0
for ind, rpm in enumerate(requested_rpms):
    rads = rpm * .1047166 # rpm to rad
    total += rads * requested_torques_nm[ind] 

print(total)