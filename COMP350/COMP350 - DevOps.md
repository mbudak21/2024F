# Lecture 1
## What is DevOps?
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
# Lecture 2-3 - Linux Bash
- File names are case sensitive
- `mkdir dir1 dir2`
- Hard link: `ln file link` e.g.: `ls data.jpg hardlink.jpg`
	1. A hard link cannot reference a file outside its own file system.
	2. Hard links can't reference directories.
	3. Hard links are indistinguishable from the file itself.
- Sym link: `ln -s item link`
	Creates a text pointer to the file.
- `$which ls > /usr/bin/ls` 

## chmod
 U     G    W 
000 000 000 -> bits (enable disable)
rw_rwx___x -> 110 111 001 -> 671
rw_rw_r__   -> 110 110 100 -> 664

## Raid

### Raid 0 - Stripping
Uses both disks as one big volume.

### Raid 1 - Mirroring
Mirrors one disk to another. Reads are faster, writes are same.

### Raid 5 - Stripping + Parity
Needs at least 3 disks, if 1 disk fails its contents can be calculated from the other disks. 

---
# Lectures 6-X