import time
import re
from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager
import netconf_client
from lxml import etree
import sys
from paramiko import ssh_exception
from io import StringIO, BytesIO
from typing import List, Dict
class netconf_client_class:
    def __init__(self,
                 host: str = "192.168.1.1",
                 username: str = "admin",
                 password: str = "admin",
                 port: str = "833",
                 logfile: str = "cli"):
        # self.log = log_file_class.log_file(logfile, host)
        # self.log = log_file_class.logger("cli", host)
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.manger = None

    def login(self):
        try:
            session= connect_ssh(host=self.host,port=int(self.port), username=self.username, password=self.password,initial_timeout=10,general_timeout=300)
            self.manager = Manager(session, timeout=1200) 
        except ssh_exception.AuthenticationException as e:
            print('%s authentication failed with the remote netconf server: %s' %(self.host,e))
            sys.exit()
        except Exception as e:
            # connection timeout
            # No connection could be made because the target machine actively refused it
            print('%s Netconf login device failed: %s' %(self.host,e))
            sys.exit()

    
    def close(self):
        if self.manager:
            self.manager.close_session()


    @staticmethod
    def strip_outer_rpc_element(tree):
        if tree.getroot().tag == '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc':
            if len(tree.getroot()) == 1:
                newtree = etree.ElementTree(tree.getroot()[0])
                return newtree
            else:
                print('Request contained more than one outermost element.  Not allowed')
                return None
        else:
            return tree   

        
    def send_rpc(self,rpc=""):
        parser = etree.XMLParser(remove_blank_text=True)
        string_to_send=rpc
        send_raw_string = False
        try:
            tree = etree.parse(StringIO(string_to_send), parser)
        except etree.XMLSyntaxError as e:
            print (e)
            print("Your RPC message does not appear to be valid XML, send it anyway!!!")
            send_raw_string = True
        if not send_raw_string:
            tree_to_send =self.strip_outer_rpc_element(tree)
            if tree_to_send is None:
                return False
            else:
                string_to_send = etree.tostring(tree_to_send.getroot(), pretty_print=True).decode()
        
        try:
            # print ("Your original rpc:\n###\n%s\n###" % string_to_send)
            response=self.manager.dispatch(string_to_send)
            rpc_response=etree.tostring(etree.fromstring(response.xml), pretty_print=True).decode()
            # print(rpc_response)
            return rpc_response
        except netconf_client.error.RpcError as e:  # 这个地方会经常用到，当发送的RPC消息，OLT返回有错误时，都会在这里命中
            print("netconf_client.error.RpcError:")
            rpc_response=e.reply_raw.decode("utf-8")
            # print(rpc_response)
            return rpc_response
        except netconf_client.error.NetconfClientException as e:
            print('netconf_client.error.NetconfClientException: %s' % e)
            # print (string_to_send)
            sys.exit()
        except Exception as e:
            print(f'{self.host} Unknown error occurred: {e}')
            # print (string_to_send)
            sys.exit()
        except:pass



    def get_fields_from_rpc(self,rpc_reply: str = "", fields: List[str]= []) -> Dict[str, str]:
        """
        从 RPC Reply XML 中获取指定字段的值，自动处理命名空间。
        :param rpc_reply: RPC Reply XML 字符串
        :param fields: 需要获取值的字段名列表, like ["name", "type","admin-status", "oper-status","last-change"]
        :return: 字典 {字段名: 值}
        """
        root = etree.fromstring(rpc_reply.encode('utf-8'))
    
        # 构建结果字典
        results = {f: None for f in fields}
        # 等同于如下
        # results = {}
        # for each in fields:
        #     results[each]=None
        # print (results)
        # 遍历所有元素，匹配字段名
        for elem in root.iter():
            localname = etree.QName(elem).localname  #admin-status,oper-status,last-change
            # print (localname)
            if localname in fields:
                text = elem.text.strip() if elem.text and elem.text.strip() else ""
                results[localname] = text
        return results
    
    def get_nodes_from_rpc(self,rpc_reply: str = "", node_name: str ="", fields: List[str]= []) -> Dict[str, str]:

        """
        通用 XML 字段提取函数（不依赖命名空间）
        
        :param xml_string: XML 字符串
        :param node_name: 要提取的节点名称，是RPC消息中的重复字段，例如 获取多个ONT光功率中的'rssi-onu', 或者获取dhcpv4 session中的所有的IP信息。
        :param fields: 节点下要提取的字段列表
        :return: 字典列表 [{field: value}]
        """
        root = etree.fromstring(rpc_reply.encode('utf-8'))
        nodes = root.xpath(f".//*[local-name()='{node_name}']")  # 匹配所有 node_name 节点
        results = []
        for node in nodes:
            entry = {}
            for field in fields:
                elem = node.xpath(f".//*[local-name()='{field}']")
                entry[field] = elem[0].text.strip() if elem else None
            results.append(entry)
        return results
        
        # xml_data = """
        # <config xmlns="http://tail-f.com/ns/config/1.0">
        # <hardware-state xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
        #     <component>
        #     <name>PON_16_XGS</name>
        #     <transceiver-link xmlns="urn:bbf:yang:bbf-hardware-transceivers">
        #         <diagnostics>
        #         <rssi-onu xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hws-xcvr-diagnostics-aug">
        #             <detected-serial-number>ALCLF94A3510</detected-serial-number>
        #             <rssi>-197</rssi>
        #             <v-ani-ref>NS-B1-WM1-ONT01</v-ani-ref>
        #         </rssi-onu>
        #         <rssi-onu xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hws-xcvr-diagnostics-aug">
        #             <detected-serial-number>ALCLF94A7805</detected-serial-number>
        #             <rssi>-202</rssi>
        #             <v-ani-ref>NS-L1-NR02-R1-ONT01</v-ani-ref>
        #         </rssi-onu>
        #         <rssi-onu xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hws-xcvr-diagnostics-aug">
        #             <detected-serial-number>ALCLF94A7836</detected-serial-number>
        #             <rssi>-209</rssi>
        #             <v-ani-ref>NS-L1-NR06-R1-ONT01</v-ani-ref>
        #         </rssi-onu>
        #         <rssi-onu xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hws-xcvr-diagnostics-aug">
        #             <detected-serial-number>ALCLF94A8805</detected-serial-number>
        #             <rssi>-207</rssi>
        #             <v-ani-ref>NS-L1-108-01-ONT01</v-ani-ref>
        #         </rssi-onu>
        #         </diagnostics>
        #     </transceiver-link>
        #     </component>
        # </hardware-state>
        # </config>
        # """