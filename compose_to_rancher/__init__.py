"""Convert a docker-compose.yml file version 2 to a docker-compose-v1.yml \
version 1, compatible with Rancher"""
import argparse
import yaml

default_file_path = 'docker-compose.yml'
default_output_file_path = 'docker-compose-v1.yml'

EXCLUDED_OPTIONS = ['build', 'depends_on']

#######################
# Base Functions
#######################

def convert_compose_to_rancher(compose_v2_data):
    """
    Convert a parsed yaml data structure docker-compose V2 to a \
    V1 docker-compose data structure
    """
    new_compose = {}
    for service, service_options in compose_v2_data['services'].items():
        #error if no image option is declared
        if 'image' not in service_options:
            raise ValueError('No "image" option in service "{0}"'.format(service))

        #create new dictionary
        new_compose[service] = {}

        for option in service_options:
            if option == 'depends_on':
                add_or_merge(new_compose[service], 'links', service_options['depends_on'])

            if option not in EXCLUDED_OPTIONS:
                add_or_merge(new_compose[service], option, service_options[option])


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

#######################
# Main
#######################

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

#######################
# Utility Functions
#######################

def add_or_merge(dictionary, key, values):
    """
    Add or merge the values in 'values' to 'dictionary' at 'key'
    """
    if key in dictionary:
        if isinstance(values, list):
            dictionary[key] = dictionary[key] + values
        else:
            dictionary[key].update(values)
    else:
        dictionary[key] = values

    return dictionary

#######################
# Init
#######################

if __name__ == '__main__':
    main()
