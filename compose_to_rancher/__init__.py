"""Convert a docker-compose.yml file version 2 to a docker-compose-v1.yml \
version 1, compatible with Rancher"""
import argparse
import yaml

default_file_path = 'docker-compose.yml'
default_output_file_path = 'docker-compose-v1.yml'


def convert_compose_to_rancher(compose_v2_data):
    """
    Convert a parsed yaml data structure docker-compose V2 to a \
    V1 docker-compose data structure
    """
    new_compose = {}
    for service, contents in compose_v2_data['services'].items():
        new_compose[service] = {}
        for key in contents:
            if key != 'build':
                new_compose[service][key] = contents[key]
        if 'image' not in contents:
            raise ValueError('no image in service {}'.format(key))
    return new_compose


def read_write_compose(file_path, output_file_path):
    """
    Read a Docker Compose V2 file in file_path and write a Rancher compatible \
    Docker Compose file V1 in output_file_path
    """
    with open(file_path) as f:
        compose_v2_data = yaml.load(f)

    new_compose = convert_compose_to_rancher(compose_v2_data)

    yaml_out = yaml.dump(new_compose, default_flow_style=False)
    with open(output_file_path, mode='w') as f_out:
        f_out.write(yaml_out)


def main():
    """
    Read and parse the command line and convert Docker Compose V2 to a \
    Rancher compatible Docker Compose V1
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', default=default_file_path,
                        help='the input docker-compose.yml file in version 2')
    parser.add_argument('-o', '--output', default=default_output_file_path,
                        help='the output to write a docker-compose.yml version \
                        1 compatible with Rancher')
    args = parser.parse_args()
    file_path = args.file
    output_file_path = args.output
    read_write_compose(file_path, output_file_path)

if __name__ == '__main__':
    main()
