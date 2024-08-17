import argparse as ap
import commands
def main(**args):
    ip = args.get("nmap")
    if ip:
        scan_result = commands.nmap.run_nmap_scan(ip)
        if scan_result:
            commands.nmap.analyze_with_openai(scan_result)
    links = args.get("links")
    if links:
        commands.links.get_links(links)

if "__main__" == __name__:
    parser = ap.ArgumentParser()
    parser.add_argument("--nmap", help="ip address to scan")
    parser.add_argument("--links", help="get all links of url")
    args = parser.parse_args()
    main(**vars(args))
