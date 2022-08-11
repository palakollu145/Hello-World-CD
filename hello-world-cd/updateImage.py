import yaml

fname = "values.yaml"

stream = open(fname, 'r')
data = yaml.load(stream,Loader=yaml.SafeLoader)

data['image'] = 'lakshitsainiceligo/qa:HelloWorld_1.0.0.13.0'

with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
