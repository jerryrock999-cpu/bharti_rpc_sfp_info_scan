#import traceback
import traceback
# import pramiko_linux_shell_class
#import db_class
import log_file_class
import os
import time
import re
import sys
import getpass
from netconf_client_class import netconf_client_class
import threading
username = ""
password = ""
import frequent_rpc
cmd_list_nt = []
cmd_list_lt = []
ip_list = []
lock=threading.Lock()
import random

def linux_shell_olt(olt_ip : str):
    print (f"will collect sfp info from OLT {olt_ip}")
    netconf_linux_shell_client = netconf_client_class(
        host=olt_ip, port="830", username="admin", password="admin"
    )
    netconf_linux_shell_client.login()
    output_typeb=netconf_linux_shell_client.send_rpc(frequent_rpc.get_typeb)
    fields_to_get1 = ["name", "serial-num","mfg-name", "model-name","mfg-date","admin-state","oper-state","temperature","supply-voltage"]
    fields_to_get2=["admin-state","oper-state","tx-bias","tx-power-dbm","status"]
    fields_to_get_member=["channel-termination-yang-name-in-olt","service-state"]
    # print (output_typeb)
    typeb_members=netconf_linux_shell_client.get_nodes_from_rpc(rpc_reply=output_typeb,node_name="member-channel-termination",fields=fields_to_get_member)
    typeb_dict={}
    for each in typeb_members:
        # print (each)
        pon_name=each["channel-termination-yang-name-in-olt"].split("_")[-2]
        type_b_role=each["service-state"]
        typeb_dict.update({pon_name:type_b_role})
    # print (typeb_dict)
    # for field, value in typeb_dict.items():
    #     print(f"{field}: {value}")

    # get each PON laser status
    fields_to_get_laser=["port-layer-if", "enabled","laser-on-by-default"]
    output_laser=netconf_linux_shell_client.send_rpc(frequent_rpc.get_laser_status)
    # print (output_laser)
    lasers=netconf_linux_shell_client.get_nodes_from_rpc(rpc_reply=output_laser,node_name="interface",fields=fields_to_get_laser)
    # print (lasers)
    lasers_dict={}
    for each in lasers:
        # print (each)
        ct_name=each["port-layer-if"].split("_")[-2]
        laser_status=each["laser-on-by-default"]
        lasers_dict.update({ct_name:laser_status})
        ct_id=f"ct{ct_name}"
        ct_enable_status=each["enabled"]
        lasers_dict.update({ct_id:ct_enable_status})
    # print (lasers_dict)
    for i in range(1,17):      
        PONSFP_n=f"PONSFP_{i}"
        PON_n_GPON=f"PON_{i}_GPON"
        if f"_{i}_GPON" in output_typeb:
            typeb=typeb_dict.get(f"{i}","none")
        else:
            typeb="no"
        each_pon_laser=lasers_dict.get(f"{i}","none")
        each_ct_enable_status=lasers_dict.get(f"ct{i}","none")

        # get SFP serial info
        output=netconf_linux_shell_client.send_rpc(frequent_rpc.get_pon_sn.strip().replace("PONSFP_n",PONSFP_n))
        values = netconf_linux_shell_client.get_fields_from_rpc(rpc_reply=output, fields=fields_to_get1)
        # print (values)
        if values["serial-num"]:
          entry_sn=[values["name"],values["serial-num"],values['mfg-name'],values['model-name'],values["mfg-date"],values["admin-state"],values["oper-state"],values["temperature"],values["supply-voltage"]]
        else:continue
        # print (entry_sn)
        # get SFP tx power info
        output=netconf_linux_shell_client.send_rpc(frequent_rpc.get_pon_tx.strip().replace("PON_n_GPON",PON_n_GPON))
        values_tx = netconf_linux_shell_client.get_fields_from_rpc(rpc_reply=output, fields=fields_to_get2)
        entry_tx=[values_tx["admin-state"],values_tx["oper-state"],values_tx["tx-bias"],values_tx["tx-power-dbm"],values_tx["status"],typeb]

        # get olt version
        output=netconf_linux_shell_client.send_rpc(frequent_rpc.get_olt_version)
        values_version=netconf_linux_shell_client.get_fields_from_rpc(rpc_reply=output, fields=["software-release"])
        olt_version=[values_version["software-release"]]
        each_entry=[olt_ip]+ entry_sn + entry_tx + [each_pon_laser] +[each_ct_enable_status] + olt_version
        
        # print (each_entry)
        # for field, value in values.items():
        #     print(f"{field}: {value}")
        with lock:
          summary.workbook_append(each_entry)
    netconf_linux_shell_client.close()


def eacholt_withoute(olt_ip):
    if olt_ip.strip() and compile_ip.search(olt_ip):
        olt_ip = olt_ip.strip()
        try:
            linux_shell_olt(olt_ip)
        # except SystemExit:
        #     print ("SystemExit!")
        # Exception 基类不包含SystemExit异常
        except:
            print("%s hit an exception!" % (olt_ip))
            traceback.print_exc()
            each_entry = [olt_ip, "login error"]
            with lock:
                summary.workbook_append(each_entry)


if __name__ == "__main__":
    time_start = time.time()

    compile_ip = re.compile(
        r'^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$'
    )

    # runtime = p[2]
    olt_cfg = open("olt_info", "r")
    ip_list = olt_cfg.readlines()
    olt_cfg.close()
    file_create_time = time.strftime("_%Y%m%d_%H%M%S")
    summary = log_file_class.excel_tool("scan_result" + file_create_time)
    summary.workbook_rewrite([["olt_ip","name", "serial-num","mfg-name", "model-name","mfg-date","admin-state","oper-state","temperature","supply-voltage","admin-state","oper-state","tx-bias","tx-power-dbm","status","typeb","laser","ct_enable_status","olt-version"]])
    # linux_shell_olt()
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(max_workers=16) as executor:
        for each_ip in ip_list:
            executor.submit(eacholt_withoute,olt_ip=each_ip)
    time_end = time.time()
    print("Script consume time:", int(time_end - time_start))
