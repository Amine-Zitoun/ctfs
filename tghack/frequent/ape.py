import string
from string import uppercase
latters = uppercase
# AFTER FREQUENCY ANALYSIS WE FIND THAT Q IS THE MOST REPEATED WORD IN THE CIPHER
#
OFFSET= latters.index('Q') - latters.index('E')
enc_str = """U tmhq x0awqp mf kag. Kag mdq zaf xuwq yq. Kagd iadxp...ue...m...rmudkfmxq nqomgeq ymzk oazrxuofuzs fdgfte omz qjuef 
mf Gn20{urpvaqvaz_ufqz_rp}
ftq 
ND20{emyq_fuyq}. U my purrqdqzf. Rad_yq_ftqqdq mdq azx333333k azqe mzp lqdae. M lqqqda omz!zaf!mxea!nq!m!azq. Rad MO20{kag_uf_omz} ea kag ymwq gb efaduqe. Rad yq
ftqdq mdq za efaduqe mzp ftqdqradq ==za mofuaze. Kag ftuzw883333kag  omz ymwq FM20{bqqcfcv_bxst_tcs}
FS20{nqsuzzuzs_yuppxq_qzp}
MZ20{zpfarqqqpwffqfm_evdw_hff}
WL20{afdfp_jfafib_bka} YQ20{moffuaz_iuftagf_efadk?} Ftqdq~ue~zaftuzs~rad yq== fa pa. Za efmdfuzs bauzf.... FG20{iffebjeff_iedzla_yu}
ad qzpuzs bauzf QZP. 
Mzp qhqdk efadk tme m nqsuzzuzs yuppxq*mzp*qzp. Ftdagsta{gf----fuyq-U-vgef} qjuef. Yadq*xasuo, xqee--mofuaze rad yq."""
new_str =''
for i in enc_str:
	if i.upper() in latters:
		new_str += latters[latters.index(i.upper())-OFFSET]
	else:
		new_str += i
print new_str
# FLAG = TG20{beginning_middle_end}
