Certainly! Here’s a more concise version of the `README.md` file:

---

# VPC Listing Scripts

## Overview

Scripts for listing AWS VPCs using `boto3`.

## Scripts

### `vpc-listing.py`
Lists VPCs and their CIDR blocks in the default region.

### `vpc-listing-different-region.py`
Lists VPCs and CIDR block states in the `eu-central-1` region.

## Requirements

- Python 3.x
- `boto3` library

Install `boto3` with:
```bash
pip install boto3
```

Ensure AWS credentials are configured. Check:
```
aws configure list
```

---