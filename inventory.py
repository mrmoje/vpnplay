#!/usr/bin/env python

import argparse
import json
import sys
from os import getenv


def main(parser=None):
    try:
        if parser is None:
            parser = make_parser()

        args = parser.parse_args()

        if args.list:
            output = get_list(env, args.json_file)
            print json.dumps(output, indent=4, separators=(',', ': '),
                             sort_keys=True)
        elif args.host:
            output = get_host(env, args.host, args.json_file)
            print json.dumps(output, indent=4, separators=(',', ': '),
                             sort_keys=True)
        else:
            parser.print_usage()
        return 0
    except KeyboardInterrupt:
        return


def make_parser():
    parser = argparse.ArgumentParser(description='Ansible Dynamic Inventory.')

    parser.add_argument('--list', dest='list',
                        help='List Ansible groups', action='store_true')
    parser.add_argument('--host', dest='host',
                        help='Get attributes for a specific host')
    parser.add_argument('--json-file', dest='json_file', default='inventory.json',
                        help='Set Json file')
    return parser


def staging_local_host_shiv(host):
    return host.replace('.', '-') if env == 'local' else host


def get_environment_inventory(env, json_file):

    with open(json_file) as inventory_json:
        inventory_data = json.load(inventory_json)

    output = inventory_data.get('common')
    env_dat = inventory_data.get(env) or {'common': {'all': output['all']}}

    if env_dat.get('override') == 'all':
        output = env_dat['common']
    else:
        for group, group_dat in output.iteritems():
            if group_dat.get('hosts'):
                output[group]['hosts'] = [
                    staging_local_host_shiv(host) + '.' +
                    env_dat['common']['all']['vars']['domain']
                    for host in group_dat.get('hosts')]

        output.update(env_dat.get('common'))

    return output


def get_list(env, json_file):
    return get_environment_inventory(env, json_file)


def get_host(env, host, json_file):
    return dict()


if __name__ == '__main__':
    env = getenv('DEPLOY_TO_ENV', 'local')
    if env not in ['local', 'vpnserv_1']:
        sys.exit(1)
    sys.exit(main())

# end of script
