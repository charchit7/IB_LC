Newark:
======
SQL> select count(1),machine,username,terminal from v$session where upper(username)=upper('ORADBA') group by machine,username,terminal order by machine;
       COUNT(1) MACHINE
--------------- ----------------------------------------------------------------
USERNAME                                                                                                                         TERMINAL
-------------------------------------------------------------------------------------------------------------------------------- ------------------------------
              1 dandelion
ORADBA                                                                                                                           pts/1
              1 dandelion
ORADBA                                                                                                                           pts/4
2 rows selected.
/ngs/app/qtldrnp>
/ngs/app/qtldrnp> find . -exec grep -iHn "**********************" '{}' \; -print
1:connect ORADBA@qtldrnp/**********************
./work/App_Monitroing/connect_oradba.sql
1:connect ORADBA@qtldrnp/**********************
./work/aakarsh/connect.sql
1:sqlplus ORADBA@qtldrnp/**********************
./work/om/connect.sql
1:connect ORADBA@qtldrnp/**********************
./work/om/connect_oradba.sql
1:sqlplus ORADBA@qtldrnp/**********************
./work/om/neet/connect.sql
1:sqlplus ORADBA@qtldrnp/**********************
./work/patkar/connect_oradba.sql
1:sqlplus ORADBA@qtldrnp/**********************
./work/pdp/connect.sql
16:qtldrnp=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
22:qtldrmp=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
./work/pdp/sap_quote/p.ksh
16:qtldrnp=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
22:qtldrmp=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
./work/pdp/sap_quote/sap_quote_monitor.ksh
1:display =`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
./work/pdp/sap_quote/test.ksh
1:display1=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
./work/pdp/sap_quote/test2.ksh
1:qtldrnp=`sqlplus ORADBA@qtldrnp/********************** <<EOF | grep KEEP | sed 's/KEEP//;s/[ ]//g'
./work/pdp/sap_quote/test4.ksh
1:count=`sqlplus ORADBA@qtldrnp/********************** <<EOF
./work/pdp/sap_quote/text.ksh
1:sqlplus ORADBA@qtldrnp/**********************
./work/ramesh/connect.sql
1:. /ngs/app/qtldrnp/SCRIPTS/KSH/Safesql.ksh oradba@qtldrnp/**********************
./work/ramesh/sfcon.sql
/ngs/app/qtldrnp>
Maiden:
======
SQL> select count(1),machine,username,terminal from v$session where upper(username)=upper('ORADBA') group by machine,username,terminal order by machine;
       COUNT(1) MACHINE
--------------- ----------------------------------------------------------------
USERNAME                                                                                                                         TERMINAL
-------------------------------------------------------------------------------------------------------------------------------- ------------------------------
              1 dagda
ORADBA                                                                                                                           pts/3
1 row selected.
/ngs/app/qtldrmp>
/ngs/app/qtldrmp> find . -exec grep -iHn "**********************" '{}' \; -print
1:connect ORADBA@qtldrmp/**********************
./work/aakarsh/connect.sql
1:sqlplus ORADBA@qtldrmp/**********************
./work/om/connect.sql
1:connect ORADBA@qtldrmp/**********************
./work/om/connect_oradba.sql
1:sqlplus ORADBA@qtldrmp/**********************
./work/pdp/connect.sql
1:connect ORADBA@qtldrmp/**********************
./work/pdp/connect_oradba.sql
2:oradba@qtldrmp/**********************
./work/pdp/spool.ksh
1:sqlplus ORADBA@qtldrmp/**********************
./work/ramesh/connect.sql
/ngs/app/qtldrmp>



oradba@qtldrnp     :    G00d_bY3_Qu4r4Nt1E
oradba@qtldrmp    :    G00d_bY3_Qu4r4Nt1E
Related CR: https://cst.apple.com/tkt.do?tkt=CHG000244682 - Password change for ORADBA@ QTLDRMP and QTLDRNP

for impact analysis we check for barcodings and sessions




ssh c5020167@dandelion
su - qtldrnp
A1LdB35T_m4dHU
cd work/pdp/connect.sql
ssh c5020167@dagda
su - qtldrmp
l3t_it4T_p3acE
cd work/pdp/connect.sql


login here and fir this command: find . -exec grep -iHn "**********************" '{}' \; -print    #what this command does is that it checks for the password in the filesystem 
#that greap does that , so that we can change the password

https://cst.apple.com/tkt.do?tkt=CHG000294141 - [APS-CR]Password changes in QTLDRNP and QTLDRMP
[5:33 PM] check this CR,, I raised this for QTLDR_BO_USER@qtldrmp
and QTLDR_BO_USER@qtldrnp password change
[5:33 PM] fror any password change we need one risk 3 CR




5:27
oradba@qtldrnp     :    G00d_bY3_Qu4r4Nt1E
oradba@qtldrmp    :    G00d_bY3_Qu4r4Nt1E



