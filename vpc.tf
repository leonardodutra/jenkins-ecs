# Criação da VPC
resource "aws_vpc" "vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "vpc"
  }
}
output "vpc" {
  value       = aws_vpc.vpc
  description = "The private IP address of the main server instance."
}
