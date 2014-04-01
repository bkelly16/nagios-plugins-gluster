nfsEnabled1 = {'rep1': {'brickCount': '2',
          'bricks': ['10.70.43.33:/bricks/rep1_1',
                     '10.70.43.33:/bricks/rep1_2'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '53496a0c-94eb-46a2-9312-eeb700e9fba5',
          'volumeName': 'rep1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'REPLICATE'},
 'vol1': {'brickCount': '3',
          'bricks': ['10.70.43.33:/bricks/b1',
                     '10.70.43.33:/bricks/my-vol1-add-brck-b2.new',
                     '10.70.43.33:/bricks/vol1/my-new-brick_b3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'f96856f1-b2c0-4e24-aef0-7f2a01f37b99',
          'volumeName': 'vol1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'},
 'vol2': {'brickCount': '1',
          'bricks': ['10.70.43.190:/exports/vol2'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '12817858-77cd-450d-8a70-f8d617db838e',
          'volumeName': 'vol2',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'},
 'vol3': {'brickCount': '1',
          'bricks': ['10.70.43.190:/exports/vol3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'a3d0f537-761f-46d3-addd-58c5eeb66b58',
          'volumeName': 'vol3',
          'volumeStatus': 'OFFLINE',
          'volumeType': 'DISTRIBUTE'},
 'vol4': {'brickCount': '2',
          'bricks': ['10.70.43.190:/bricks/vol3_a',
                     '10.70.43.190:/bricks/vol3_b'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '81201e32-8f14-4fa0-b4ef-23852f2f9a1d',
          'volumeName': 'vol4',
          'volumeStatus': 'OFFLINE',
          'volumeType': 'REPLICATE'},
 'vol5': {'brickCount': '3',
          'bricks': ['10.70.43.190:/bricks/vol5_a',
                     '10.70.42.228:/bricks/vol5_b',
                     '10.70.43.33:/bricks/vol5_c'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '69e039dd-e0b1-4069-ad65-99cb26c2d157',
          'volumeName': 'vol5',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'}}

# nfs enabled by default
nfsEnabled2 = {'rep1': {'brickCount': '2',
          'bricks': ['10.70.43.133:/bricks/rep1_1',
                     '10.70.43.133:/bricks/rep1_2'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '53496a0c-94eb-46a2-9312-eeb700e9fba5',
          'volumeName': 'rep1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'REPLICATE'}}

#NFS enabled using set option
nfsEnabled3 = {'vol1': {'brickCount': '3',
          'bricks': ['10.70.43.33:/bricks/b1',
                     '10.70.43.33:/bricks/my-vol1-add-brck-b2.new',
                     '10.70.43.33:/bricks/vol1/my-new-brick_b3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on', 'nfs.disable': 'off'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'f96856f1-b2c0-4e24-aef0-7f2a01f37b99',
          'volumeName': 'vol1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'}}


nfsDisabled1 = {'vol1': {'brickCount': '3',
          'bricks': ['10.70.43.33:/bricks/b1',
                     '10.70.43.33:/bricks/my-vol1-add-brck-b2.new',
                     '10.70.43.33:/bricks/vol1/my-new-brick_b3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'f96856f1-b2c0-4e24-aef0-7f2a01f37b99',
          'volumeName': 'vol1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'},
 'rep1': {'brickCount': '2',
          'bricks': ['10.70.43.133:/bricks/rep1_1',
                     '10.70.43.133:/bricks/rep1_2'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '53496a0c-94eb-46a2-9312-eeb700e9fba5',
          'volumeName': 'rep1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'REPLICATE'}}


brickTst1 = {'vol1': {'brickCount': '3',
          'bricks': ['10.70.43.33:/bricks/b1',
                     '10.70.43.433:/bricks/my-vol1-add-brck-b2.new',
                     '10.70.43.33:/bricks/vol1/my-new-brick_b3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'f96856f1-b2c0-4e24-aef0-7f2a01f37b99',
          'volumeName': 'vol1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'},
 'rep1': {'brickCount': '2',
          'bricks': ['10.70.43.133:/bricks/rep1_1',
                     '10.70.43.133:/bricks/rep1_2'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '53496a0c-94eb-46a2-9312-eeb700e9fba5',
          'volumeName': 'rep1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'REPLICATE'}}


brickTst2 = {'vol1': {'brickCount': '3',
          'bricks': ['10.70.43.133:/bricks/b1',
                     '10.70.43.233:/bricks/my-vol1-add-brck-b2.new',
                     '10.70.43.333:/bricks/vol1/my-new-brick_b3'],
          'bricksInfo': [],
          'distCount': '1',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '1',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': 'f96856f1-b2c0-4e24-aef0-7f2a01f37b99',
          'volumeName': 'vol1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'DISTRIBUTE'},
 'rep1': {'brickCount': '2',
          'bricks': ['10.70.43.133:/bricks/rep1_1',
                     '10.70.43.133:/bricks/rep1_2'],
          'bricksInfo': [],
          'distCount': '2',
          'options': {'features.quota': 'on', 'nfs.disable': 'on'},
          'replicaCount': '2',
          'stripeCount': '1',
          'transportType': ['TCP'],
          'uuid': '53496a0c-94eb-46a2-9312-eeb700e9fba5',
          'volumeName': 'rep1',
          'volumeStatus': 'ONLINE',
          'volumeType': 'REPLICATE'}}
