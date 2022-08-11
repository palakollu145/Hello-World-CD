import yaml
import sys

if __name__ == "__main__":
    image = sys.argv[1]
    with open("values.yaml") as f:
        y = yaml.safe_load(f)
        y['image'] = 'lakshitsainiceligo/qa:' + image
        print(yaml.dump(y, default_flow_style=False, sort_keys=False))

    with open('values.yaml', 'w') as file:
        yaml.dump(y, file)
