# analysis goals:

- general processing TODO:
- [ ] get important data from mcaps
    - [x] filter based on when MCU mode is in RTD
    - [ ] split into multiple zero-time aligned dataframes when a desired specific, or set of specific, message member(s) change or reach a specific value
    - [ ] be able to have a script that we can run that can mass-convert mcap files to mat files (needs to be threaded)
- [ ] make a script that that checks through all of the mcap files and groups mcap files with the same schemas together

- yaw pid analysis:
- [ ] keep track of configurations that have been used
- [ ] controller error over time correlated with controller config
- [ ] torque differences over time vs current yaw rate

- tcs / launch analysis:
- [ ] be able to overlay many different runs in comparison to the "ideal run" graph
    - [ ] torques vs time
    - [ ] wheel speeds vs time
    - [ ] (controller desired and actual torque) vs time 
- [ ] detect start of launch (detect when accel gets yammed)
