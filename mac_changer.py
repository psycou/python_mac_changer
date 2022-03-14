
import subprocess
import optparse
import re as re




def get_arguments():
    parser = optparse.OptionParser()
    
    parser.add_option("-i", "--interface", dest="interface", help="The interface To change Mac adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New Mac adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help fom more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac adress, use --help fom more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC adress for " + interface + " to " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_mac_add(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_adress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_adress_search_result:
        return mac_adress_search_result.group(0)
    else:
        print("[-] could not read Mac address") 




options = get_arguments()

current_mac = get_mac_add(options.interface)
print("[+] Current Mac = " + str(current_mac))
   
change_mac(options.interface, options.new_mac)

current_mac = get_mac_add(options.interface)

if current_mac == options.new_mac:
    print("[+] Adress Mac chnaged Successfully to " + current_mac)

else:
    print("[-] Something Went Wrong")