resource "aws_subnet" "tcb_blog_public_subnet" {
  vpc_id     = aws_vpc.tcb_blog_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "tcb_blog_public_subnet"
  }
}

resource "aws_internet_gateway" "tcb_blog_igw" {
  vpc_id = aws_vpc.tcb_blog_vpc.id

  tags = {
    Name = "tcb_blog_igw"
  }
}
resource "aws_route_table" "tcb_blog_rt" {
  vpc_id = aws_vpc.tcb_blog_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.tcb_blog_igw.id
  }

  tags = {
    Name = "tcb_blog_rt"
  }
}

# Criação da Rota Default para Acesso à Internet
resource "aws_route" "tcb_blog_routetointernet" {
  route_table_id            = aws_route_table.tcb_blog_rt.id
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id                = aws_internet_gateway.tcb_blog_igw.id
}

resource "aws_route_table_association" "tcb_blog_pub_association" {
  subnet_id      = aws_subnet.tcb_blog_public_subnet.id
  route_table_id = aws_route_table.tcb_blog_rt.id
}