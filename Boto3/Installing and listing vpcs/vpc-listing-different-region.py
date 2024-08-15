import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")

all_ec2_vpc_list = ec2_client.describe_vpcs()

vpcs = all_ec2_vpc_list["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidrblock_id = vpc["CidrBlockAssociationSet"]

    for cidr_id in cidrblock_id:
        print(cidr_id["CidrBlockState"])