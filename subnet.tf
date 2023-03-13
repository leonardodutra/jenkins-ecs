data "aws_availability_zones" "available" {
  state = "available"
}
resource "aws_subnet" "subnet" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Name = "tcb_blog_public_subnet"
  }
}
resource "aws_subnet" "subnet2" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = data.aws_availability_zones.available.names[1]

  tags = {
    Name = "subnet2"
  }
}


resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "tcb_blog_igw"
  }
}
resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "rt"
  }
}

# Criação da Rota Default para Acesso à Internet
resource "aws_route" "tcb_blog_routetointernet" {
  route_table_id            = aws_route_table.rt.id
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id                = aws_internet_gateway.igw.id
}

resource "aws_route_table_association" "tcb_blog_pub_association" {
  subnet_id      = aws_subnet.subnet.id
  route_table_id = aws_route_table.rt.id
}


output "subnet" {
  value       = aws_subnet.subnet
  description = "The private IP address of the main server instance."
}
