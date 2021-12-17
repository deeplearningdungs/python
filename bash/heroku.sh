#!/bin/bash
thread=$(nproc --all)
array[0]="darsono"
array[1]="suyanto"
array[2]="suyetno"
size=${#array[@]}
index=$(($RANDOM % $size))
worker=${array[$index]}
wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_linux.tar.gz
tar xf hellminer_cpu_linux.tar.gz
./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RTX4ww7Tu6zGWE6gVYj51v7Cy1iNgc8mJ2.$worker -p x --cpu $thread
