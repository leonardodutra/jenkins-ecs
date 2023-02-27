terraform {
  backend "s3" {
    encrypt = true
    bucket = "totalexpress-devsecops-terraform-cicd-hom"
    dynamodb_table = "totalexpress-devsecops-terraform-cicd-hom"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
