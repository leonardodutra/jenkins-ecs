# Criação da VPC
resource "aws_vpc" "tcb_blog_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "tcb_blog_vpc"
  }
}