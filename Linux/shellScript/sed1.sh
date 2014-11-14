#!/bin/bash

#replace the "" with NA
sed "s/\"\"/NA/g" tcsv1.txt >tcsv2.txt

#replace the "" with empty space
sed "s/\"\"//g" tcsv1.txt >tcsv2b.txt



# $ cat pets.txt
# This is my cat
#   my cat's name is betty
# This is my dog
#   my dog's name is frank
# This is my fish
#   my fish's name is george
# This is my goat
#   my goat's name is adam

$ sed "3s/my/your/g" pets.txt
# This is my cat
#   my cat's name is betty
# This is your dog
#   my dog's name is frank
# This is my fish
#   my fish's name is george
# This is my goat
#   my goat's name is adam


#list the top 10 process cost most memory
ps aux | sort -nk +4 | tail


ssh user@server bash < /path/to/local/script.sh
# 在远程机器上运行一段脚本。这条命令最大的好处就是不用把脚本拷到远程机器上。
ssh user@host cat /path/to/remotefile | diff /path/to/localfile -
# 比较一个远程文件和一个本地文件
net rpc shutdown -I ipAddressOfWindowsPC -U username%password
# 远程关闭一台Windows的机器