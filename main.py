import argparse as ap
import commands
def main(**args):
    ip = args.get("nmap")
    if ip:
        scan_result = commands.nmap.run_nmap_scan(ip)
        if scan_result and args.get("IA"):
            commands.nmap.analyze_with_openai(scan_result)

    links = args.get("links")
    if links:
        scan_links = commands.links.get_links(links)
        if scan_links and args.get("IA"):
            commands.links.analyze_with_openai(scan_links)


if "__main__" == __name__:
    parser = ap.ArgumentParser()
    parser.add_argument("--nmap", help="ip address to scan")
    parser.add_argument("--links", help="get all links of url")
    parser.add_argument("--IA", action="store_true", help="Set IA to analyze results")
    args = parser.parse_args()
    main(**vars(args))
