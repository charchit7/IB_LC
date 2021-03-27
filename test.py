import pyperclip
pyperclip.copy('etl_infa_supte,artemis_appte(GBI AC Repair),etlp_infa_appte,gsf_appte,gbi4p_appte,gbi_hana_supte,aps,gbiedw_appte(EDW),gbi_gbirefp_appte,kafka_etlp_appte,autosys_promotion,gbi_appte,gbibods_aps_supte,etl_appte,rusld,apsedw,pmw_appte')
a = list(pyperclip.paste().split(','))
# print(a)   


pyperclip.copy('gbi_salesp_appte,autosys_promotion,gbi_hana_supte,etl_infa_supte,gbi_logisticsp_appte,gbi_gcaedwp_appte,gbiedw_appte(EDW),autosys_prod(Autosys Job Scheduler),gbi_gotup_appte,aps,etlp(GBI Informatica Platform),gbi_retailp_appte,gbi_appte,gbi_finp_appte,gbitqd_appte(Teradata Admin),etl_appte,gbi_itmssecp_appte,gia,artemis_appte(GBI AC Repair),pmw_appte,gsf_appte,gbibods_aps_supte,gbi_apcarep_appte,edw_artemis(GBI EDW ARTEMIS),apsedw,gbi4p_appte,gbi_mktgp_appte,kafka_etlp_appte')
b = list(pyperclip.paste().split(','))
# print(b)



def cc(arr,arr2):
    temp = []
    for i in arr:
        if i not in arr2:
            temp.append(i)
    return temp

print(cc(b,a))
