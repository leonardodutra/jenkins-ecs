resource "aws_cloudwatch_log_group" "ecs" {
  name = "ecs"

  tags = {
    Environment = "production"
    Application = "serviceA"
  }
}
