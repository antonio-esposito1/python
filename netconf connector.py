import requests

url = "http://lab0:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/mivpe015"

payload="<node xmlns=\"urn:TBD:params:xml:ns:yang:network-topology\">\n  <node-id>mivpe015</node-id>\n  <host xmlns=\"urn:opendaylight:netconf-node-topology\">172.16.1.85</host>\n  <port xmlns=\"urn:opendaylight:netconf-node-topology\">830</port>\n  <username xmlns=\"urn:opendaylight:netconf-node-topology\">antonio</username>\n  <password xmlns=\"urn:opendaylight:netconf-node-topology\">admin</password>\n  <tcp-only xmlns=\"urn:opendaylight:netconf-node-topology\">false</tcp-only>\n  <schemaless xmlns=\"urn:opendaylight:netconf-node-topology\">false</schemaless>\n</node>\n"
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)



