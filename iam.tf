resource "aws_iam_role" "role" {
  name = "role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = [
          "ecs.amazonaws.com",
          "ecs-tasks.amazonaws.com"
          ]
        }
      },
    ]
  })

  tags = {
    tag-key = "tag-value"
  }
}

output "role" {
  value       = aws_iam_role.role
  description = "The private IP address of the main server instance."
}
