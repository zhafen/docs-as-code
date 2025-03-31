# Terraform Demo Configuration

# Specify the required Terraform version
terraform {
    required_version = ">= 1.0.0"
}

# Configure the provider (e.g., AWS)
provider "aws" {
    region = "us-east-1"
}

# Create a resource (e.g., an AWS S3 bucket)
resource "aws_s3_bucket" "demo_bucket" {
    bucket = "terraform-demo-bucket-${random_id.bucket_id.hex}"
    acl    = "private"

    tags = {
        Name        = "TerraformDemoBucket"
        Environment = "Demo"
    }
}

# Generate a random ID for unique bucket naming
resource "random_id" "bucket_id" {
    byte_length = 8
}

# Output the bucket name
output "bucket_name" {
    value = aws_s3_bucket.demo_bucket.bucket
}