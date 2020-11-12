import subprocess
import re
import time
from subprocess import call
 
f=open('db_list.txt','r')
for line in f:
        r1=line
        r1=r1.strip('\n')
        result=r1.split('_')
        name=result[0]
        shfile=name+'.models.sh'
 
        x=open(shfile,'w+')
        x.write('#!/bin/bash\n')
        x.write('#$ -cwd\n')
        x.write('#$ -l mem_free=16G\n')
        x.write('#$ -l h_vmem=16G\n')
        x.write('#$ -V\n')
 
        x.write("gemini de_novo -d 10 --min-gq 20 \\\n")
        x.write("\t--columns \"chrom, start, end, rs_ids, ref, alt, impact, aa_change, gene, exon, transcript, max_aaf_all, aaf_adj_exac_all, aaf_adj_exac_nfe, exac_num_het, exac_num_hom_alt, aaf_esp_all, aaf_esp_ea, aaf_1kg_all, aaf_1kg_eur, is_conserved, cadd_scaled, gerp_bp_score,  clinvar_sig, clinvar_disease_name, pfam_domain, num_hom_ref, num_het, num_hom_alt, qual, gt_depths, gt_quals\" \\\n")
        x.write("\t--filter \"max_aaf_all <= 0.1 AND impact_severity IN ('HIGH', 'MED')\" \\\n")
        x.write("\t"+r1+" > "+ name + "_de_novo_3-8.txt")
 
        x.write("\n\ngemini comp_hets -d 10 --min-gq 20 \\\n")
        x.write("\t--columns \"chrom, start, end, rs_ids, ref, alt, impact, aa_change, gene, exon, transcript, max_aaf_all, aaf_adj_exac_all, aaf_adj_exac_nfe, exac_num_het, exac_num_hom_alt, aaf_esp_all, aaf_esp_ea, aaf_1kg_all, aaf_1kg_eur, is_conserved, cadd_scaled, gerp_bp_score,  clinvar_sig, clinvar_disease_name, pfam_domain, num_hom_ref, num_het, num_hom_alt, qual, gt_depths, gt_quals\" \\\n")
        x.write("\t--filter \"max_aaf_all <= 0.1 AND impact_severity IN ('HIGH', 'MED')\" \\\n")
        x.write("\t"+r1+" > "+ name + "_comp_hets_3-8.txt")
 
        x.write("\n\ngemini autosomal_recessive -d 10 --min-gq 20 \\\n")
        x.write("\t--columns \"chrom, start, end, rs_ids, ref, alt, impact, aa_change, gene, exon, transcript, max_aaf_all, aaf_adj_exac_all, aaf_adj_exac_nfe, exac_num_het, exac_num_hom_alt, aaf_esp_all, aaf_esp_ea, aaf_1kg_all, aaf_1kg_eur, is_conserved, cadd_scaled, gerp_bp_score,  clinvar_sig, clinvar_disease_name, pfam_domain, num_hom_ref, num_het, num_hom_alt, qual, gt_depths, gt_quals\" \\\n")
        x.write("\t--filter \"max_aaf_all <= 0.1 AND impact_severity IN ('HIGH', 'MED')\" \\\n")
        x.write("\t"+r1+" > "+ name + "_homo_rec_3-8.txt")
 
        x.write("\n\ngemini x_linked_recessive -d 10 --min-gq 20 \\\n")
        x.write("\t--columns \"chrom, start, end, rs_ids, ref, alt, impact, aa_change, gene, exon, transcript, max_aaf_all, aaf_adj_exac_all, aaf_adj_exac_nfe, exac_num_het, exac_num_hom_alt, aaf_esp_all, aaf_esp_ea, aaf_1kg_all, aaf_1kg_eur, is_conserved, cadd_scaled, gerp_bp_score,  clinvar_sig, clinvar_disease_name, pfam_domain, num_hom_ref, num_het, num_hom_alt, qual, gt_depths, gt_quals\" \\\n")
        x.write("\t--filter \"max_aaf_all <= 0.1 AND impact_severity IN ('HIGH', 'MED')\" \\\n")
        x.write("\t"+r1+" > "+ name + "_x_linked_3-8.txt")
 
        x.close()
        toqsub="qsub "+shfile
        call(toqsub,shell=True)
f.close()