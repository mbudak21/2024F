# What is DevOps?
Developer + Operations

DevOps aims to achieve the following:
- Faster time to market
- Lower failure rate of new releases
- Faster time to recovery in the event of crashes, etc
- Improved deployment frequency 
- ...

By doing the below:
- Automating the building of both infrastructure and applications. 
- Applies a series of automated tests to infrastructure and applications.
- Automates the **deployment** to end-users. 
# Skipping the Linux stuff
Forgot how to use tee tho

# Raid

## Raid 0 - Stripping
Uses both disks as one big volume.

## Raid 1 - Mirroring
Mirrors one disk to another. Reads are faster, writes are same.

## Raid 5 - Stripping + Parity
Needs at least 3 disks, if 1 disk fails its contents can be calculated from the other disks. 