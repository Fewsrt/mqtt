pty "pptp $fasacserver.ddns.net --nolaunchpppd --debug"
name $vpn
password $vpn
remotename PPTP
require-mppe-128
require-mschap-v2
refuse-eap
refuse-pap
refuse-chap
refuse-mschap
noauth
debug
persist
maxfail 0
defaultroute
replacedefaultroute
usepeerdns