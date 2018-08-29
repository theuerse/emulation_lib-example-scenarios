#!/bin/sh
# enter sudo pwd as needed, only checks if the IFB module is available

sudo modprobe ifb
sudo ip link set dev ifb0 up
echo "<IFB module>"
lsmod | grep ifb
echo "</IFB module>"
echo "<network interfaces>"
ip link
echo "</network interfaces>"
sudo modprobe -r ifb


# If you use link cmd backends which utilize the IFB,
# you have to ensure that at least one IFB-device (ifb0)
# is loaded / usable before starting the emulations

# One way to achieve this, is to set the number of ifbs at boot (only one needed)
# https://elixir.bootlin.com/linux/v2.6.22-rc4/source/drivers/net/ifb.c
# https://forum.armbian.com/topic/3125-kernel-boot-arguments/
# sudo vim /boot/armbianEnv.txt
# add the following
# extraargs=ifb.numifbs=1
