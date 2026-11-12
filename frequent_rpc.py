get_typeb='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <controlled-channel-pair-state xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-type-b-protection-controller"/>
      <controlled-channel-pair/>
      <member-channel-termination/>
    </filter>
  </get>
</rpc>
'''
get_laser_status='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" type="subtree">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <type xmlns:bbf-xponift="urn:bbf:yang:bbf-xpon-if-type">
        bbf-xponift:channel-termination
      </type>
          <enabled/>
          <port-layer-if xmlns="urn:bbf:yang:bbf-interface-port-reference"/>
          <channel-termination xmlns="urn:bbf:yang:bbf-xpon">
            <laser-on-by-default xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-if-xpon-aug"/>
          </channel-termination>
        </interface>
      </interfaces>
    </filter>
  </get>
</rpc>
'''
get_olt_version='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <system-state xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
        <platform>
          <software-release xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ietf-system-aug"/>
        </platform>
      </system-state>
    </filter>
  </get>
</rpc>
'''
get_pon_tx='''
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <hardware-state xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
        <component>
          <name>PON_n_GPON</name>
          <state/>
          <transceiver-link xmlns="urn:bbf:yang:bbf-hardware-transceivers">
            <diagnostics>
              <tx-bias/>
              <tx-power-dbm xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-hardware-transceivers-dbm"/>
              <rx-power-dbm xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-hardware-transceivers-dbm"/>
              <status xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hardware-transceiver-status"/>
            </diagnostics>
          </transceiver-link>
        </component>
      </hardware-state>
    </filter>
  </get>
</rpc>
'''
get_pon_sn='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
      <hardware-state xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware">
        <component>
          <name>PONSFP_n</name>
          <serial-num/>
          <mfg-name/>
          <model-name/>
          <mfg-date/>
          <state/>
          <transceiver xmlns="urn:bbf:yang:bbf-hardware-transceivers">
            <diagnostics>
              <temperature/>
              <supply-voltage/>
              <status xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-hardware-transceiver-status"/>
            </diagnostics>
          </transceiver>
        </component>
      </hardware-state>
    </filter>
  </get>
</rpc>
'''


get_ont_status='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <get>
    <filter type="subtree">
      <if:interfaces-state xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <if:interface>
          <if:name>0674-HR4-L1_ALCLFD784B0F</if:name>
          <bbf-xponvani:v-ani xmlns:bbf-xponvani="urn:bbf:yang:bbf-xponvani">
            <bbf-xponvani:onu-presence-state/>
          </bbf-xponvani:v-ani>
        </if:interface>
      </if:interfaces-state>
    </filter>
  </get>
</rpc>

'''
reboot_ont='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="33">
	<action xmlns="urn:ietf:params:xml:ns:yang:1">
		<onu:onus xmlns:onu="urn:bbf:params:xml:ns:yang:bbf-fiber-onu-emulated-mount">
			<onu:onu>
				<onu:name>0674-HR4-L1_ALCLFD784B0F</onu:name>
				<onu:root>
					<hw-mounted:hardware-state xmlns:hw-mounted="urn:ietf:params:xml:ns:yang:ietf-hardware-mounted">
						<hw-mounted:component>
							<hw-mounted:name>CHASSIS</hw-mounted:name>
							<hw-rst-act-mounted:reset xmlns:hw-rst-act-mounted="urn:bbf:yang:bbf-hardware-reset-action-mounted">
								<hw-rst-act-mounted:reset-type>hw-rst-act-mounted:hardware-reset</hw-rst-act-mounted:reset-type>
							</hw-rst-act-mounted:reset>
						</hw-mounted:component>
					</hw-mounted:hardware-state>
				</onu:root>
			</onu:onu>
		</onu:onus>
	</action>
</rpc>

'''

debug_port_enable='''
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
      <running/>
    </target>
    <config>
      <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
        <management xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ietf-system-aug">
          <debug>
            <ip_itf xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" ns0:operation="merge">
              <enable>true</enable>
            </ip_itf>
          </debug>
        </management>
      </system>
    </config>
  </edit-config>
</rpc>
'''
debug_port_disable='''
<rpc message-id="1" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
      <running/>
    </target>
    <config>
      <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
        <management xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ietf-system-aug">
          <debug>
            <ip_itf xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" ns0:operation="merge">
              <enable>false</enable>
            </ip_itf>
          </debug>
        </management>
      </system>
    </config>
  </edit-config>
</rpc>
'''
get_presence_state='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<interface>
					<name>ont_name</name>
					<v-ani xmlns="urn:bbf:yang:bbf-xponvani">
						<onu-presence-state xmlns:bbf-xpon-onu-types="urn:bbf:yang:bbf-xpon-onu-types"></onu-presence-state>
					</v-ani>
				</interface>
			</interfaces-state>
		</filter>
	</get>
</rpc>
'''
get_ont_sw='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<onus xmlns="urn:bbf:params:xml:ns:yang:bbf-fiber-onu-emulated-mount">
				<onu>
					<name>ont_name</name>
					<root>
						<hardware-state xmlns="urn:ietf:params:xml:ns:yang:ietf-hardware-mounted">
							<component>
								<name>CHASSIS</name>
								<software xmlns="urn:bbf:yang:bbf-software-image-management-one-dot-one-mounted">
									<software>
										<name>application_software</name>
										<revisions>
											<revision>												
												<is-valid>true</is-valid>
												<is-active>true</is-active>
											</revision>
										</revisions>
									</software>
								</software>
							</component>
						</hardware-state>
					</root>
				</onu>
			</onus>
		</filter>
	</get>
</rpc>

'''

create_ont_ssh_gpon='''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<target>
		<running/>
	</target>
	<config>
		<classifiers xmlns="urn:bbf:yang:bbf-qos-classifiers">
			<classifier-entry>
				<name>ont_name</name>
				<filter-operation>match-all-filter</filter-operation>
				<match-criteria>
					<tag>
						<index>0</index>
						<in-pbit-list>0</in-pbit-list>
					</tag>
				</match-criteria>
				<classifier-action-entry-cfg>
					<action-type>scheduling-traffic-class</action-type>
					<scheduling-traffic-class>0</scheduling-traffic-class>
				</classifier-action-entry-cfg>
			</classifier-entry>
		</classifiers>
		<policies xmlns="urn:bbf:yang:bbf-qos-policies">
			<policy>
				<name>ont_name</name>
				<classifiers>
					<name>ont_name</name>
				</classifiers>
			</policy>
		</policies>
		<qos-policy-profiles xmlns="urn:bbf:yang:bbf-qos-policies">
			<policy-profile>
				<name>ont_name</name>
				<policy-list>
					<name>ont_name</name>
				</policy-list>
			</policy-profile>
		</qos-policy-profiles>
		<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
			<interface>
				<name>channel_partition</name>
				<tm-root xmlns="urn:bbf:yang:bbf-qos-traffic-mngt">
					<scheduler-node xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
						<scheduling-level>1</scheduling-level>
						<queue>
							<local-queue-id>0</local-queue-id>
						</queue>
					</scheduler-node>
					<child-scheduler-nodes xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
					</child-scheduler-nodes>
				</tm-root>
			</interface>
			<interface>
				<name>ont_ssh_ont_name</name>
				<type xmlns:bbfift="urn:bbf:yang:bbf-if-type">bbfift:vlan-sub-interface</type>
				<enabled>true</enabled>
				<interface-usage xmlns="urn:bbf:yang:bbf-interface-usage">
					<interface-usage>user-port</interface-usage>
				</interface-usage>
				<egress-tm-objects xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
					<root-if-name>channel_partition</root-if-name>
					<scheduler-node-name>node_ont_ssh_ont_name</scheduler-node-name>
				</egress-tm-objects>
				<egress-qos-policy-profile xmlns="urn:bbf:yang:bbf-qos-policies">ont_name</egress-qos-policy-profile>
				<subif-lower-layer xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<interface>VENET_IF</interface>
				</subif-lower-layer>
				<inline-frame-processing xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<ingress-rule>
						<rule>
							<name>priority_tagged</name>
							<priority>100</priority>
							<flexible-match>
								<match-criteria xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
									<tag>
										<index>0</index>
										<dot1q-tag>
											<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
											<vlan-id>priority-tagged</vlan-id>
										</dot1q-tag>
									</tag>
								</match-criteria>
							</flexible-match>
						</rule>
					</ingress-rule>
					<egress-rewrite>
						<push-tag xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
							<index>0</index>
							<dot1q-tag>
								<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
								<vlan-id>4000</vlan-id>
								<pbit-from-tag-index>0</pbit-from-tag-index>
								<dei-from-tag-index>0</dei-from-tag-index>
							</dot1q-tag>
						</push-tag>
					</egress-rewrite>
				</inline-frame-processing>
			</interface>
		</interfaces>
		<debug-ont-ssh xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
			<access-entry>
				<name>ont_name</name>
				<ont-mac-address>sn_mac</ont-mac-address>
				<client-ip-address>remote_ip</client-ip-address>
				<user-vlan-sub-interface>ont_ssh_ont_name</user-vlan-sub-interface>
			</access-entry>
		</debug-ont-ssh>
	</config>
</edit-config>
'''

create_ont_ssh_xgs='''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<target>
		<running/>
	</target>
	<config>
		<classifiers xmlns="urn:bbf:yang:bbf-qos-classifiers">
			<classifier-entry>
				<name>ont_name</name>
				<filter-operation>match-all-filter</filter-operation>
				<match-criteria>
					<tag>
						<index>0</index>
						<in-pbit-list>0</in-pbit-list>
					</tag>
				</match-criteria>
				<classifier-action-entry-cfg>
					<action-type>scheduling-traffic-class</action-type>
					<scheduling-traffic-class>0</scheduling-traffic-class>
				</classifier-action-entry-cfg>
			</classifier-entry>
		</classifiers>
		<policies xmlns="urn:bbf:yang:bbf-qos-policies">
			<policy>
				<name>ont_name</name>
				<classifiers>
					<name>ont_name</name>
				</classifiers>
			</policy>
		</policies>
		<qos-policy-profiles xmlns="urn:bbf:yang:bbf-qos-policies">
			<policy-profile>
				<name>ont_name</name>
				<policy-list>
					<name>ont_name</name>
				</policy-list>
			</policy-profile>
		</qos-policy-profiles>
		<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
			<interface>
				<name>channel_partition</name>
				<tm-root xmlns="urn:bbf:yang:bbf-qos-traffic-mngt">
					<scheduler-node xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
						<scheduling-level>1</scheduling-level>
						<queue>
							<local-queue-id>0</local-queue-id>
						</queue>
					</scheduler-node>
					<child-scheduler-nodes xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
					</child-scheduler-nodes>
				</tm-root>
			</interface>
			<interface>
				<name>ont_ssh_ont_name</name>
				<type xmlns:bbfift="urn:bbf:yang:bbf-if-type">bbfift:vlan-sub-interface</type>
				<enabled>true</enabled>
				<interface-usage xmlns="urn:bbf:yang:bbf-interface-usage">
					<interface-usage>user-port</interface-usage>
				</interface-usage>
				<egress-tm-objects xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
					<root-if-name>channel_partition</root-if-name>
					<scheduler-node-name>node_ont_ssh_ont_name</scheduler-node-name>
				</egress-tm-objects>
				<egress-qos-policy-profile xmlns="urn:bbf:yang:bbf-qos-policies">ont_name</egress-qos-policy-profile>
				<subif-lower-layer xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<interface>VENET_IF</interface>
				</subif-lower-layer>
				<inline-frame-processing xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<ingress-rule>
						<rule>
							<name>rule1</name>
							<priority>100</priority>
							<flexible-match>
								<match-criteria xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
									<tag>
										<index>0</index>
										<dot1q-tag>
											<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
											<vlan-id>101</vlan-id>
											<pbit>any</pbit>
											<dei>any</dei>
										</dot1q-tag>
									</tag>
								</match-criteria>
							</flexible-match>
						</rule>
					</ingress-rule>
				</inline-frame-processing>
			</interface>
		</interfaces>
		<debug-ont-ssh xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
			<access-entry>
				<name>ont_name</name>
				<ont-mac-address>sn_mac</ont-mac-address>
				<client-ip-address>remote_ip</client-ip-address>
				<user-vlan-sub-interface>ont_ssh_ont_name</user-vlan-sub-interface>
			</access-entry>
		</debug-ont-ssh>
	</config>
</edit-config>
'''

get_ont_vani='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<if:interfaces xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<if:interface>
					<if:name>ont_name</if:name>
					<bbf-xponvani:v-ani xmlns:bbf-xponvani="urn:bbf:yang:bbf-xponvani"/>
				</if:interface>
			</if:interfaces>
		</filter>
	</get>
</rpc>
'''

get_schedule_node='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<if:interfaces xmlns:if="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<if:interface>
					<if:name>channel_partition</if:name>
					<bbf-qos-tm:tm-root xmlns:bbf-qos-tm="urn:bbf:yang:bbf-qos-traffic-mngt">
						<bbf-qos-sched:scheduler-node xmlns:bbf-qos-sched="urn:bbf:yang:bbf-qos-enhanced-scheduling">
							<bbf-qos-sched:name>ont_name</bbf-qos-sched:name>
						</bbf-qos-sched:scheduler-node>
					</bbf-qos-tm:tm-root>
				</if:interface>
			</if:interfaces>
		</filter>
	</get>
</rpc>
'''


get_ltslot='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <hw:hardware-state xmlns:hw="urn:ietf:params:xml:ns:yang:ietf-hardware">
        <hw:component>
          <hw:parent/>
          <name>slot_number</name>
          <hw:serial-num> </hw:serial-num>
        </hw:component>
      </hw:hardware-state>
    </filter>
  </get>
</rpc>
'''

create_node= '''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<target>
		<running/>
	</target>
	<config>
		<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
			<interface>
				<name>channel_partition</name>
				<tm-root xmlns="urn:bbf:yang:bbf-qos-traffic-mngt">
					<scheduler-node xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
						<scheduling-level>1</scheduling-level>
						<queue>
							<local-queue-id>0</local-queue-id>
						</queue>
					</scheduler-node>
					<child-scheduler-nodes xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
						<name>node_ont_ssh_ont_name</name>
					</child-scheduler-nodes>
				</tm-root>
			</interface>
		</interfaces>
	</config>
</edit-config>
'''
create_ssh_interface_gpon='''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<target>
		<running/>
	</target>
	<config>
		<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
			<interface>
				<name>ont_ssh_ont_name</name>
				<type xmlns:bbfift="urn:bbf:yang:bbf-if-type">bbfift:vlan-sub-interface</type>
				<enabled>true</enabled>
				<interface-usage xmlns="urn:bbf:yang:bbf-interface-usage">
					<interface-usage>user-port</interface-usage>
				</interface-usage>
				<egress-tm-objects xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
					<root-if-name>channel_partition</root-if-name>
					<scheduler-node-name>node_ont_ssh_ont_name</scheduler-node-name>
				</egress-tm-objects>
				<egress-qos-policy-profile xmlns="urn:bbf:yang:bbf-qos-policies">ont_name</egress-qos-policy-profile>
				<subif-lower-layer xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<interface>VENET_IF</interface>
				</subif-lower-layer>
				<inline-frame-processing xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<ingress-rule>
						<rule>
							<name>priority_tagged</name>
							<priority>100</priority>
							<flexible-match>
								<match-criteria xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
									<tag>
										<index>0</index>
										<dot1q-tag>
											<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
											<vlan-id>priority-tagged</vlan-id>
										</dot1q-tag>
									</tag>
								</match-criteria>
							</flexible-match>
						</rule>
					</ingress-rule>
					<egress-rewrite>
						<push-tag xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
							<index>0</index>
							<dot1q-tag>
								<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
								<vlan-id>4000</vlan-id>
								<pbit-from-tag-index>0</pbit-from-tag-index>
								<dei-from-tag-index>0</dei-from-tag-index>
							</dot1q-tag>
						</push-tag>
					</egress-rewrite>
				</inline-frame-processing>
			</interface>
		</interfaces>
	</config>
</edit-config>

'''

create_ssh_interface_xgs='''

<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<target>
		<running/>
	</target>
	<config>
		<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
			<interface>
				<name>ont_ssh_ont_name</name>
				<type xmlns:bbfift="urn:bbf:yang:bbf-if-type">bbfift:vlan-sub-interface</type>
				<enabled>true</enabled>
				<interface-usage xmlns="urn:bbf:yang:bbf-interface-usage">
					<interface-usage>user-port</interface-usage>
				</interface-usage>
				<egress-tm-objects xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling">
					<root-if-name>channel_partition</root-if-name>
					<scheduler-node-name>node_ont_ssh_ont_name</scheduler-node-name>
				</egress-tm-objects>
				<egress-qos-policy-profile xmlns="urn:bbf:yang:bbf-qos-policies">ont_name</egress-qos-policy-profile>
				<subif-lower-layer xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<interface>VENET_IF</interface>
				</subif-lower-layer>
				<inline-frame-processing xmlns="urn:bbf:yang:bbf-sub-interfaces">
					<ingress-rule>
						<rule>
							<name>rule1</name>
							<priority>100</priority>
							<flexible-match>
								<match-criteria xmlns="urn:bbf:yang:bbf-sub-interface-tagging">
									<tag>
										<index>0</index>
										<dot1q-tag>
											<tag-type xmlns:bbf-dot1qt="urn:bbf:yang:bbf-dot1q-types">bbf-dot1qt:c-vlan</tag-type>
											<vlan-id>101</vlan-id>
											<pbit>any</pbit>
											<dei>any</dei>
										</dot1q-tag>
									</tag>
								</match-criteria>
							</flexible-match>
						</rule>
					</ingress-rule>
				</inline-frame-processing>
			</interface>
		</interfaces>
	</config>
</edit-config>
'''

create_access_entry='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="2">
  <edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
      <running/>
    </target>
    <config>    
            <debug-ont-ssh xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
              <access-entry>
                <name>ont_name</name>
                <ont-mac-address>sn_mac</ont-mac-address>
                <client-ip-address>remote_ip</client-ip-address>
                <user-vlan-sub-interface>ont_ssh_ont_name</user-vlan-sub-interface>
              </access-entry>
            </debug-ont-ssh>         
    </config>
  </edit-config>
</rpc>
'''

get_access_entry='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
            <debug-ont-ssh-state xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
              <access-entry>
              <name>ont_name</name>
              </access-entry>
            </debug-ont-ssh-state>
    </filter>                                   
  </get>
</rpc>
'''
get_gem_running='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<bbf-xpongemtcont:xpongemtcont xmlns:bbf-xpongemtcont="urn:bbf:yang:bbf-xpongemtcont">
				<bbf-xpongemtcont:gemports>
					<bbf-xpongemtcont:gemport>
						<bbf-xpongemtcont:name>ont_ssh_gem_ont_name</bbf-xpongemtcont:name>
					</bbf-xpongemtcont:gemport>
				</bbf-xpongemtcont:gemports>
			</bbf-xpongemtcont:xpongemtcont>
		</filter>
	</get>
</rpc>
'''
create_gem='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
      <running/>
    </target>
    <config>
            <xpongemtcont xmlns="urn:bbf:yang:bbf-xpongemtcont">
              <gemports>
                <gemport>
                  <name>ont_ssh_gem_ont_name</name>
                  <gemport-id>gemportid</gemport-id>
                  <interface>ont_ssh_ont_name</interface>
                  <traffic-class>0</traffic-class>
                </gemport>
              </gemports>
            </xpongemtcont>          
    </config>
  </edit-config>
</rpc>

'''

get_access_entry_running='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<get>
		<filter type="subtree">
			<debug-ont-ssh xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
				<access-entry>
					<name>ont_name</name>
					<ont-mac-address></ont-mac-address>
					<user-vlan-sub-interface></user-vlan-sub-interface>
					<client-ip-address></client-ip-address>
				</access-entry>
			</debug-ont-ssh>
		</filter>
	</get>
</rpc>
'''

delete_ont_ssh='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
	<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
		<target>
			<running/>
		</target>
		<config>
			<xpongemtcont xmlns="urn:bbf:yang:bbf-xpongemtcont">
				<gemports>
					<gemport xc:operation="remove">
						<name>ont_ssh_gem_ont_name</name>
					</gemport>
				</gemports>
			</xpongemtcont>
			<debug-ont-ssh xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ont-remote-debug">
				<access-entry xc:operation="remove">
					<name>ont_name</name>
				</access-entry>
			</debug-ont-ssh>
			<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<interface xc:operation="remove">
					<name>ont_ssh_ont_name</name>
				</interface>
				<interface>
					<name>channel_partition</name>
					<tm-root xmlns="urn:bbf:yang:bbf-qos-traffic-mngt">
						<child-scheduler-nodes xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling" xc:operation="remove" >
							<name>node_ont_ssh_ont_name</name>
						</child-scheduler-nodes>
						<scheduler-node xmlns="urn:bbf:yang:bbf-qos-enhanced-scheduling" xc:operation="remove" >
						<name>node_ont_ssh_ont_name</name>
						</scheduler-node>					
					</tm-root>
				</interface>
			</interfaces>
			<qos-policy-profiles xmlns="urn:bbf:yang:bbf-qos-policies">
				<policy-profile xc:operation="remove">
					<name>ont_name</name>
				</policy-profile>
			</qos-policy-profiles>
			<policies xmlns="urn:bbf:yang:bbf-qos-policies">
				<policy xc:operation="remove">
					<name>ont_name</name>
				</policy>
			</policies>
			<classifiers xmlns="urn:bbf:yang:bbf-qos-classifiers">
				<classifier-entry xc:operation="remove">
					<name>ont_name</name>
				</classifier-entry>
			</classifiers>
		</config>
	</edit-config>
</rpc>
'''


get_alarm='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <al:alarms xmlns:al="urn:ietf:params:xml:ns:yang:ietf-alarms">
        <al:alarm-list/>
      </al:alarms>
    </filter>
  </get>
</rpc>
'''
aes_enable='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="138">
	<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
		<target>
			<running/>
		</target>
		<config>
			<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<interface>
					<name>ont_name</name>
					<v-ani xmlns="urn:bbf:yang:bbf-xponvani">
						<management-gemport-aes-indicator>true</management-gemport-aes-indicator>
					</v-ani>
				</interface>
			</interfaces>
		</config>
	</edit-config>
</rpc>
'''

aes_disable='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="138">
	<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
		<target>
			<running/>
		</target>
		<config>
			<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<interface>
					<name>ont_name</name>
					<v-ani xmlns="urn:bbf:yang:bbf-xponvani">
						<management-gemport-aes-indicator>false</management-gemport-aes-indicator>
					</v-ani>
				</interface>
			</interfaces>
		</config>
	</edit-config>
</rpc>
'''

aes_get='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
	<get>
		<filter type="subtree">
			<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
				<interface>
					<name>ont_name</name>
					<v-ani xmlns="urn:bbf:yang:bbf-xponvani">
						<management-gemport-aes-indicator/>
					</v-ani>
				</interface>
			</interfaces>
		</filter>
	</get>
</rpc>
'''
