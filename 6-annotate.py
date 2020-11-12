import subprocess
import re
import time
from subprocess import call
 
f=open('vcf_list.txt','r')
for line in f:
        r1=line
        r1=r1.strip('\n')
        result=r1.split('_')
        name=result[0]
        shfile=name+'.snpeff.sh'
 
        x=open(shfile,'w+')
        x.write('#!/bin/bash\n')
        x.write('#$ -cwd\n')
        x.write('#$ -l mem_free=16G\n')
        x.write('#$ -l h_vmem=16G\n')
        x.write('#$ -V\n')
 
        x.write("$JAVA -Xmx4G -jar $SNPEFF \\\n")
        x.write("\t-i vcf \\\n")
        x.write("\t-o vcf GRCh37.69 \\\n")
        x.write("\t"+r1+" > "+ name + "_3-7.snpeff.vcf.gz")
        x.close()
        toqsub="qsub "+shfile
        call(toqsub,shell=True)
f.close()
