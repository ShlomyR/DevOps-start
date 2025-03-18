provider "azurerm" {
  features {}
  subscription_id = "fa2658e7-e031-4256-bb9f-aae52ce91263"
}


resource "azurerm_resource_group" "devops_rg" {
  name     = "shlomyGroupTest"
  location = "Israel Central"
}

resource "azurerm_container_registry" "acr" {
  name                = "mydevopsacr"
  resource_group_name = azurerm_resource_group.devops_rg.name
  location           = azurerm_resource_group.devops_rg.location
  sku                = "Basic"
  admin_enabled      = true
}
