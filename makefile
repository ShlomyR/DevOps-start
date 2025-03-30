terraform-init:
	terraform -chdir=02-Automate_Infrastructure_Deployment_with_Terraform/Terraform init && \
	terraform -chdir=02-Automate_Infrastructure_Deployment_with_Terraform/Terraform apply -auto-approve

clean:
	rm -rf 02-Automate_Infrastructure_Deployment_with_Terraform/Terraform/.terraform \
	       02-Automate_Infrastructure_Deployment_with_Terraform/Terraform/terraform.tfstate*