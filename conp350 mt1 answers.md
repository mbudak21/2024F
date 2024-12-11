# 1
1. `ls *.txt LOG | cat >> LOG-all.txt`
2. Its a variable that persists on a shell session, some are user defined, some are system defined. For example, $SESSION variable could be user defined and $SHELL variable could be system defined. 
3. First, we can't create a hard link of a file outside of the current file system. Second, we can't reference a dir.
4. `rw_r_____ -> 110 100 000 -> 640` > `chmod 640 file`
5. use tee, cat data | tee file.txt
6. pwd
7. sudo --user "user"
# 2
1. /dev/sdc2
2. Raid 0 has no backup disks, its faster. Raid 2 uses some backup disks.
3. /etc/fstab.conf
4. Plug it in > find its /dev name > `mount <device-name> /mnt/usb`
5. use lsblk to find the name of the partition, use fdisk to format it to ext4.
6. Yes you can, you can use btrfs and ext4 at the same time for example. Or if you dual boot Linux with windows, the windows partition will use NTFS while the Linux partition can use a different FS such as ext4.
# 3
1. The router. ipv4 or ipv6.
2. ?
3. Depending on the configuration, usually in Turkey as far as I know, there is no guarrantee that the user will get the same public IP address. So most of the time the public IP address is changed.
4. The outside traffic comes in the form of a public IP, the NAT has a list that maps the Public IP to a port in the local network. And using this the NAT forwards the incoming traffic to this device.
5. We need docker networks to enable communication via networks between our containers. For example, we can connect a mysql db container to our app container using docker networks. This configuration also helps us make sure we can use the same config if we decide to put the database on a server and the app on a different device.
6. It enables the mapping of incoming traffic addressed to a specific IP and a Port, to a different IP and maybe a different port in the Public Networks. This protects the inner device from being exposed completely, and only exposes the port needed.
7. This ip is used to address the device in the local network. The router and other devices in the network use this address to talk to the users device.
8. It gets assigned both, private one for communication between the router and the device, public one for other stuff.
# 4.
1. `docker exec -it  <container-name> /bin/bash`
2. map those files using VOLUME
3. ?
4. docker-compose up
5. ?
6. ?
7. ?
8. ADD lets the adding of URLs from internet unluke COPY.
9. I'm guessing that OS-level would be more compatible across devices which run the same OS?
10. ENV ?
11. For persistent storage