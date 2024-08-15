{
    'Vpcs': [
        {
            'CidrBlock': 'string',
            'DhcpOptionsId': 'string',
            'State': 'pending'|'available',
            'VpcId': 'string',
            'OwnerId': 'string',
            'InstanceTenancy': 'default'|'dedicated'|'host',
            'Ipv6CidrBlockAssociationSet': [
                {
                    'AssociationId': 'string',
                    'Ipv6CidrBlock': 'string',
                    'Ipv6CidrBlockState': {
                        'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                        'StatusMessage': 'string'
                    },
                    'NetworkBorderGroup': 'string',
                    'Ipv6Pool': 'string',
                    'Ipv6AddressAttribute': 'public'|'private',
                    'IpSource': 'amazon'|'byoip'|'none'
                },
            ],
            'CidrBlockAssociationSet': [
                {
                    'AssociationId': 'string',
                    'CidrBlock': 'string',
                    'CidrBlockState': {
                        'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                        'StatusMessage': 'string'
                    }
                },
            ],
            'IsDefault': True|False,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}