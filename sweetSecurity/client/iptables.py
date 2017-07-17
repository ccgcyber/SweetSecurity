import sweetSecurityDB

def writeHeader():
	dfgw=sweetSecurityDB.getDfgw()
	dfgw=dfgw['dfgw']
	f = open('/opt/sweetsecurity/client/iptables_new.sh','w')
	f.write('IPTABLES=/sbin/iptables\n')
	f.write('sudo ${IPTABLES} --flush\n')
	f.write('sudo ${IPTABLES} --delete-chain\n')
	f.write('sudo ${IPTABLES} --table nat --flush\n')
	f.write('sudo ${IPTABLES} --table nat --delete-chain\n')
	f.write('sudo ${IPTABLES} -P INPUT ACCEPT\n')
	f.write('sudo ${IPTABLES} -P FORWARD ACCEPT\n')
	f.write('sudo ${IPTABLES} -P OUTPUT ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -i lo -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -o lo -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -p ICMP -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A FORWARD -p ICMP -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -p ICMP -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -p tcp --sport 22 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -p tcp --dport 22 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -p tcp --sport 22 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -p udp --dport 67 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -p udp --dport 67 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -p udp --dport 5353 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -p udp --dport 5353 -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -s "%s" -j ACCEPT\n' % dfgw)
	f.write('sudo ${IPTABLES} -A FORWARD -s "%s" -j ACCEPT\n' % dfgw)
	f.write('sudo ${IPTABLES} -A FORWARD -d "%s" -j ACCEPT\n' % dfgw)
	f.write('sudo ${IPTABLES} -A OUTPUT -s "%s" -j ACCEPT\n' % dfgw)
	f.write('sudo ${IPTABLES} -A FORWARD -s "224.0.0.251" -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A OUTPUT -s "224.0.0.251" -j ACCEPT\n')
	f.write('sudo ${IPTABLES} -A INPUT -s "224.0.0.251" -j ACCEPT\n')
	f.close()
def writeFooter():
	f = open('/opt/sweetsecurity/client/iptables_new.sh','a')
	f.write('sudo ${IPTABLES} -N LOGGING\n')
	f.write('sudo ${IPTABLES} -A FORWARD -j LOGGING\n')
	#f.write('sudo ${IPTABLES} -A LOGGING -m limit --limit 50/min -j LOG --log-prefix "IPTables-Dropped: " --log-level 4\n')
	f.write('sudo ${IPTABLES} -A LOGGING -j LOG --log-prefix "IPTables-Dropped: " --log-level 4\n')
	f.write('sudo ${IPTABLES} -A LOGGING -j DROP\n')
	f.write('sudo iptables-save\n')
	f.close()

def addSimple(source,action):
	f = open('/opt/sweetsecurity/client/iptables_new.sh','a')
	f.write('sudo ${IPTABLES} -A FORWARD -s "%s" -j %s\n' % (source,action))
	f.write('sudo ${IPTABLES} -A FORWARD -d "%s" -j %s\n' % (source,action))
	f.close()

def addFull(source,destination,action):
	f = open('/opt/sweetsecurity/client/iptables_new.sh','a')
	f.write('sudo ${IPTABLES} -A FORWARD -s "%s" -d "%s" -j %s\n' % (source,destination,action))
	f.write('sudo ${IPTABLES} -A FORWARD -s "%s" -d "%s" -j %s\n' % (destination,source,action))
	f.close()
